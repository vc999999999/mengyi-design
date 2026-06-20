# Layer 1 · AI 出图提示词(Anthropic 手绘极简)

满版手绘插画提示词。**风格描述固定不变,只换主体概念与"手的动作意象"。** 给用户时中英两版都给,说明出好图后替换套版里的 `<img src>`。

## 主体公式

> 把【概念】表现为:**抽象几何图表(折线图 / 圆点 / 简单形状)＋ 极简化的手部动作**,传达一个动作意象。

常见动作意象(选一个最贴的):
- **掌控趋势** → 一只手把上升折线往上拉 / 指向最高点
- **调整模型** → 手拧旋钮 / 推滑块 / 拨动节点
- **拣选/连接** → 手捏起一个圆点节点,连到另一个
- **托起** → 手掌托着一张卡片或一个图形
- **指引** → 手指点向某个数据点

## 通用 / 即梦(中文)

```
极简扁平手绘插画,Excalidraw 白板手绘风格,粗黑马克笔线条带自然不完美的手作抖动感;无任何阴影、无渐变、无 3D 立体;仅三种颜色——淡紫灰色纯色背景、纯黑色线条、米白色填充强调节点与卡片,低饱和、温和现代;主体把「{概念}」表现为 抽象几何图表(折线图/圆点)与极简化的手部动作结合,传达「{动作意象,如 掌控趋势}」,示意性强,大量留白,横构图
```

## Midjourney / SD(英文)

```
minimalist flat hand-drawn illustration, Excalidraw whiteboard style, bold black marker linework with natural imperfect hand-drawn wobble, absolutely no shadows no gradients no 3D; only three colors — pale lilac-gray solid background, pure black lines, cream off-white fills for nodes and cards, low saturation, calm and modern; depict {concept} as abstract geometric charts (line graph / dots) combined with a simplified hand gesture conveying "{action, e.g. taking control of a trend}", highly diagrammatic, lots of negative space, landscape --no shadow, gradient, 3d, photorealistic
```

## 主体示例(怎么想)

| 概念 | 画成 |
|---|---|
| 掌控增长 | 手把上升折线往右上拉,顶点一个米白圆点 |
| 调参 / 微调模型 | 手拧一个旋钮,旁边小折线随之变化 |
| 数据驱动决策 | 手指点向折线最高的数据点,其余点变暗 |
| 连接想法 | 手把两个米白圆点用一条线连起来 |
| 风险下行 | 手按住一条下滑折线,试图托住 |
| 筛选信息 | 手从一堆圆点里捏起一个 |

## 小贴士(给用户)

- 比例:长图竖屏出 `3:4`;长图横幅/幻灯片出 `16:9` 或 `3:2`。
- **务必带负向词**压住写实/阴影/3D:`no shadow, no gradient, no 3d, not photorealistic, flat`。
- 出来的图要能和套版的三色无缝接上,别让 AI 自己加别的颜色;如跑色,补:`strictly three colors: lilac-gray background, black lines, cream fills`。
- 手要极简(几笔线条 + 米白掌),别追求写实手;写实手会破坏白板手绘的统一感。
