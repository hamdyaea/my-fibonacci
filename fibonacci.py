#!/usr/bin/env python3
# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-only
"""Generate Fibonacci numbers starting with 1, 1."""
import argparse
from itertools import islice

def fibonacci():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b

def first_n(count: int) -> list[int]:
    if isinstance(count, bool) or not isinstance(count, int) or count < 0:
        raise ValueError("Count must be a nonnegative integer")
    return list(islice(fibonacci(), count))

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--count", type=int, default=100)
    args = parser.parse_args()
    try:
        print(first_n(args.count))
    except ValueError as exc:
        parser.error(str(exc))

if __name__ == "__main__":
    main()
