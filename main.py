#!/usr/bin/env python3
"""news-image-20261121 entry: copy the front page to /output/entry.png.

The poster itself (entry.png) is the entry: a newspaper front page summing
up the world news of Saturday 21 November 2026. This program only delivers
that image to the grader's output directory. Python 3.13, standard library
only, no network.
"""
import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.isfile(src):
        print("error: entry.png missing next to main.py", file=sys.stderr)
        sys.exit(1)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    size = os.path.getsize(dst)
    if size > 1024 * 1024:
        print("error: entry.png over 1 MiB:", size, file=sys.stderr)
        sys.exit(1)
    print("wrote", dst, size, "bytes")


if __name__ == "__main__":
    main()
