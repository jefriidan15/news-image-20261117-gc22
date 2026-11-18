#!/usr/bin/env python3
"""news-image-20261117 entry (Python 3.13, standard library only).

The program copies the entry.png beside this file to the output
directory: /output in the grader, or $MAKEFUN_OUTPUT_DIR elsewhere.
Run:  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUT.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "entry.png", OUT / "entry.png")
print("wrote", OUT / "entry.png")
