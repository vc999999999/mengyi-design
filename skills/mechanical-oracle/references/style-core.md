# 风格契约 · style-core

所有产物(长图/多图/PPT/插图)共享的固定内核。改套版时**照抄这里的代码片段**,不要自创。这是「同一个账号」视觉统一的唯一来源。

## 1 · 色板(默认即品牌,可整套换色)

锁的是**角色结构与丝网冲击力**:**墨黑底 + 暖纸底 + 4 个高饱和强调色**。默认六色就是「电子梦呓」品牌识别,**日常用默认**;做子系列/节日/特别企划时可整套换,但必须守规则。

**默认预设(品牌经典):**
```
墨黑 #100E0C  纸白 #ECE0C4  电蓝 #1B46D4  镉黄 #F5C20B  朱红 #E5341D  品红 #E8356F
```
**铁规(换色也要满足):** ① 有近黑墨色(底/线) ② 有暖浅纸底 ③ 至少 3 个**高饱和**强调色(丝网风的命脉就是高饱和冲击力,别用灰扑扑的色)。改 `:root` 的 `--ink/--paper/--blue/--yellow/--red/--magenta` 即可换。

**可直接换用的其他预设**(都满足铁规):
```
霓虹夜  墨黑#0E0E18 纸白#ECE6D6 电蓝#2348E0 镉黄#F7D108 朱红#FF4D1A 品红#FF3D8B
薄荷糖  墨黑#12130E 纸白#EFE9D6 电蓝#1FA8C4 镉黄#F2C20B 朱红#E5482A 品红#E85FA0
暮山红  墨黑#1A120C 纸白#F2E7CE 电蓝#2E6E8E 镉黄#E8A60B 朱红#D8401D 品红#D85A7A
```

许可的中性衍生色(低饱和,仅用于次级文字/网格,别另造):
`#7a6f59`(暗金小字) `#cdbf9f`(纸底次级字) `#3a342a`(深米正文) `#1f1b16`(深底网格) `#9a8f78`(页脚字)

分类语义色(角色固定,色相随预设走):**电蓝=科普 / 朱红=测评 / 品红=教程**。镉黄不作栏目语义,固定作「高亮/变异/按钮」。内容不在三类内时,选最近的一类,别造第四种语义。

## 2 · 字体

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;700;900&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
```
- 标题/大字 = `'Noto Sans SC'` **900**;正文 = 400/700,行高 1.7~1.85。
- 数字/英文标签/期号/角标 = `'Space Mono'`,`letter-spacing:.1em~.18em`,多用大写。英文一律走 Space Mono。

## 3 · 三样质感(照抄,别删)

```html
<!-- SVG 滤镜:放 body 顶部隐藏 svg 的 defs 里 -->
<filter id="warp"><feTurbulence type="fractalNoise" baseFrequency="0.012 0.02" numOctaves="2" seed="7" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="8"/></filter>
<filter id="ooze"><feTurbulence type="fractalNoise" baseFrequency="0.02 0.04" numOctaves="3" seed="11" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="9"/></filter>
<pattern id="halftone" width="7" height="7" patternUnits="userSpaceOnUse"><circle cx="3.5" cy="3.5" r="1.5" fill="#100E0C"/></pattern>
```
```css
/* 纸张颗粒:全屏遮罩 */
.grain{position:absolute;inset:0;z-index:99;pointer-events:none;mix-blend-mode:multiply;opacity:.13;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='140' height='140'%3E%3Cfilter id='g'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='2'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23g)'/%3E%3C/svg%3E");}
/* 半调网点:叠在色块上做层次 */
.dots{background-image:radial-gradient(#100E0C 1.1px,transparent 1.4px);background-size:6px 6px;}
```
`warp` 用于标题/图框(微扭,scale 别超 ~12 否则糊);`ooze` 用于可爱装饰;`halftone`/`.dots` 给色块加层次(想要更暗就把 `background-size` 调小)。颗粒 opacity 控 0.10~0.16。

## 4 · 四个固定锚点(每个版面/每张图都要有)

1. **刊头条** — `电子梦呓 / DIGITAL REVERIE` + 期号/分类(Space Mono 小字,色 `#7a6f59`)。
2. **分类色标** — 一个小色块标签(语义色,见上),让读者一眼分栏目。
3. **变异标题带** — 900 大标题,**只让一个字变异**(`transform:scaleY(1.4)` 拉长 / 换镉黄或品红 / 套 `filter:url(#warp)`)。
4. **孔洞/圆窗 = 插画位** — 可爱主角从圆窗/开口探出(粗黑边图框,圆角更萌),或整版满铺,二选一。

## 5 · 可爱形象契约(社交媒体导向)

主角永远:**大圆眼带高光、圆胖身体、表情友好、像玩偶**;机械只是点缀(小天线/齿轮/接缝/小星星)。

**禁止瘆人元素**(出图提示词与 SVG 装饰都遵守):密集多眼凝视、獠牙、内脏血肉、骷髅、空洞黑眼、扭曲到看不清脸。可爱里带一点机械小怪趣即可。

## 6 · 软性美学指导(理解原因,灵活执行)

- **一处变异原则**:每个版面只在标题/装饰动 1~2 处「怪趣」,其余规整。原因:满版都怪 = 视觉噪声,读者抓不到重点;一处变异才是「记忆点」。正文/数据/说明**始终规整可读**——这是阅读体验的底线,不是风格的牺牲品。
- **留白敢留**:节奏 = 大留白 + 突然的高饱和色块 + 一处怪趣。塞满会丢掉丝网海报的呼吸感。
- 不用柔和阴影、不用玻璃拟态、圆角克制(0~小圆角)。这是印刷品气质,不是 SaaS 界面。
