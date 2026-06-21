# 新增一套风格 · 脚手架

想往合集里加一套新风格,照这个来。

## 步骤

1. **拷骨架**:把本目录的 `SKILL.md` 复制到 `skills/<你的风格>/SKILL.md`,再从任意现有风格(如 `skills/anthropic-sketch`)**复制 `references/`、`assets/`、`scripts/`、`LICENSE.txt`** 过去当起点。
2. **改风格契约**:重写 `references/style-core.md`(色板规则 / 字体 / 质感代码 / 锚点 / 软性美学)——这是风格的唯一来源。
3. **改五个分支**(按需保留):
   - `assets/changtu.html`(长图)、`assets/duotu.html`(多图)、`assets/deck.html`(PPT):换配色变量、字体、装饰,保留结构与导出注释。
   - `references/illustration-prompts.md`(套版图位,固定主体)
   - `references/article-illustration.md`(文章插画,只锁风格、AI 自由构图)
   - `references/video-prompts.md`(视频,可选)
4. **改自检**:`scripts/check_style.py` 改成校验你这套风格的**规则**(配色规则、字体、质感标志、风格铁律),而不是死 hex。保留"有 FAIL 退出码非 0"。
5. **填 SKILL.md**:补好 frontmatter 的 `name` / `description`(写清"做什么 + 何时触发"),决策表指向上面的文件。
6. **登记到市场**:在 `../.claude-plugin/marketplace.json` 的某个 plugin 的 `skills` 数组里加 `"./skills/<你的风格>"`。
7. **配预览图**:在 `../previews/` 放一张 `<你的风格>.svg`,在根 `README.md` 的"包含的风格"里加一节并引用它。
8. **自检过关**:`python skills/<你的风格>/scripts/check_style.py 一个产出.html`,全 PASS 再提交。

## 一套风格的标准文件清单

```
skills/<风格>/
├── SKILL.md                      工作流入口(触发/决策表/工作流/自检/交接)
├── LICENSE.txt
├── references/
│   ├── style-core.md             风格契约(唯一来源)
│   ├── illustration-prompts.md   套版图位提示词(固定主体)
│   ├── article-illustration.md   文章插画提示词(只锁风格,自由构图)
│   └── video-prompts.md          视频提示词(可选)
├── assets/
│   ├── changtu.html · duotu.html · deck.html   长图/多图/PPT 模板
└── scripts/
    └── check_style.py            出图质量自检(规则化闸门)
```
