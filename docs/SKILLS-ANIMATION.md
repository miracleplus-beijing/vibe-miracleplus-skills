# Skills展示动画实现文档

## 实现时间
2026-01-19

## 功能概述

在Hero区域的统计徽章下方添加了一个Claude Code风格的动画展示区域，循环展示所有自研和评测的Skills名称。

---

## 动画效果

### 1. 左侧Spinner（花朵动画）
- **字符序列**: `·` → `✻` → `✽` → `✶` → `✳` → `✢`
- **切换速度**: 每100ms切换一次
- **视觉效果**: 带有脉冲动画（缩放+透明度变化）
- **颜色**: 纯白色

### 2. 右侧打字机效果
- **打字速度**: 每个字符50-80ms随机延迟（模拟真实打字）
- **显示时长**: 完整显示后暂停1.5秒
- **擦除速度**: 每个字符30ms（快速倒序删除）
- **切换间隔**: 擦除后暂停300ms再显示下一个

### 3. 光标闪烁
- **字符**: `|` (竖线)
- **闪烁频率**: 1秒一次
- **颜色**: 纯白色

---

## 展示内容

### 自研Skills（3个）
1. Alpha-Sight
2. Person-Analyzer
3. Qi-Signal-Analysis

**视觉特征**:
- 字体加粗（font-weight: 700）
- 纯白色
- 带有白色发光效果（text-shadow）

### 评测Skills（6个）
4. JSON-Canvas
5. Literature-Review
6. Obsidian-Bases
7. Obsidian-Markdown
8. Scientific-Critical-Thinking
9. Scientific-Writing

**视觉特征**:
- 常规字重（font-weight: 500）
- 85%透明度的白色
- 无发光效果

---

## 视觉设计

### 容器样式
```css
- 背景: rgba(255, 255, 255, 0.15) - 半透明白色
- 毛玻璃效果: backdrop-filter: blur(20px)
- 边框: 1px solid rgba(255, 255, 255, 0.25)
- 圆角: 12px
- 阴影: 0 8px 32px rgba(0, 0, 0, 0.1)
- 最小宽度: 400px (移动端: 320px)
- 内边距: 1.25rem 2.5rem
```

### 布局
- 位置: Hero区域统计徽章下方，margin-top: 3rem
- 对齐: 水平居中
- 内部布局: Flexbox，gap: 1rem
- 元素顺序: Spinner | Text | Cursor

### 字体
- 使用JetBrains Mono（等宽字体）
- 字号: 1.1rem (移动端: 0.95rem)
- 字间距: 0.02em

---

## 技术实现

### HTML结构
```html
<div class="skills-showcase">
  <div class="skills-showcase-content">
    <span class="skills-spinner" id="skillsSpinner">·</span>
    <span class="skills-text" id="skillsText"></span>
    <span class="skills-cursor">|</span>
  </div>
</div>
```

### CSS关键点
1. **Spinner脉冲动画**
   ```css
   @keyframes spinnerPulse {
     0%, 100% { opacity: 1; transform: scale(1); }
     50% { opacity: 0.7; transform: scale(1.1); }
   }
   ```

2. **光标闪烁动画**
   ```css
   @keyframes cursorBlink {
     0%, 50% { opacity: 1; }
     51%, 100% { opacity: 0; }
   }
   ```

3. **容器淡入动画**
   - 使用现有的fadeInUp动画
   - 延迟0.8s开始（在统计徽章之后）

### JavaScript逻辑

#### 1. Spinner动画
```javascript
setInterval(() => {
  spinner.textContent = spinnerFrames[spinnerIndex];
  spinnerIndex = (spinnerIndex + 1) % spinnerFrames.length;
}, 100);
```

#### 2. 打字机效果
```javascript
async function typewriterEffect(text, type) {
  // 设置样式类
  textElement.className = `skills-text ${type}`;

  // 逐字符显示
  for (let i = 0; i < text.length; i++) {
    textElement.textContent += text[i];
    await sleep(randomBetween(50, 80));
  }

  // 暂停
  await sleep(1500);

  // 逐字符删除
  for (let i = text.length; i > 0; i--) {
    textElement.textContent = text.substring(0, i - 1);
    await sleep(30);
  }

  // 短暂暂停
  await sleep(300);
}
```

#### 3. 主循环
```javascript
async function animationLoop() {
  while (true) {
    const skill = skills[currentSkillIndex];
    await typewriterEffect(skill.name, skill.type);
    currentSkillIndex = (currentSkillIndex + 1) % skills.length;
  }
}
```

---

## 性能优化

1. **单一定时器**: Spinner使用一个setInterval，避免多个定时器
2. **Async/Await**: 清晰的异步流程控制
3. **动画守卫**: `isAnimating`标志防止重叠动画
4. **CSS动画**: 光标和脉冲使用CSS动画（GPU加速）
5. **最小DOM操作**: 只更新textContent，不改变DOM结构
6. **延迟启动**: 页面加载1秒后才开始动画

---

## 响应式设计

### 移动端适配（<768px）
```css
.skills-showcase-content {
  min-width: 320px;
  padding: 1rem 1.5rem;
}

.skills-text {
  font-size: 0.95rem;
  min-width: 220px;
}

.skills-spinner {
  font-size: 1.25rem;
}
```

---

## 文件修改

### 1. index.html
- 在`.stats`后添加`.skills-showcase`容器
- 位置: 第54-61行

### 2. styles.css
- 添加Skills Showcase Animation样式
- 位置: 第205-298行
- 更新响应式样式: 第896-908行

### 3. app.js
- 添加`initSkillsShowcase()`函数
- 位置: 第683-770行
- 在DOMContentLoaded中调用: 第166行

---

## 使用说明

### 修改Skills列表
在`app.js`的`initSkillsShowcase()`函数中修改`skills`数组：

```javascript
const skills = [
  { name: 'Skill名称', type: 'built' },      // 自研
  { name: 'Skill名称', type: 'evaluated' }   // 评测
];
```

### 调整动画速度
```javascript
// Spinner速度
setInterval(() => { ... }, 100);  // 改变100

// 打字速度
await sleep(randomBetween(50, 80));  // 改变50-80

// 显示时长
await sleep(1500);  // 改变1500

// 擦除速度
await sleep(30);  // 改变30
```

### 修改视觉样式
```css
/* 容器透明度 */
.skills-showcase-content {
  background: rgba(255, 255, 255, 0.15);  /* 调整0.15 */
  backdrop-filter: blur(20px);  /* 调整20px */
}

/* 自研Skills发光效果 */
.skills-text.built {
  text-shadow: 0 0 20px rgba(255, 255, 255, 0.5);  /* 调整参数 */
}
```

---

## 特色亮点

1. **Claude Code风格**: 完美复刻Claude Code CLI的花朵spinner
2. **真实打字感**: 随机延迟模拟真实打字节奏
3. **视觉层次**: 自研Skills加粗+发光，评测Skills常规显示
4. **毛玻璃美学**: 半透明背景+模糊效果，现代感十足
5. **流畅动画**: 所有过渡都经过精心调校
6. **性能优化**: 高效的动画实现，不影响页面性能

---

## 浏览器兼容性

- **Chrome/Edge**: 完全支持
- **Firefox**: 完全支持
- **Safari**: 完全支持（backdrop-filter需要15.4+）
- **移动浏览器**: 支持

---

## 测试建议

- [ ] Spinner正常循环旋转
- [ ] 打字机效果流畅
- [ ] 自研Skills显示加粗+发光
- [ ] 评测Skills显示常规样式
- [ ] 光标正常闪烁
- [ ] 循环播放所有9个Skills
- [ ] 移动端显示正常
- [ ] 动画不卡顿

---

## 效果预览

打开`index.html`，在Hero区域的统计徽章下方，你会看到：

```
[·] Alpha-Sight|
```

Spinner会持续旋转，文字会逐字符打出，然后暂停，再逐字符删除，循环展示所有Skills。

🎉 动画实现完成！
