#!/usr/bin/env python3
"""Print line, word, and byte counts for files or stdin."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def count_text(data: bytes) -> tuple[int, int, int]:
    text = data.decode("utf-8", errors="replace")
    lines = text.count("\n")
    if text and not text.endswith("\n"):
        lines += 1
    words = len(text.split())
    return lines, words, len(data)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        help="Files to read (default: stdin)",
    )
    args = parser.parse_args()

    if not args.paths:
        data = sys.stdin.buffer.read()
        lines, words, nbytes = count_text(data)
        print(f"{lines:8d} {words:8d} {nbytes:8d}")
        return 0

    total_lines = total_words = total_bytes = 0
    for path in args.paths:
        data = path.read_bytes()
        lines, words, nbytes = count_text(data)
        total_lines += lines
        total_words += words
        total_bytes += nbytes
        print(f"{lines:8d} {words:8d} {nbytes:8d} {path}")

    if len(args.paths) > 1:
        print(f"{total_lines:8d} {total_words:8d} {total_bytes:8d} total")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
