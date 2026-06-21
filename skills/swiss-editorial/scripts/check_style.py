#!/usr/bin/env python3
"""杂志编辑 / 瑞士国际 · 出图自检 / self-check.

用法:
    python check_style.py 产出.html [更多.html ...]

锁的是"理性克制的国际主义编排",允许换强调色:
必须项(缺/违反 = FAIL,退出码非 0):
  有浅纸底、有近黑文字、强调色至多一个(瑞士风定义)、三套字体(Archivo + Inter + Noto Sans SC)、
  用了网格(display:grid)、有细分割线(border-top);
  扁平铁律:box-shadow / text-shadow / 任意 gradient / 3D 变换 → FAIL。
软提示(WARN):完全没有强调色(纯黑白也行,但确认是否刻意)。
"""
import re, sys, colorsys

NEUTRAL_SKIP = {"FFFFFF", "FFF", "000000", "000"}


def hexnorm(h):
    h = h.upper().lstrip("#")
    return "".join(c * 2 for c in h) if len(h) == 3 else h


def hls(h):
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    _, L, S = colorsys.rgb_to_hls(r, g, b)
    return L, S


def check(path):
    src = open(path, encoding="utf-8").read()
    flat = src.replace(" ", "")
    fails, warns, oks = [], [], []

    hexes = {hexnorm(h) for h in re.findall(r"#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b", src)}
    hexes = {h for h in hexes if len(h) == 6}
    lit = {h: hls(h) for h in hexes}

    # 1 纸白 + 近黑 + 至多一个强调色
    has_paper = any(l > 0.85 for l, _ in lit.values())
    has_ink = any(l < 0.20 for l, _ in lit.values())
    accents = sorted(h for h, (l, s) in lit.items() if h not in NEUTRAL_SKIP and s > 0.50 and 0.12 < l < 0.90)
    (oks if has_paper else fails).append("有浅纸底" if has_paper else "缺浅纸底")
    (oks if has_ink else fails).append("有近黑文字" if has_ink else "缺近黑文字")
    if len(accents) <= 1:
        oks.append(f"强调色 {len(accents)} 个(≤1)")
        if len(accents) == 0:
            warns.append("没有强调色 —— 纯黑白也可,确认是否刻意")
    else:
        fails.append(f"强调色过多 {accents} —— 瑞士风只用一个强调色")

    # 2 三套字体
    for f in ("Archivo", "Inter", "Noto+Sans+SC"):
        name = f.replace("+", " ")
        (oks if (f in src or name in src) else fails).append(
            f"字体 {name}" + ("" if (f in src or name in src) else " 缺失"))

    # 3 网格 + 细分割线
    for label, ok in [
        ("网格布局(display:grid)", "display:grid" in flat or "grid-template" in flat),
        ("细分割线(border-top)", "border-top" in flat),
    ]:
        (oks if ok else fails).append(label + ("" if ok else " 缺失"))

    # 4 扁平铁律
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
