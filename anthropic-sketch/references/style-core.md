# 风格契约 · style-core（Anthropic 手绘极简）

所有产物共享的固定内核。改套版时**照抄这里的代码片段**,别自创。这套风格的灵魂 = 极简扁平 + 粗黑手绘线 + 三色克制 + 几何符号与手部动作结合。

## 1 · 色板(规则固定,具体色可换)

风格锁的是**结构与克制**,不是某三个 hex。每套配色 = **3 个角色**:

1. **背景** = 一个柔和、低饱和的浅/中浅色(撑起整页)
2. **线条/文字** = 近黑墨色(画所有手绘线与正文,可降透明度做次级文字)
3. **卡片/节点** = 一个更浅的浅色(填卡片、数据点、强调块),与背景拉出层次

**铁规**:三色都**低饱和**(不刺眼、不鲜艳)、整套**≤3 色**、必须有「近黑墨色」和「浅卡片色」这组明度对比。次级文字用墨色降透明度(如 `rgba(17,17,17,.6)`),不另造灰色。**不要鲜艳色**;确需一个品牌强调色,只点一处且仍偏低饱和。

**默认预设(紫灰,模板自带):**
```
背景 #D6D2E1   墨黑 #111111   卡片 #F3EFE4
```
**可直接换用的其他预设**(都满足铁规,改 `:root` 三个变量即可):
```
暖米   背景 #EDE7DA   墨黑 #14110E   卡片 #FBF7EE
淡蓝   背景 #DCE3EE   墨黑 #11151B   卡片 #F4F7FB
薄荷   背景 #DCE7E0   墨黑 #101512   卡片 #F2F8F4
裸粉   背景 #ECE0DD   墨黑 #1A1210   卡片 #FBF1EE
```
要自配:挑一个低饱和浅色当背景,配近黑墨色,卡片取比背景更浅一档的同/邻色系即可。自检验证的是「低饱和 + 黑线 + 浅卡片」这套规则,不是具体 hex。

## 2 · 字体

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Kalam:wght@300;400;700&family=ZCOOL+KuaiLe&family=Noto+Sans+SC:wght@400;500;700&display=swap" rel="stylesheet">
```
- 中文标题/标签/手写感文字 = `'ZCOOL KuaiLe'`(马克笔感圆体)。
- 英文/数字/手写注释 = `'Kalam'`(手绘马克笔)。
- 正文长段落 = `'Noto Sans SC'` 400/500(保证可读;手绘字只用在标题与标注,长正文别用,否则难读)。

## 3 · 手绘质感(照抄,别删)

唯一滤镜 `#sketch`:给线条/图形加"手抖"不完美感。**scale 要小(1.5~3)**,大了会糊。

```html
<!-- 放 body 顶部隐藏 svg 的 defs 里 -->
<filter id="sketch" x="-5%" y="-5%" width="110%" height="110%">
  <feTurbulence type="fractalNoise" baseFrequency="0.018" numOctaves="2" seed="7" result="n"/>
  <feDisplacementMap in="SourceGraphic" in2="n" scale="2.4"/>
</filter>
```
- **插画/图表/装饰线**:画在 `<svg>` 里,整组套 `filter:url(#sketch)`。线条 `stroke:#111; stroke-width:3~5; stroke-linecap:round; stroke-linejoin:round; fill:none`(需要填充的节点/卡片 `fill:#F3EFE4`)。
- **HTML 卡片**:不套滤镜(否则文字也抖、难读),改用**不均匀圆角 + 极微旋转**模拟手作:
  ```css
  .card{background:#F3EFE4;border:2.5px solid #111;
    border-radius:16px 10px 18px 9px / 9px 18px 10px 16px;}
  .card:nth-child(even){transform:rotate(-.5deg)} .card:nth-child(odd){transform:rotate(.4deg)}
  ```

## 4 · 扁平铁律(本风格的硬边界)

**没有阴影、没有渐变、没有 3D。** 全部纯色平涂。
- 禁止 `box-shadow`(非 none)、`text-shadow`、`drop-shadow`、任何 `*-gradient()`、`perspective`/3D 变换。
- 背景永远是 `#D6D2E1` 纯色,不加纹理/颗粒/图案(与"电子梦呓"那套不同,这套要绝对干净)。
- 自检脚本会拦这些,见 SKILL.md 第 3 步。

## 5 · 标注语言(这套风格的"记忆点")

用手绘批注传达重点,而不是加粗变色:
- **圈词**:给关键词套一个手绘椭圆(SVG `<ellipse>` 不闭合更像手画),`filter:url(#sketch)`。
- **下划波浪线 / 直线**:标题或词下方一道手绘线。
- **箭头**:卡片之间用手绘箭头连(指示流程/因果)。
- **圆点节点**:米白填充、黑边的小圆,做"数据点 / 步骤点"。

片段:
```html
<!-- 圈一个词 -->
<svg class="anno" viewBox="0 0 200 70"><g filter="url(#sketch)">
  <path d="M18 40 C18 14 182 10 188 36 C192 60 30 66 14 42" fill="none" stroke="#111" stroke-width="3.5" stroke-linecap="round"/>
</g></svg>
<!-- 手绘箭头 -->
<svg class="arr" viewBox="0 0 120 40"><g filter="url(#sketch)" fill="none" stroke="#111" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round">
  <path d="M8 20 H104"/><path d="M90 8 L106 20 L90 32"/></g></svg>
```

## 6 · 主体公式:几何 + 手

每个版面有**一个**核心手绘插画:**抽象几何图表(折线图 / 圆点 / 简单形状)＋ 极简化的手部动作**,传达一个动作意象(掌控趋势 / 调整旋钮 / 拣选节点 / 托起卡片)。手要极简(米白掌 + 黑线手指,几笔即可),不追求写实。模板已内置一个"手调整上升折线"的范例,可改造。

## 7 · 软性美学指导(理解原因,灵活执行)

- **留白是主角**:紫灰大面积留空,内容稀疏地放。原因:极简风的高级感来自呼吸感,塞满就垮。
- **线条要敢粗**:主体轮廓 3~5px,比你以为的更粗才有"马克笔"味。
- **不完美才对**:圆角不要四角统一、线条不要绝对直、卡片轻微歪——这是"手作痕迹",不是 bug。
- **一图一意**:一个版面只讲一个核心意象,别堆多个插画。
