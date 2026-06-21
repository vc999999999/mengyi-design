#!/usr/bin/env python3
"""电子梦呓 · 出图自检 / self-check.

用法:
    python check_style.py 产出.html [更多.html ...]

配色是「规则」不是固定 hex —— 锁的是丝网冲击力,允许整套换色:
必须项(缺/违反 = FAIL,退出码非 0):
  有近黑墨色、有暖浅纸底、≥3 个高饱和强调色(丝网命脉)、两套字体(Noto Sans SC + Space Mono)、
  warp 滤镜、纸张颗粒、半调网点、刊头条(电子梦呓)、含一个字的变异标题。
软提示(WARN):变异处过多(>6,可能"处处都怪")、疑似瘆人词(与可爱契约冲突)。

设计意图:给"出图质量"一个客观闸门;默认即品牌,换色只要守住「墨黑+暖纸+高饱和强调」即可。
"""
import re, sys, colorsys

CREEPY = ["獠牙", "骷髅", "内脏", "血肉", "尸", "腐", "空洞黑眼", "密集眼"]


def hexnorm(h):
    h = h.upper().lstrip("#")
    return "".join(c * 2 for c in h) if len(h) == 3 else h


def hls(h):
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    H, L, S = colorsys.rgb_to_hls(r, g, b)
    return H, L, S


def check(path):
    src = open(path, encoding="utf-8").read()
    flatnospace = src.replace(" ", "")
    fails, warns, oks = [], [], []

    hexes = {hexnorm(h) for h in re.findall(r"#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b", src)}
    hexes = {h for h in hexes if len(h) == 6}
    lit = {h: hls(h) for h in hexes}

    # 1 配色规则:墨黑底 + 暖浅纸底 + ≥3 高饱和强调色
    has_ink = any(l < 0.20 for _, l, _ in lit.values())
    has_paper = any(l > 0.78 for _, l, _ in lit.values())
    vivid = sorted(h for h, (hh, l, s) in lit.items() if s > 0.50 and 0.20 < l < 0.82)
    (oks if has_ink else fails).append("有近黑墨色" if has_ink else "缺近黑墨色(底/线应近黑)")
    (oks if has_paper else fails).append("有暖浅纸底" if has_paper else "缺暖浅纸底")
    (oks if len(vivid) >= 3 else fails).append(
        f"高饱和强调色 {len(vivid)} 个(≥3)" if len(vivid) >= 3
        else f"高饱和强调色不足({len(vivid)}<3)—— 丝网风需要高饱和冲击力")

    # 2 字体
    for f in ("Noto+Sans+SC", "Space+Mono"):
        name = f.replace("+", " ")
        (oks if (f in src or name in src) else fails).append(
            f"字体 {name}" + ("" if (f in src or name in src) else " 缺失"))

    # 3 质感
    for label, ok in [
        ("warp 位移滤镜", 'id="warp"' in src and "url(#warp)" in src),
        ("纸张颗粒 grain", "feTurbulence" in src and "mix-blend-mode:multiply" in flatnospace),
        ("半调网点 halftone", "radial-gradient" in src or 'id="halftone"' in src),
    ]:
        (oks if ok else fails).append(label + ("" if ok else " 缺失"))

    # 4 锚点
    for label, ok in [
        ("刊头条(电子梦呓)", "电子梦呓" in src),
        ("插画位/孔洞", any(k in src for k in ("masc", "frame", "opening", "pic", "hero"))),
    ]:
        (oks if ok else fails).append(label + ("" if ok else " 缺失"))

    # 5 变异标题
    muts = len(re.findall(r'class="[^"]*\bmut\b', src)) + src.count("scaleY")
    if muts == 0:
        fails.append("变异标题: 一个变异字都没有")
    else:
        oks.append(f"变异标题(共 {muts} 处)")
        if muts > 6:
            warns.append(f"变异处偏多({muts}) —— 留意'一处变异原则'")

    # 6 可爱契约
    hit = [w for w in CREEPY if w in src]
    if hit:
        warns.append(f"出现疑似瘆人词 {hit} —— 与'可爱契约'冲突,确认基调")

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
