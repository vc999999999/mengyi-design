# Layer 1 · AI 出图提示词公式

满版主体的提示词。**风格描述固定不变,只换主体概念。** 给用户时,中英两版都给,并说明出好图后替换套版 HTML 里的 `<img src>`。

## 主体公式（可爱优先 · 适合社交媒体）

> 把【概念】**拟人化**为：可爱机械吉祥物 / 圆滚滚机械小兽 / Q 版机械精灵（三选一,看哪个最贴）。

形象基调:**软萌、友好、像贴纸/玩偶**。大眼睛、圆脑袋、胖乎乎的身体、表情可爱。机械元素是「点缀的小齿轮/天线/接缝」,不是冰冷神祇。

- 抽象/系统类概念 → **圆头机械吉祥物**(像桌面机器人玩偶,有小天线、友好笑脸)
- 力量/速度/数据类 → **圆滚滚机械小兽**(短腿、大眼、Q 版,绝不凶)
- 内部/感知类 → **机械小精灵**(漂浮的小圆球生物,带光点眼睛)

> ⚠ 避免诡异:**不要**多眼密集凝视、獠牙、内脏、骷髅、血肉、空洞黑眼。要的是「可爱里带一点点机械怪趣」,不是恐怖。眼睛可以多,但要圆、要亮、要呆萌,不要瘆人。

## 通用 / 即梦（中文）

```
复古丝网版画风格的可爱插画,粗黑墨线勾边但线条圆润,半调网点上色,有限高饱和平涂色——钴蓝、镉黄、朱红、品红,暖米色纸底;主体是把「{概念}」拟人化的可爱机械吉祥物/圆滚滚机械小兽,大而圆的亮眼睛、胖乎乎圆身体、软萌友好的表情,贴纸/吉祥物式构图,1970 年代复古绘本质感,可爱讨喜,高对比,横构图 2:1
```

## Midjourney / SD（英文）

```
vintage risograph screenprint illustration, bold but rounded black ink linework, soft halftone dot shading, limited flat saturated palette — cobalt blue, cadmium yellow, vermilion red, hot magenta on warm cream paper; subject: {concept} as a cute chibi mechanical mascot / round chubby robot creature, big round sparkly eyes, plump rounded body, kawaii friendly smile, sticker / mascot composition, retro 1970s picture-book charm, adorable, high contrast --ar 2:1 --style raw
```

## 主体示例（怎么往可爱想）

| 概念 | 可爱拟人化主体 |
|---|---|
| 注意力机制 | 戴一圈小望远镜、瞪着圆眼睛的胖机械小章鱼 |
| Transformer | 抱成一团、节节相扣的呆萌机械毛毛虫 |
| 幻觉 Hallucination | 头顶冒星星泡泡、看花眼的迷糊机器人 |
| 算力 / GPU | 圆滚滚冒小汗珠、努力转齿轮的小钢炉宠物 |
| 数据隐私 | 抱着小锁、护着发光小心心的盾牌机器人 |
| 世界杯竞彩参考 | 抱着足球水晶球、歪头预言的占卜师小机器人 |
| RAG 检索增强 | 一堆小手翻绘本的章鱼图书管理员(友好版) |
| 过拟合 | 把自己用线团缠成毛球的呆萌小机器人 |

## 出图小贴士（给用户）

- 想要满版海报底图 → 用 `3:4` 或 `4:5`;想要幻灯片满铺 / 长图图框 → 用 `2:1` 或 `3:2`,提示词把比例那句改掉即可。
- 出图后图色会和套版色板天然接近(钴蓝/镉黄/朱红/品红 + 米底),图嵌进版面不违和——别让图跑出这套色。
- 想要「孔洞」效果:出图时主体居中、四周留点米底空,方便套版用色块从边缘围住、只露中间的可爱主角。
- 如果出来的图还是偏诡异,在提示词里再加重:`软萌、圆润、表情友好、像玩偶、kawaii、no creepy、no scary`。
