# 视频版 · AI 视频提示词分支（Anthropic 手绘极简）

把这套白板手绘风做成短视频/动态。**风格描述固定不变,只换主体概念与动作。** 产出 = 一组中+英提示词,交给 AI 视频工具出片(本分支不产 HTML,不跑 check_style.py)。

核心气质:像**白板讲解动画(whiteboard explainer)**——线条像被一支马克笔现场画出来,平面 2D、三色克制、无阴影无 3D。

## 先决策:图生视频 还是 文生视频

- **图生视频(首选,风格最稳)**:先用 `illustration-prompts.md` 或现成长图/插画出一张静帧,再让视频工具「按手绘逻辑动起来」。三色与线条 100% 保真。
- **文生视频(从零)**:没静帧时用;务必强调「平面 2D 白板手绘、无阴影无 3D、三色」防漂移。

## 动作公式:把手绘元素变成动作(克制、温和,一图一动作)

| 元素 | 动起来 |
|---|---|
| 线条/折线 | **自我描画(draw-on)**:像马克笔从头画到尾 |
| 圆点节点 | 依次**弹出/点上**,带一点点回弹 |
| 手 | 伸入画面,把折线**往上拉** / 拨节点 / 点向数据点 |
| 批注(圈/下划线) | 最后**手绘浮现**,圈住关键词 |
| 整体 | 线条保持极轻微的手抖(boil/抖动),镜头极缓推近 |

节奏:先描线 → 圆点弹出 → 手介入动作 → 批注收尾,**3–6 秒**,可循环。

## 图生视频(中文 · 即梦/可灵/海螺)

```
保持原图的白板手绘极简风、三色(淡紫灰底/纯黑线/米白卡)与扁平质感完全不变;像白板讲解动画那样动起来:黑色线条像马克笔被现场描画出来,圆点节点依次轻轻弹出,一只简笔的手伸入把折线往上拉,最后手绘圈出关键词;线条带极轻微手抖,镜头极缓推近;平面 2D、无阴影无 3D、不写实;3–6 秒,动作温和克制
```

## 图生视频(EN · Runway / Sora / Pika）

```
keep the original whiteboard hand-drawn minimalist style, three colors (lilac-gray bg / pure black lines / cream cards) and flat look fully intact; animate like a whiteboard explainer: black lines draw themselves on as if by a marker, dot-nodes pop in one by one, a simple line-drawn hand reaches in and pulls the line graph upward, finally a hand-drawn circle annotates the keyword; lines keep a subtle hand-drawn boil, very slow camera push-in; flat 2D, no shadow no 3D, non-photoreal; 3-6s, calm restrained motion
```

## 文生视频(中文)

```
极简白板手绘讲解动画,Excalidraw 风格,粗黑马克笔线条带自然手抖;仅三色——淡紫灰纯色背景、纯黑线条、米白填充;把「{概念}」表现为 抽象几何图表(折线/圆点)＋ 简笔手部动作,传达「{动作意象,如 掌控趋势}」;线条自我描画、圆点依次弹出、手把折线往上拉;平面 2D、绝无阴影/渐变/3D、不写实,大量留白;3–6 秒,横屏 16:9
```

## 文生视频(EN)

```
minimalist whiteboard hand-drawn explainer animation, Excalidraw style, bold black marker lines with natural hand-drawn boil; only three colors — pale lilac-gray solid background, pure black lines, cream fills; depict {concept} as abstract geometric charts (line graph / dots) plus a simple line-drawn hand gesture conveying "{action}"; lines draw themselves on, dots pop in, a hand pulls the line graph up; flat 2D, absolutely no shadow/gradient/3D, non-photoreal, lots of negative space; 3-6s, landscape 16:9 --no shadow, 3d, photorealistic
```

## 小贴士(给用户)

- 比例:竖屏(抖音/小红书)`9:16`;横屏/演示 `16:9`。改提示词末尾比例即可。
- **务必带负向词**压住 3D/阴影/写实:`no shadow, no gradient, no 3d, not photorealistic, flat 2d`。
- 保持三色:跑色时补 `strictly three colors: lilac-gray bg, black lines, cream fills`(换了配色预设就换成对应三色)。
- 动作要少而稳:白板风的高级感来自"克制",别加炫光、粒子、快切。
- 想要"线条自己画出来"最稳的做法:用 draw-on / handwriting reveal 类工具或模板,而非纯生成。
