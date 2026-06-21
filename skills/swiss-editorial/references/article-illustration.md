# 文章插画分支 · 只给风格,构图交给内容 + AI

**用途**:给一篇文章 / 一段内容配图。**不套任何模板、不定版式**——只把「瑞士国际 / 编辑风」的风格 DNA 注入提示词,画面由**文章内容 + AI 自由构图**。产出 = 一条提示词(中 + 英)。

> 与 `illustration-prompts.md` 区别:那份是固定构成、填套版图位;本份只锁风格、自由构图,适合文章题图 / 段落配图。

## 怎么用(三步)

1. **读内容,提炼一个画面意象**:一句话,从文章长出一个**几何 / 字体构成的概念图**(瑞士风不画写实插画,用几何符号传达观念)。
2. **套提示词**:`[风格 DNA(固定)] + 画面:{你的意象(自由)} + [比例 / 负向词]`。
3. **出图**:交给即梦 / MJ / SD;不满意只换「画面」那句。

## 风格 DNA(固定,照抄)

瑞士国际主义平面设计 / 编辑海报、严格网格、极致留白、超大无衬线字体编排、几何构成(大圆 / 方块 / 对角线 / 网格点)、纸白底 + 纯黑 + **单一强调色**、绝对扁平(无阴影、无渐变、无 3D)、理性克制、高对比。

## 提示词模板

**中文 · 通用 / 即梦**
```
瑞士国际主义风格的极简编辑海报,严格网格排版,大量留白,超大无衬线字体,几何构成(大圆/方块/对角线);纸白色背景 + 纯黑 + 单一强调色(瑞士红),绝对扁平、无阴影无渐变无 3D,理性克制高对比;画面:{从文章提炼的几何/概念意象,自由构图};{比例,如 横 16:9 / 竖 3:4}
```

**EN · Midjourney / SD**
```
Swiss International Typographic Style minimalist editorial poster, strict grid layout, generous negative space, oversized sans-serif typography, geometric composition (big circle / squares / diagonals); off-white paper background + pure black + a single accent color (swiss red), absolutely flat, no shadow no gradient no 3D, rational and restrained, high contrast; scene: {free geometric/conceptual composition drawn from the article}; {ratio} --no shadow, gradient, 3d, photorealistic
```

## 示例(文章 → 自由意象)

| 文章主题 | 一句画面意象(交给 AI) |
|---|---|
| 不是模板是工厂 | 一个被红圈圈住的方块,旁边一排灰色相同方块——独一份 vs 批量 |
| baseline 对照 | 画面正中一条竖线,把版面分成黑 / 白两半,各一个圆点对照 |
| 触发入口 description | 一个巨大的红色箭头从边缘指向一个小方块入口 |
| 信息流程化 | 三个圆点用直线串成一条流程,末端一个红点 |
| 秩序与噪音 | 整齐网格点阵中,一个红点偏离格线 |

## 唯一约束(扁平 + 单色)

**无阴影、无渐变、无 3D;只用 纸白 + 黑 + 一个强调色**(瑞士风定义)。除此之外,构成、留白比例、字体大小全交给内容和 AI。

## 小贴士

- 比例:题图 `16:9` / `2:1`;竖屏 `3:4`;方图 `1:1`。
- 跑色就补:`only off-white, black and one single accent color`。换了 `--accent` 预设就把强调色换成对应色。
- 想更"海报感",加 `large bold typographic composition, lots of empty space`。
