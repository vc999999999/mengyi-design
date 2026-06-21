# 视频版 · AI 视频提示词分支(瑞士国际 / 编辑风)

把这套编辑风做成短视频/动态。气质 = **动态排版(kinetic typography)+ 网格动画**:元素精准地"咬"进网格,干净利落,绝对扁平。产出 = 中+英提示词,交给 AI 视频工具(本分支不产 HTML,不跑 check_style.py)。

## 先决策
- **图生视频(首选)**:先用 `illustration-prompts.md` / 长图出静帧,再让其"按网格动起来",风格最稳。
- **文生视频**:从零;强调"平面 2D 动态排版、无 3D 无阴影"防漂移。

## 动作公式(精准、克制)
- 超大标题**逐行入场 / 字距收紧**;细分割线**从一端画到另一端**;
- 编号 `01 02 03` 依次**对齐弹入**;强调色块**滑入**点睛;几何形(圆/方块)**精准对位**;
- 镜头不动或极缓推;**硬切、无缓动花哨**,像翻杂志。3–6 秒,可循环。

## 图生视频(中文 · 即梦/可灵/海螺)
```
保持原图的瑞士国际编辑风、严格网格、纸白+纯黑+单一强调色、绝对扁平完全不变;动态排版方式动起来:超大标题逐行入场、细分割线从一端画到另一端、编号依次对齐弹入、强调色块利落滑入点睛、几何形精准对位;镜头几乎不动,硬切不花哨;平面 2D、无阴影无渐变无 3D;3–6 秒
```

## 图生视频(EN · Runway / Sora / Pika)
```
keep the original Swiss International editorial style, strict grid, off-white + black + single accent, fully flat and intact; animate as kinetic typography: oversized headline enters line by line, hairline rules draw across, numerals snap into alignment, an accent block slides in, geometric shapes lock to the grid; near-static camera, crisp cuts no fancy easing; flat 2D, no shadow no gradient no 3D; 3-6s
```

## 文生视频(中文)
```
瑞士国际主义动态排版动画(kinetic typography),严格网格,极致留白,超大无衬线字体,纸白背景+纯黑+单一强调色(瑞士红);把「{概念}」做成几何与文字编排:标题逐行入场、分割线展开、编号对齐弹入、强调色块滑入;平面 2D 绝对扁平、无阴影无渐变无 3D,理性克制;3–6 秒,横屏 16:9
```

## 文生视频(EN)
```
Swiss International style kinetic typography animation, strict grid, extreme negative space, oversized sans-serif type, off-white background + black + single accent (swiss red); animate {concept} as geometric + type composition: headline in line by line, rules draw across, numerals snap, accent block slides; flat 2D absolutely flat, no shadow/gradient/3D, rational restrained; 3-6s, landscape 16:9 --no shadow, gradient, 3d
```

## 小贴士
- 比例:竖屏 `9:16`;横屏 `16:9`。
- 负向词:`no 3d, no shadow, no gradient, no bouncy easing`(瑞士风要利落不软弹)。
- 强调色只点睛,别让多种颜色一起动。
