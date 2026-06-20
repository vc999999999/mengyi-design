# 视频版 · AI 视频提示词分支

把「电子梦呓」风格做成短视频/动态。**风格描述固定不变,只换主体概念与动作。** 产出 = 一组中+英提示词,交给 AI 视频工具出片(本分支不产 HTML,故不跑 check_style.py)。

## 先决策:图生视频 还是 文生视频

- **图生视频(首选,风格最稳)**:先用 `illustration-prompts.md` 或现成长图/插画出一张静帧,再让视频工具「只加动作」。风格 100% 保真,只动起来。
- **文生视频(从零生成)**:没有静帧时用;风格可能漂移,需在提示词里强调「平涂 2D 丝网、非 3D、非写实」。

## 动作公式:把"五招"变成动作(只动 1~2 处,主角始终可爱)

| 招 | 动起来 |
|---|---|
| 变异 | 标题里那一个变异字轻微拉伸/扭动呼吸(warp 感) |
| 增殖 | 头顶小星星 / 呆萌复眼依次亮起、轻闪 |
| 越界 | 可爱主角从圆窗/边框里慢慢探头、又缩回 |
| 嫁接 | 身上的电路/网格纹流过一道光 |
| 孔洞 | 圆窗里主角眨眼、冒头打招呼 |

底噪动作(几乎都加):**主角像呼吸般缓缓起伏 + 每约 2 秒眨一次眼 + 纸张颗粒轻微浮动 + 镜头极缓推近**。幅度小而温柔,**3–6 秒无缝循环**,不要快切。

## 图生视频(中文 · 即梦/可灵/海螺)

```
保持原图的复古丝网版画质感、半调网点与配色完全不变;让画面温柔动起来:主角像呼吸般缓缓起伏,每隔约 2 秒眨一次眼,{头顶小星星依次轻闪 / 圆窗里探头打招呼 / 身上网格流过一道光},纸张颗粒轻微浮动,镜头极缓慢推近;动作幅度小、不变形,不改变角色造型与颜色;3–6 秒无缝循环
```

## 图生视频(EN · Runway / Sora / Pika)

```
keep the original vintage risograph screenprint texture, halftone dots and color palette fully intact; animate gently: the mascot bobs as if breathing, blinks about every 2s, {little stars twinkle in sequence / peeks out of the round window / a light sweeps across the body grid}, paper grain subtly drifts, very slow camera push-in; small non-distorting motion, do not change the character design or colors; seamless 3-6s loop
```

## 文生视频(中文)

```
复古丝网版画风格的可爱 2D 动画,粗黑圆润墨线,半调网点质感,有限高饱和平涂色——钴蓝、镉黄、朱红、品红,暖米色纸底,轻微纸张颗粒抖动;主体是把「{概念}」拟人化的可爱机械吉祥物/圆滚滚小机器人,大圆眼带高光、表情友好;动作:像呼吸般缓缓起伏、偶尔眨眼、{头顶小星星依次闪烁};镜头缓慢推近,无快速剪辑;定格动画/丝网海报质感,可爱讨喜,平面 2D 非 3D、非写实;3–6 秒无缝循环,竖屏 9:16
```

## 文生视频(EN)

```
vintage risograph screenprint cute 2D animation, bold rounded black ink linework, halftone dot texture, limited flat saturated palette — cobalt blue, cadmium yellow, vermilion red, hot magenta on warm cream paper, subtle paper-grain flicker; subject: {concept} as a cute chibi mechanical mascot / round robot, big round sparkly eyes, friendly; motion: gentle breathing bob, occasional blink, {little stars twinkling in sequence}; slow push-in camera, no fast cuts; stop-motion / screenprint poster feel, flat 2D not 3D, non-photoreal, adorable; seamless 3-6s loop, vertical 9:16
```

## 小贴士(给用户)

- 比例:抖音/小红书/视频号 → `9:16`;横屏/B站 → `16:9`;把提示词末尾比例改掉即可。
- 想配长图/封面用,出一段 3–6 秒循环当**动态封面/片头**最合适。
- 文生视频若出现 3D/写实漂移,补负向词:`no 3D render, no realistic, flat 2D illustration, no photoreal`。
- 始终遵守可爱契约:动作温柔、表情友好,**不要**让眨眼/复眼变得密集瘆人(见 `style-core.md`)。
- 多工具差异:**图生视频**在即梦/可灵(Kling)/海螺(Hailuo)上风格最稳;Runway Gen-3 / Sora 文生也可,但更需负向词压住写实化。
