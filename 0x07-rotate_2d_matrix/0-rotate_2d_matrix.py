#!/usr/bin/python3
"""90 degrees Clockwise matrix rotation module"""


def rotate_2d_matrix(matrix):
    """Rotate 2D matrix by 90 degrees clockwise

    Args:
        matrix (List[List[int]]): 2D matrix to be rotated
    """
    n = len(matrix)
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            # Swap matrix[i][j] and matrix[j][i]
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse the matrix
    for i in range(n):
        matrix[i].reverse()
