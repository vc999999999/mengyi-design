#!/usr/bin/env python3
"""Anthropic 手绘极简 · 出图自检 / self-check.

用法:
    python check_style.py 产出.html [更多.html ...]

配色是「规则」不是固定 hex —— 校验的是结构与克制,允许换色板:
必须项(缺/违反 = FAIL,退出码非 0):
  有近黑墨色(画线/文字)、有浅色卡片(明度对比)、配色克制(无鲜艳高饱和色)、
  三套字体(ZCOOL KuaiLe + Kalam + Noto Sans SC)、#sketch 手绘滤镜并被使用、含手绘 <svg>;
  扁平铁律:box-shadow / text-shadow / drop-shadow / 任意 gradient / 3D 变换 → FAIL。
软提示(WARN):中等偏高饱和色(可能偏离"低饱和"基调)。

设计意图:风格命脉是"极简扁平 + 低饱和 + 黑线浅卡",所以把这些做成硬闸门,而非锁死某三个颜色。
"""
import re, sys, colorsys

NEUTRAL_SKIP = {"FFFFFF", "FFF", "000000", "000"}  # 纯黑白不参与"鲜艳"判定


def hexnorm(h):
    h = h.upper().lstrip("#")
    return "".join(c * 2 for c in h) if len(h) == 3 else h


def hls(h):
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    l, s = colorsys.rgb_to_hls(r, g, b)[1], colorsys.rgb_to_hls(r, g, b)[2]
    return l, s


def check(path):
    src = open(path, encoding="utf-8").read()
    flat = src.replace(" ", "")
    fails, warns, oks = [], [], []

    hexes = {hexnorm(h) for h in re.findall(r"#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b", src)}
    hexes = {h for h in hexes if len(h) == 6}
    lit = {h: hls(h) for h in hexes}

    # 1 配色规则:近黑墨色 + 浅卡片 + 低饱和克制
    has_ink = any(l < 0.20 for l, _ in lit.values())
    has_light = any(l > 0.86 for l, _ in lit.values())
    (oks if has_ink else fails).append("有近黑墨色(线条/文字)" if has_ink else "缺近黑墨色 —— 线条/文字应近黑")
    (oks if has_light else fails).append("有浅色卡片(明度对比)" if has_light else "缺浅色卡片 —— 需浅色填充拉出层次")
    vivid = sorted(h for h, (l, s) in lit.items() if h not in NEUTRAL_SKIP and s > 0.50 and 0.12 < l < 0.92)
    midsat = sorted(h for h, (l, s) in lit.items() if h not in NEUTRAL_SKIP and 0.35 < s <= 0.50 and 0.12 < l < 0.92)
    if vivid:
        fails.append(f"配色不够克制:鲜艳高饱和色 {vivid} —— 本风格只用低饱和色")
    else:
        oks.append("配色克制(低饱和)")
    if midsat:
        warns.append(f"中等偏高饱和 {midsat} —— 确认是否够温和")

    # 2 三套字体
    for f in ("ZCOOL+KuaiLe", "Kalam", "Noto+Sans+SC"):
        name = f.replace("+", " ")
        (oks if (f in src or name in src) else fails).append(
            f"字体 {name}" + ("" if (f in src or name in src) else " 缺失"))

    # 3 手绘滤镜 + SVG
    for label, ok in [("#sketch 手绘滤镜", 'id="sketch"' in src and "url(#sketch)" in src),
                      ("含手绘 <svg>", "<svg" in src)]:
        (oks if ok else fails).append(label + ("" if ok else " 缺失"))

    # 4 扁平铁律(硬闸门)
    violations = [
        ("box-shadow", re.search(r"box-shadow:\s*(?!none)[^;]+", src)),
        ("text-shadow", re.search(r"text-shadow:\s*(?!none)[^;]+", src)),
        ("drop-shadow", "drop-shadow(" in flat),
        ("渐变 gradient", re.search(r"(linear|radial|conic)-gradient\(", src)),
        ("3D 变换", any(k in flat for k in ("perspective(", "rotate3d(", "translate3d(", "rotatex(", "rotatey("))),
    ]
    any_v = False
    for label, hit in violations:
        if hit:
            fails.append(f"违反扁平铁律: 出现 {label}"); any_v = True
    if not any_v:
        oks.append("扁平铁律(无阴影/渐变/3D)")

    return fails, warns, oks


def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    total = 0
    for path in sys.argv[1:]:
        fails, warns, oks = check(path)
        print(f"\n=== {path} ===")
        for o in oks:   print(f"  \033[32mPASS\033[0m {o}")
        for w in warns: print(f"  \033[33mWARN\033[0m {w}")
        for f in fails: print(f"  \033[31mFAIL\033[0m {f}")
        print("  → " + ("✅ 通过" if not fails else f"❌ {len(fails)} 项未达标")
              + (f" · {len(warns)} 条提示" if warns else ""))
        total += len(fails)
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()
