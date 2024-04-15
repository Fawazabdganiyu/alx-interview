#!/usr/bin/python3
"""N Queens problem module"""
from sys import argv, exit

result = []


def is_safe(board, row, col):
    """`Check if a queen can be placed on board[row][col]"""
    # Check this row on left side
    for i in range(col):
        if board[row][i]:
            return False

    # Check upper diagonal on left side
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal on left side
    i = row
    j = col
    while j >= 0 and i < 4:
        if board[i][j]:
            return False
        i = i + 1
        j = j - 1

    return True


def solve_nqueen_util(board, col):
    """Solve the NQueens problem recursively"""
    # base case: If all queens are placed return true
    if col == 4:
        v = []
        for i in board:
            for j in range(len(i)):
                if i[j] == 1:
                    v.append(j + 1)
        result.append(v)
        return True

    # Consider this column and try placing this queen in all rows one by one
    retval = False
    for i in range(4):
        # Check if queen can be placed on board[i][col]
        if is_safe(board, i, col):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # Make result true if any placement is possible
            retval = solve_nqueen_util(board, col + 1) or retval

            # If not a solution, backtrack
            board[i][col] = 0

    return retval


def nqueens(n):
    """Print every possible solution to the problem
    """
    result.clear()
    board = [[0 for j in range(n)] for i in range(n)]
    solve_nqueen_util(board, 0)
    result.sort()
    return result


if __name__ == "__main__":
    argc = len(argv) - 1
    if argc != 1:
        print("Usage: nqueens N")
        exit(1)

    n = argv[1]

    if not n.isdigit():
        print("N must be a number")
        exit(1)
    if int(n) < 4:
        print("N must be at least 4")
        exit(1)

    solutions = nqueens(int(n))
    for solution in solutions:
        print([[i, solution[i]] for i in range(len(solution))])
