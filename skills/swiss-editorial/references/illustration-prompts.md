# Layer 1 · AI 出图提示词(瑞士国际 / 编辑风)

填套版图位用的提示词:**固定构成公式**(几何 + 字体编排)。给用户时中英两版都给,出好图后替换套版里的图位 / `--figure` 区。

> 想"不限版式、AI 自由构图",用 `article-illustration.md`。

## 构成公式(固定)

> 网格 + 大量留白 + **超大无衬线字体 / 编号** + **几何构成(大圆 / 方块 / 对角线 / 网格点)** + 纸白底 + 黑 + **一个**强调色。把【概念】抽象成一组几何符号关系。

## 通用 / 即梦(中文)

```
瑞士国际主义平面设计海报,严格网格,极致留白,超大无衬线字体与编号,几何构成——大圆、方块、对角线、网格点;纸白色背景,纯黑,单一强调色(瑞士红),绝对扁平无阴影无渐变,理性克制,高对比;主题:把「{概念}」抽象为几何符号关系;竖构图 3:4
```

## Midjourney / SD(英文)

```
Swiss International Typographic Style graphic poster, strict grid, extreme negative space, oversized sans-serif type and numerals, geometric composition — big circle, squares, diagonals, dot grid; off-white paper background, pure black, one single accent color (swiss red), absolutely flat, no shadow no gradient, rational restrained, high contrast; subject: {concept} abstracted into geometric symbol relationships; 3:4 --no shadow, gradient, 3d, photorealistic
```

## 主体示例

| 概念 | 几何构成 |
|---|---|
| 工厂质检 | 一排方块,只有一个被红圆框住 |
| 对照实验 | 竖线一分为二,左右各一圆,一黑一红 |
| 流程闭环 | 四点用直角折线连成回路,起点红 |
| 层级 | 大中小三个同心圆,最小的红 |

## 小贴士
- 比例随用途(`3:4` / `16:9` / `1:1`)。
- 务必带负向词:`no shadow, no gradient, no 3d`;并强调 `only black + off-white + one accent`。
- 换强调色就把 "swiss red" 换成你的 `--accent` 对应色。
