# 文章插画分支 · 只给风格,构图交给内容 + AI

**用途**:给一篇文章 / 一段内容配插画。**不套任何模板、不定版式、不固定主体**——只把「Anthropic 手绘极简」的风格 DNA 注入提示词,画面画什么、怎么构图,由**文章内容 + AI 自由发挥**。产出 = 一条可直接出图的提示词(中 + 英)。

> 和 `illustration-prompts.md` 的区别:那份有固定主体公式(几何图表 + 手)、用来填套版图位;**本份只锁风格、不锁构图**,适合文章配图 / 题图 / 段落插画,让 AI 自己根据内容想画面。

## 怎么用(三步)

1. **读内容,提炼一个画面意象**:用一句话,从文章本身长出一个场景/概念图(别强加固定形象)。可多想 2~3 个备选,让 AI 各出一张挑。
2. **套提示词**:`[风格 DNA(固定)] + 画面:{你的画面意象(自由)} + [比例 / 负向词]`。
3. **出图**:交给即梦 / MJ / SD;不满意就只换「画面意象」那一句,风格 DNA 不动。

## 风格 DNA（固定不变,照抄）

极简扁平手绘、Excalidraw 白板马克笔风、粗黑线条带自然手抖不完美感、极简化的几何图形语言、三色克制(淡紫灰底 / 纯黑线 / 米白填充)、低饱和、大量留白、平面 2D、**无阴影、无渐变、无 3D**、非写实。

## 提示词模板

**中文 · 通用 / 即梦**
```
极简扁平手绘插画,Excalidraw 白板马克笔风格,粗黑线条带自然手抖,极简几何图形语言;仅三色——淡紫灰纯色背景、纯黑线条、米白填充,低饱和,大量留白;无阴影无渐变无 3D,平面 2D 非写实;画面:{从文章提炼的意象,自由构图};{比例,如 横 16:9 / 竖 3:4}
```

**EN · Midjourney / SD**
```
minimalist flat hand-drawn illustration, Excalidraw whiteboard marker style, bold black lines with natural hand-drawn wobble, simplified geometric visual language; only three colors — pale lilac-gray solid background, pure black lines, cream off-white fills, low saturation, lots of negative space; absolutely no shadow no gradient no 3D, flat 2D, non-photoreal; scene: {free composition drawn from the article}; {ratio} --no shadow, gradient, 3d, photorealistic
```

## 示例(文章 → 自由画面)

| 文章主题 | 一句画面意象(交给 AI) |
|---|---|
| 第一性原理思考 | 一个大问号被拆成几块基础几何形,一只手在重新拼装 |
| 复利的力量 | 一颗小种子和一棵由圆点累积长成的大树并排 |
| 决策疲劳 | 一个人面前一排开关,有的已拨下、手悬在最后一个上 |
| 系统 vs 目标 | 一条循环箭头的回路 对比 一个孤零零的终点旗 |

注意:同一篇可给 2~3 句不同意象,让 AI 各出一版。

## 唯一约束(扁平铁律)

**无阴影、无渐变、无 3D、非写实**,保持三色克制与手绘线。除此之外,构图、主体、视角、繁简全部交给内容和 AI。

## 小贴士

- 比例随用途:公众号题图 `16:9` 或 `2:1`;竖屏 `3:4`;方图 `1:1`。
- 跑色就补:`严格只用 淡紫灰背景 / 纯黑线 / 米白填充 三种颜色`。换了配色预设(见 `style-core.md`)就把这三色换成对应值。
- 出来太写实/带阴影,加重负向词:`no shadow, no gradient, no 3d, not photorealistic, flat 2d line art`。
