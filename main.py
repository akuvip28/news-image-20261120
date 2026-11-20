#!/usr/bin/env python3
"""make.fun entry: Sum up 20 November's world news in one image.

Writes one image to /output/entry.png. The image (asset/news-20261120.png,
rendered offline from the public news digests of Friday 20 November 2026)
is copied byte-for-byte, so the program needs no network, has no
dependencies beyond the Python standard library, and produces identical
bytes on every run.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "asset", "news-20261120.png")
DST = "/output/entry.png"


def main():
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()
