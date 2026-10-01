"""Chapter 10 teaching example. Python 3.9+; standard library only.

Run: python examples/10_python_annotations_and_parsing.py --output-dir results/demo
Reads an option and prints values; does not create files or run optimization.
"""
from __future__ import annotations

import argparse
from pathlib import Path


def identity(p: dict[str, float] | None = None):
    return p


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args()

    p = {"rho": 50.0}
    value = identity(p)
    annotation = identity.__annotations__["p"]
    print("p value:", value)
    print("p type:", type(value).__name__)
    print("annotation:", annotation)
    print("annotation type:", type(annotation).__name__)
    print("output path:", args.output_dir.as_posix() if args.output_dir is not None else None)


if __name__ == "__main__":
    main()
