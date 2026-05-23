#!/usr/bin/env python3

import sys


if __name__ == "__main__":
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    j: int = 1
    length: int = len(sys.argv)
    if (length == 1):
        print("No arguments provided!")
    else:
        print(f"Arguments received: {length - 1}")
        while j < length:
            print(f"Argument {j}: {sys.argv[j]}")
            j = j + 1
    print(f"Total arguments: {len(sys.argv)}")
