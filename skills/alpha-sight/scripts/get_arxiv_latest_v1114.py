import arxiv
import csv
from datetime import datetime, timedelta
import time
import os
import requests
from urllib.parse import urlencode
import re
from bs4 import BeautifulSoup


def load_signal_authors(file_path):
    """加载信号源看板中的作者名单"""
    authors = set()
    try:
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row.get('name'):
                    author_name = row['name'].strip().title()
                    authors.add(author_name)
    except Exception as e:
        print(f"⚠️ 加载信号源文件出错: {e}")
    return authors

def get_daily_submission_count(category, type):
    """获取指定类别的新提交论文数量"""
    try:
        url = f"https://arxiv.org/list/{category}/{type}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        if response.status_code == 429:
            retry = int(response.headers.get("Retry-After", 10))
            print(f"⏳ 被限流，等待 {retry} 秒后重试...")
            time.sleep(retry)
            response = requests.get(url, headers=headers, timeout=10)

        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # 查找"Total of XX entries"文本
        total_text = soup.find(string=re.compile(r'Total of \d+ entries'))
        if total_text:
            # 提取数字
            match = re.search(r'Total of (\d+) entries', total_text)
            if match:
                count = int(match.group(1))
                print(f"   📊 {category}: {count} 篇新提交")
                return count
        
        # 如果没找到，尝试备用方法
        dd_tags = soup.find_all('dd')
        if dd_tags:
            count = len(dd_tags)
            print(f"   📊 {category}: ~{count} 篇新提交 (备用计数)")
            return count
            
        print(f"   ⚠️ {category}: 无法获取提交数量")
        return 0
        
    except Exception as e:
        print(f"   ❌ {category}: 获取提交数量失败 - {e}")
        return 0

def get_category_submission_counts(categories, type):
    """批量获取所有类别的当天提交数量"""
    print("🔍 获取各类别当天新提交数量...")
    category_counts = {}
    total_count = 0
    
    for category in categories:
        count = get_daily_submission_count(category, type)
        category_counts[category] = count
        total_count += count
        time.sleep(0.5)  # 避免请求过于频繁
    
    print(f"📈 总计: {total_count} 篇新提交论文")
    return category_counts, total_count

def normalize_author_name(name):
    """标准化作者名字格式"""
    return name.strip().title()

def clean_abstract(abstract):
    """清理和格式化摘要文本"""
    if not abstract:
        return ""
    
    # 移除多余的空白字符和换行符
    cleaned = abstract.strip().replace('\n', ' ').replace('\r', ' ')
    # 替换多个空格为单个空格
    cleaned = ' '.join(cleaned.split())
    
    return cleaned

def format_arxiv_url(entry_id):
    """格式化arXiv链接为标准格式"""
    # 从entry_id中提取论文ID
    if '/' in entry_id:
        paper_id = entry_id.split('/')[-1]
    else:
        paper_id = entry_id
    
    # 移除版本号（如果有的话）
    if 'v' in paper_id and paper_id.split('v')[-1].isdigit():
        paper_id = paper_id.split('v')[0]
    
    # 确保返回标准的arXiv abs URL格式
    return f"https://arxiv.org/abs/{paper_id}"


def _ping_arxiv():
    """只测连通性，不测数据量"""
    try:
        h = {"User-Agent": "QijiFetcher/1.0 (contact: youremail@example.com)"}
        r = requests.get(
            "https://export.arxiv.org/api/query",
            params={"search_query": "all:ai", "max_results": 1},
            headers=h, timeout=20
        )
        return r.status_code == 200
    except Exception:
        return False

def test_arxiv_connection():
    """测试 arXiv：使用日期范围查询最新论文"""
    try:
        print("🔍 测试arXiv连接...")
        os.environ["ARXIV_USER_AGENT"] = "QijiFetcher/1.0 (contact: youremail@example.com)"
        if not _ping_arxiv():
            print("❌ 连通性测试失败（无法获得 200）")
            return False

        import arxiv
        client = arxiv.Client(page_size=5, delay_seconds=5, num_retries=8)
        
        # 使用日期范围查询最近3天的论文
        today = datetime.now().date()
        start_date = today - timedelta(days=3)
        date_query = f"submittedDate:[{start_date.strftime('%Y%m%d')}0000 TO {today.strftime('%Y%m%d')}2359]"
        
        search = arxiv.Search(
            query=f"cat:cs.AI AND {date_query}",
            max_results=5,
            sort_by=arxiv.SortCriterion.SubmittedDate,
            sort_order=arxiv.SortOrder.Descending
        )
        results = list(client.results(search))
        if results:
            print("✅ arXiv连接正常（拿到最新结果）")
            latest_paper = results[0]
            print(f"   最新论文示例: {latest_paper.title[:50]}...")
            print(f"   发布日期: {latest_paper.published.date()}")
            print(f"   更新日期: {latest_paper.updated.date()}")
        else:
            print("⚠️ 连接正常，但最近3天没有 cs.AI 论文")
        return True
    except Exception as e:
        print(f"❌ arXiv连接测试失败（异常）：{e}")
        return False


def probe_api_batch_top_dates(start_date, end_date):
    """批次探针：使用日期范围查询确认能否获取到指定日期的论文"""
    try:
        client = arxiv.Client(page_size=10, delay_seconds=3.2)
        
        # 构造日期范围查询
        date_query = f"submittedDate:[{start_date.strftime('%Y%m%d')}0000 TO {end_date.strftime('%Y%m%d')}2359]"
        
        search = arxiv.Search(
            query=f"cat:cs.AI AND {date_query}",
            sort_by=arxiv.SortCriterion.SubmittedDate,
            sort_order=arxiv.SortOrder.Descending,
            max_results=5
        )
        top = []
        for r in client.results(search):
            top.append((r.published.date().isoformat(), r.title[:60]))
        
        if top:
            print("🧪 API 顶部5条论文日期：")
            for d, t in top:
                print("   ", d, "|", t)
            return [d for d, _ in top]
        else:
            print("⚠️ 指定日期范围内没有找到论文")
            return []
            
    except Exception as e:
        print(f"❌ 批次探针失败: {e}")
        return []

def should_proceed_today(latest_dates_iso, expect_floor):
    """
    检查API批次是否已更新到期望的日期
    latest_dates_iso: probe_api_batch_top_dates() 返回的日期字符串列表
    expect_floor: 你希望至少看到的最晚日期（比如今天-1天，或 start_date）
    """
    if not latest_dates_iso:
        print("⚠️ 无法获取API顶部日期，但仍继续执行")
        return True
    
    try:
        # API 已滚到 >= 期望下限日期，才继续抓
        latest = max(datetime.fromisoformat(d).date() for d in latest_dates_iso)
        if latest >= expect_floor:
            print(f"✅ API已有 {latest} 的论文，满足期望日期 {expect_floor}")
            return True
        else:
            print(f"⏸️ API最新论文日期是 {latest}，尚未到 {expect_floor}。先跳过本次抓取。")
            return False
    except Exception as e:
        print(f"⚠️ 解析日期时出错: {e}，继续执行")
        return True

def get_latest_papers(signal_authors, start_date, end_date, category_counts=None):
    """获取最新论文的核心函数 - 使用日期范围查询"""
    
    print(f"📅 查询时间范围：{start_date} 至 {end_date}")
    print(f"📊 信号源作者数量：{len(signal_authors)}")
    
    # 生成输出文件名
    output_file = f"latest_arxiv_papers_{datetime.now().strftime('%Y%m%d_%H%M')}.csv"
    
    counter = 1
    base_name, ext = os.path.splitext(output_file)
    while os.path.exists(output_file):
        output_file = f"{base_name}_{counter}{ext}"
        counter += 1
    
    # 更保守的客户端配置
    client = arxiv.Client(
        page_size=100,  # 增加页面大小提高效率
        delay_seconds=3,
        num_retries=5
    )
    
    # 统计信息
    total_papers = 0
    matched_papers = 0
    date_stats = {}
    category_stats = {}
    processed_papers = set()
    all_papers_data = []
    
    print(f"\n🔍 开始查询论文（使用日期范围过滤）...")
    
    # 构造日期范围查询字符串
    date_query = f"submittedDate:[{start_date.strftime('%Y%m%d')}0000 TO {end_date.strftime('%Y%m%d')}2359]"
    print(f"📅 日期过滤: {date_query}")
    
    # 计算机科学相关类别（包括交叉学科）
    categories = [
        # 主要AI/ML相关
        "cs.AI", "cs.LG", "cs.CV", "cs.CL", "cs.NE", "cs.RO", "cs.IR",
        # 系统和架构
        "cs.DC", "cs.OS", "cs.AR", "cs.PF", "cs.NI",
        # 软件工程和编程语言
        "cs.SE", "cs.PL", "cs.LO", "cs.FL",
        # 理论计算机科学
        "cs.DS", "cs.CC", "cs.DM", "cs.GT", "cs.IT",
        # 应用领域
        "cs.DB", "cs.CR", "cs.GR", "cs.MM", "cs.HC", "cs.CY", "cs.ET",
        # 数学计算
        "cs.NA", "cs.MS", "cs.SC", "cs.CE",
        # 其他
        "cs.OH", "cs.SY",
        # 交叉学科
        "stat.ML", "math.OC", "math.ST", "eess.IV", "eess.SP", "eess.AS",
        "econ.EM", "q-bio.QM", "physics.data-an"
    ]
    
    for category in categories:
        print(f"\n🔍 查询类别: {category}")
        
        # 获取该类别的预期论文数量
        expected_count = category_counts.get(category, 0) if category_counts else 0
        
        try:
            # 关键修改：使用日期范围过滤
            query = f"cat:{category} AND {date_query}"
            
            # 根据预期数量调整查询上限
            max_results = max(expected_count * 2, 200) if expected_count > 0 else 2000
            print(f"📊 预期论文数: {expected_count}, 查询上限: {max_results}")
            print(f"🔎 查询语句: {query}")
            
            search = arxiv.Search(
                query=query,
                sort_by=arxiv.SortCriterion.SubmittedDate,
                sort_order=arxiv.SortOrder.Descending,
                max_results=max_results
            )
            
            category_count = 0
            category_matched = 0
            processed_in_category = 0
            
            print(f"      🔄 开始获取论文...")
            
            for result in client.results(search):
                try:
                    pub_date = result.published.date()
                    update_date = result.updated.date()
                    paper_id = result.entry_id.split('/')[-1]
                    processed_in_category += 1
                    
                    # 每处理50篇显示进度
                    if processed_in_category % 50 == 0:
                        print(f"      📊 已处理 {processed_in_category} 篇")
                    
                    # 检查是否已经处理过这篇论文
                    if paper_id in processed_papers:
                        continue
                    
                    # 日期范围已经在查询中过滤了，这里直接处理
                    authors = [normalize_author_name(a.name) for a in result.authors]
                    
                    # 将论文ID添加到已处理集合
                    processed_papers.add(paper_id)
                    
                    # 更新统计
                    date_str = pub_date.strftime("%Y-%m-%d")
                    date_stats[date_str] = date_stats.get(date_str, 0) + 1
                    category_stats[result.primary_category] = category_stats.get(result.primary_category, 0) + 1
                    
                    # 检查匹配的作者
                    matched_authors = [a for a in authors if a in signal_authors]
                    
                    # 只有匹配到信号源作者的论文才写入数据
                    if matched_authors:
                        formatted_url = format_arxiv_url(result.entry_id)
                        
                        # 准备论文数据
                        paper_data = {
                            'id': paper_id,
                            'title': result.title.strip().replace('\n', ' '),
                            'authors': ", ".join(authors),
                            'matched_authors': ", ".join(matched_authors),
                            'published_date': pub_date,
                            'primary_category': result.primary_category,
                            'all_categories': ", ".join(result.categories),
                            'abstract': clean_abstract(result.summary),
                            'abs_url': formatted_url,
                            'has_match': True
                        }
                        
                        all_papers_data.append(paper_data)
                        category_matched += 1
                        matched_papers += 1
                        print(f"         ✅ [{pub_date}] 匹配: {', '.join(matched_authors)} | {result.title[:40]}...")
                    
                    category_count += 1
                    total_papers += 1
                    
                    # 如果已获取足够数量且有预期，可以提前结束
                    if expected_count > 0 and category_count >= expected_count * 1.5:
                        print(f"      ✅ 已获取足够论文，提前结束")
                        break
                        
                except Exception as e:
                    print(f"         ⚠️ 处理论文时出错: {e}")
                    continue
            
            print(f"      📊 {category}: {category_count}篇论文, {category_matched}篇匹配")
            
        except Exception as e:
            print(f"      ❌ 类别 {category} 查询出错: {e}")
            continue
    
    # 写入CSV文件 - 只写入匹配的论文
    print(f"\n📝 写入CSV文件，共 {len(all_papers_data)} 篇匹配论文...")
    
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Title", "Authors", "Matched_Authors", "Published_Date","Primary_Category", "All_Categories", "Abstract", "Abstract_URL"])
        
        # 按发布日期排序，最新的在前
        all_papers_data.sort(key=lambda x: x['published_date'], reverse=True)
        
        for paper in all_papers_data:
            writer.writerow([
                paper['id'],
                paper['title'],
                paper['authors'],
                paper['matched_authors'],
                paper['published_date'],
                paper['primary_category'],
                paper['all_categories'],
                paper['abstract'],
                paper['abs_url']
            ])
    
    print(f"✅ 数据写入完成，共写入 {len(all_papers_data)} 篇匹配论文")
    
    return output_file, total_papers, matched_papers, date_stats, category_stats

def preview_csv(file_path):
    """预览CSV文件前几行"""
    print(f"\n📄 {file_path} 预览:")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for i, line in enumerate(lines[:4]):
                print(f"   {line.strip()}")
    except Exception as e:
        print(f"⚠️ 预览文件出错: {e}")

def print_results(output_file, total_papers, matched_papers, date_stats, category_stats):
    """打印结果统计"""
    print(f"\n📊 爬取完成!")
    print(f"   • 总论文数: {total_papers}")
    print(f"   • 匹配论文数: {matched_papers}")
    print(f"   • 匹配率: {matched_papers/total_papers*100:.1f}%" if total_papers > 0 else "   • 匹配率: 0%")
    
    if date_stats:
        print(f"\n📅 按发布日期分布:")
        for date in sorted(date_stats.keys(), reverse=True):
            weekday = datetime.strptime(date, "%Y-%m-%d").strftime("%A")
            print(f"   {date} ({weekday}): {date_stats[date]}篇")
    
    if category_stats:
        print(f"\n📂 按类别分布 (前10):")
        sorted_categories = sorted(category_stats.items(), key=lambda x: x[1], reverse=True)
        for category, count in sorted_categories[:10]:
            print(f"   {category}: {count}篇")
    
    print(f"\n📁 数据已保存到: {output_file}")
    
    if matched_papers > 0:
        print(f"🎉 成功匹配到 {matched_papers} 篇信号源作者论文!")
        print("📋 CSV文件包含以下列：")
        print("   - ID: 论文ID")
        print("   - Title: 论文标题")
        print("   - Authors: 所有作者")
        print("   - Matched_Authors: 匹配的信号源作者")
        print("   - Published_Date: 首次发布日期")
        print("   - Updated_Date: 最后更新日期")
        print("   - Primary_Category: 主要类别")
        print("   - All_Categories: 所有类别")
        print("   - Abstract: 论文摘要")
        print("   - Abstract_URL: 论文摘要链接")
        preview_csv(output_file)
    else:
        print("⚠️ 没有匹配到信号源作者论文")
        print("   可能的原因:")
        print("   1. 该时间段确实没有信号源作者发表论文")
        print("   2. 作者名字格式不匹配")
        print("   3. 需要检查信号源作者名单")
        if total_papers > 0:
            print(f"   (共扫描了 {total_papers} 篇论文，但都不匹配)")
        else:
            print("   (未获取到任何论文数据)")
        
        # 如果没有匹配论文，删除空的CSV文件
        if os.path.exists(output_file):
            os.remove(output_file)
            print(f"   已删除空的输出文件: {output_file}")

def get_latest_papers_by_days(signal_file, days_back=1):
    """根据指定天数获取最新论文的主函数"""
    
    print("🚀 获取最新论文模式")
    print("=" * 30)
    
    # 加载信号源作者
    signal_authors = load_signal_authors(signal_file)
    if not signal_authors:
        print("⚠️ 未加载到有效的信号源作者名单")
        return None
    
    # 计算日期范围
    today = datetime.now().date()
    start_date = today - timedelta(days=days_back)

    print(f"📅 查询时间范围：{start_date} 至 {today}")
    print(f"📊 查询天数：{days_back} 天")
    
    # 批次探针：检查API是否有指定日期的论文
    print("\n🧪 执行批次探针检查...")
    top_dates = probe_api_batch_top_dates(start_date, today)
    if not should_proceed_today(top_dates, start_date):
        print("💤 指定日期范围内暂无论文，跳过本次抓取")
        return None
    
    category_counts = None
    categories = [
        "cs.AI", "cs.LG", "cs.CV", "cs.CL", "cs.NE", "cs.RO", "cs.IR",
        "cs.DC", "cs.OS", "cs.AR", "cs.PF", "cs.NI",
        "cs.SE", "cs.PL", "cs.LO", "cs.FL",
        "cs.DS", "cs.CC", "cs.DM", "cs.GT", "cs.IT",
        "cs.DB", "cs.CR", "cs.GR", "cs.MM", "cs.HC", "cs.CY", "cs.ET",
        "cs.NA", "cs.MS", "cs.SC", "cs.CE",
        "cs.OH", "cs.SY",
        # 交叉学科
        "stat.ML", "math.OC", "math.ST", "eess.IV", "eess.SP", "eess.AS",
        "econ.EM", "q-bio.QM", "physics.data-an"
    ]
    
    # 如果查询最近1天，先获取当天各类别的提交数量
    if days_back == 1:
        type = "new"
        category_counts, total_expected = get_category_submission_counts(categories, type)
        print(f"📊 预期总论文数: {total_expected}")        
        time.sleep(3.2)

    elif days_back > 1:
        type = "recent"
        category_counts, total_expected = get_category_submission_counts(categories, type)
        print(f"📊 预期总论文数: {total_expected}")
        time.sleep(3.2)
        
    return get_latest_papers(signal_authors, start_date, today, category_counts)

def main():
    """主函数"""
    print("🎯 arXiv最新论文获取工具 (使用日期范围查询)")
    print("=" * 50)
    
    # 检查信号源文件
    signal_file = "信号源信息.csv"

    if not os.path.exists(signal_file):
        print(f"❌ 找不到信号源文件: {signal_file}")
        print("请确保文件在当前目录下")
        print("信号源文件应包含 'name' 列，存储作者姓名")
        return
    
    print(f"📋 使用信号源文件: {signal_file}")
    
    ok = test_arxiv_connection()
    if not ok:
        print("❌ 无法连接到 arXiv（连通性失败）")
        return
    
    # 获取用户输入
    days_input = input("请输入要查询的天数 (默认2天): ").strip()
    try:
        days_back = int(days_input) if days_input else 2
        if days_back <= 0:
            days_back = 2
    except ValueError:
        days_back = 2
    
    print(f"📅 将查询最近 {days_back} 天的论文")
    
    # 执行获取最新论文
    result = get_latest_papers_by_days(signal_file, days_back)
    if result:
        print_results(*result)
    else:
        print("❌ 获取论文失败")

if __name__ == "__main__":
    main()