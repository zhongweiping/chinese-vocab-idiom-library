#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
search.py — 中文字词成语库检索工具

扫描 ../references/ 下的库文件（characters.md / words.md / idioms.md），
按「汉字 / 词语 / 成语」或「拼音（带调或不带调均可）」检索，输出完整卡片片段。

用法：
    python3 search.py "明"            # 按汉字检索
    python3 search.py "pengyou"       # 按拼音（无调）检索
    python3 search.py "huà shé"       # 按拼音（带调、含空格）检索
    python3 search.py "画蛇"           # 按关键字检索成语
    python3 search.py                  # 列出库中全部条目
"""

import sys
import unicodedata
from pathlib import Path

# references 目录：scripts/ 的上一级下的 references/
REFS_DIR = (Path(__file__).resolve().parent.parent / "references").resolve()

# 需要扫描的库文件（顺序即展示顺序）
LIB_FILES = ["characters.md", "words.md", "idioms.md"]


def strip_tone(s: str) -> str:
    """去掉声调/变音符号，并把 ü 归并为 u，同时去除空格，便于拼音检索。"""
    s = unicodedata.normalize("NFKD", s)
    # 去掉所有组合附加符号（声调、¨ 等）
    s = "".join(c for c in s if not unicodedata.combining(c))
    return s.lower().replace(" ", "").replace("\u00a0", "")


def has_cjk(s: str) -> bool:
    return any("\u4e00" <= ch <= "\u9fff" for ch in s)


def parse_entries(text: str):
    """把 markdown 文本按 '### ' 切分为条目，返回 [(heading, body), ...]。"""
    entries = []
    cur_heading = None
    cur_lines = []
    for line in text.splitlines():
        if line.startswith("### "):
            if cur_heading is not None:
                entries.append((cur_heading, "\n".join(cur_lines).strip()))
            cur_heading = line[4:].strip()
            cur_lines = []
        else:
            if cur_heading is not None:
                cur_lines.append(line)
    if cur_heading is not None:
        entries.append((cur_heading, "\n".join(cur_lines).strip()))
    return entries


def load_all():
    """加载所有库文件，返回 [(source_file, heading, body), ...]。"""
    all_entries = []
    for fname in LIB_FILES:
        fpath = REFS_DIR / fname
        if not fpath.exists():
            continue
        text = fpath.read_text(encoding="utf-8")
        for heading, body in parse_entries(text):
            all_entries.append((fname, heading, body))
    return all_entries


def search(query: str, entries):
    """返回命中条目。中文按子串匹配；拼音按去调后子串匹配。"""
    q = query.strip()
    qn = strip_tone(q)
    q_is_cjk = has_cjk(q)
    hits = []
    for fname, heading, body in entries:
        full = f"{heading}\n{body}"
        fn = strip_tone(full)
        if q_is_cjk:
            if q in full:
                hits.append((fname, heading, body))
        else:
            # 拼音检索：去调 + 去空格后做子串匹配
            if qn and qn in fn:
                hits.append((fname, heading, body))
    return hits


def main():
    args = sys.argv[1:]
    entries = load_all()

    if not args:
        # 无参数：列出全部条目
        print(f"库中共有 {len(entries)} 个条目：\n")
        for fname, heading, _ in entries:
            print(f"  [{fname[:-3]}] {heading}")
        print("\n提示：python3 search.py <汉字 / 拼音 / 关键字> 进行检索。")
        return

    query = " ".join(args)
    hits = search(query, entries)

    if not hits:
        print(f"未找到与「{query}」匹配的条目。")
        print("可尝试更短的关键字，或按统一字段规范新增到 references/ 对应文件。")
        return

    print(f"🔍 检索「{query}」命中 {len(hits)} 条：\n")
    for fname, heading, body in hits:
        print(f"{'='*60}")
        print(f"来源：{fname}  |  {heading}")
        print(f"{'-'*60}")
        print(body)
        print()


if __name__ == "__main__":
    main()
