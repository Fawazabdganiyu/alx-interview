#!/usr/bin/python3
"""N Queens problem module"""
from sys import argv, exit


def nqueens(N):
    """Print every possible solution to the problem
    """
    pass


if __name__ == "__main__":
    argc = len(argv) - 1
    if argc != 1:
        print("Usage: nqueens N")
        exit(1)

    N = argv[1]

    if not N.isdigit():
        print("N must be a number")
        exit(1)
    if int(N) < 4:
        print("N must be at least 4")
        exit(1)

    nqueens(N)
