# Vibe for 奇绩 - Claude Code Skills

这是一个集成项目，包含：
1. **展示网站**：用于浏览奇绩（Miracle Plus）评测和自研的 Claude Code Skills
2. **Skills 源码**：可直接安装到 Claude Code 的 Skills 集合

## 项目结构

```
vibe-miracleplus-skills/
├── web/                    # 展示网站
│   ├── index.html          # 主页面
│   ├── styles.css          # 样式文件
│   ├── app.js              # JavaScript逻辑
│   └── data/
│       └── skills.json     # Skills数据
├── skills/                 # Skills 源码（可安装到 Claude Code）
│   ├── alpha-sight/        # 自研：论文分析工具
│   ├── person-analyzer/    # 自研：人物传记分析
│   ├── qi-signal-analysis/ # 自研：Qi Lu推文分析
│   ├── json-canvas/        # 评测：JSON Canvas支持
│   ├── literature-review/  # 评测：文献综述
│   ├── obsidian-bases/     # 评测：Obsidian数据库
│   ├── obsidian-markdown/  # 评测：Obsidian Markdown
│   ├── scientific-critical-thinking/ # 评测：科学批判性思维
│   └── scientific-writing/ # 评测：科学写作
├── reference/              # 参考文档
│   └── skills/
│       ├── built/          # 自研Skills标记文件
│       └── evaluated/      # 评测Skills标记文件
└── docs/                   # 项目文档
    └── plan/
        └── frontend-plan.md
```

## 功能特性

### 1. 响应式Hero区域
- 奇绩蓝渐变背景
- 动态统计数字（已评测、自研、总数）
- GitHub仓库链接

### 2. 多选筛选器
- 支持按领域筛选（产品开发、市场调查、品牌增长）
- 可同时选择多个领域
- 平滑的过渡动画

### 3. Skills卡片展示
- **自研Skills**：蓝色边框 + 发光效果 + "BUILT"标签
- **评测Skills**：灰色边框，hover时变蓝
- 每个卡片包含：
  - Skill名称和描述
  - 5星评分系统（SVG渐变星星）
  - 配置要求标签
  - GitHub和文档链接按钮

### 4. 右侧悬浮问卷按钮
- 固定在右侧
- 默认收起，hover展开
- 点击跳转飞书问卷

### 5. 动画效果
- 页面加载时的渐入动画
- 计数器动画
- 卡片滚动进入视口时的淡入效果
- 筛选时的平滑过渡

## 快速开始

### 对于普通用户（浏览 Skills）

访问在线展示页面：
- **GitHub Pages**: https://miracleplus-beijing.github.io/vibe-miracleplus-skills/web/

在线浏览所有奇绩评测和自研的 Claude Code Skills。

### 对于开发者（使用 Skills）

#### 方法 1：手动安装单个 Skill

```bash
# 克隆仓库
git clone https://github.com/miracleplus-beijing/vibe-miracleplus-skills.git

# 复制单个 Skill 到 Claude Code
cp -r vibe-miracleplus-skills/skills/person-analyzer ~/.claude/skills/
```

#### 方法 2：安装所有 Skills

```bash
# 克隆仓库
git clone https://github.com/miracleplus-beijing/vibe-miracleplus-skills.git

# 复制所有 Skills
cp -r vibe-miracleplus-skills/skills/* ~/.claude/skills/
```

#### 方法 3：符号链接（推荐，便于更新）

```bash
# 克隆仓库到固定位置
git clone https://github.com/miracleplus-beijing/vibe-miracleplus-skills.git ~/miracleplus-skills

# 创建符号链接
ln -s ~/miracleplus-skills/skills/* ~/.claude/skills/

# 后续更新只需 git pull
cd ~/miracleplus-skills && git pull
```

#### Windows 用户

```powershell
# 克隆仓库
git clone https://github.com/miracleplus-beijing/vibe-miracleplus-skills.git

# 复制到 Claude Code（PowerShell）
Copy-Item -Recurse vibe-miracleplus-skills\skills\* $env:USERPROFILE\.claude\skills\
```

## 网站维护说明

### 1. 更新数据

编辑 `web/data/skills.json` 文件：

```json
{
  "meta": {
    "title": "Vibe for 奇绩",
    "description": "使用Claude Code Skill助力奇绩的工作，更高质量，更长期地赋能奇绩校友成长",
    "repoUrl": "https://github.com/your-org/your-repo",  // 更新为实际仓库链接
    "surveyUrl": "https://your-feishu-survey-url"        // 更新为飞书问卷链接
  },
  "categories": [...],
  "skills": [...]
}
```

### 2. 添加新的Skill

在 `skills` 数组中添加新条目：

```json
{
  "id": "skill-id",
  "name": "Skill名称",
  "description": "一句话简介",
  "type": "built",           // 或 "evaluated"
  "rating": 5,               // 1-5的评分
  "category": "产品开发",     // 所属领域
  "githubUrl": "https://github.com/...",
  "docUrl": "https://feishu.cn/...",
  "requirements": [
    "Python 3.8+",
    "依赖项1",
    "依赖项2"
  ]
}
```

### 3. 本地预览网站

由于使用了 `fetch` API 读取JSON文件，需要通过HTTP服务器运行：

**方法1：使用Python**
```bash
cd web
python -m http.server 8000
# 访问 http://localhost:8000
```

**方法2：使用Node.js**
```bash
cd web
npx http-server -p 8000
# 访问 http://localhost:8000
```

**方法3：使用VS Code Live Server插件**
- 安装 Live Server 插件
- 右键 `web/index.html` → "Open with Live Server"

### 4. 部署到GitHub Pages

1. 将代码推送到GitHub仓库
2. 进入仓库设置 → Pages
3. 选择分支 `main`
4. 选择目录 `/web`
5. 保存后等待部署完成
6. 访问 `https://miracleplus-beijing.github.io/vibe-miracleplus-skills/web/`

## 设计规范

### 颜色
- **奇绩蓝**: `#088CFF` - 主色调
- **白色**: `#FFFFFF` - 背景色
- **灰色系**: 用于文本和边框

### 字体
- **标题**: Space Grotesk (700)
- **正文**: Inter (400, 500, 600)
- **代码**: JetBrains Mono (400)

### 动画
- 渐入渐出效果
- 卡片hover提升效果
- 计数器动画
- 平滑滚动

## 技术栈

- **HTML5**: 语义化标签
- **CSS3**:
  - CSS Variables
  - Flexbox & Grid
  - Animations & Transitions
  - Backdrop Filter (毛玻璃效果)
- **Vanilla JavaScript**:
  - Fetch API
  - Intersection Observer
  - DOM操作
  - 事件处理

## 浏览器兼容性

- Chrome/Edge 90+
- Firefox 88+
- Safari 14+

## 待完成事项

- [ ] 更新 `web/data/skills.json` 中的 GitHub 仓库链接
- [ ] 更新 `web/data/skills.json` 中的飞书问卷链接
- [ ] 为每个Skill添加飞书文档链接
- [ ] 测试所有链接是否正常工作
- [ ] 部署到GitHub Pages

## 维护说明

### 添加新的 Skill

1. 将 Skill 源码放入 `skills/` 目录
2. 在 `reference/skills/built/` 或 `evaluated/` 添加标记文件
3. 更新 `web/data/skills.json` 添加 Skill 信息
4. 提交并推送到 GitHub

### 添加新的领域分类

1. 在 `web/data/skills.json` 的 `categories` 数组中添加新分类
2. 为Skills分配新的 `category` 值

### 修改网站样式

- 主要颜色：修改 `web/styles.css` 中的 CSS Variables
- 布局：调整 `.skills-grid` 的 grid 属性
- 动画：修改 `@keyframes` 和 `transition` 属性

### 调试

- 打开浏览器开发者工具（F12）
- 查看 Console 面板的错误信息
- 检查 Network 面板确认 JSON 文件加载成功

## 联系方式

如有问题，请联系奇绩团队。

---

**Powered by Claude Code Skills** 🚀
