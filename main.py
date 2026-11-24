#!/usr/bin/env python3
"""Entry for make.fun competition:
"Make the AI Judge Laugh: Cat Reviews Its Human".

Writes one funny single-line one-star review, written by a house cat
about its human, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

Python 3, standard library only. Deterministic: the same text is
written on every run.
"""

import os

REVIEW = (
    "One star. He locks the bathroom door like I don't pay rent. "
    "I don't. Neither does he. The bank owns us both, "
    "and it has never once fed me."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
