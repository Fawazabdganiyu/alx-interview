#!/usr/bin/python3
"""Pascal's Triangle"""

def pascal_triangle(n):
    """ Returns a list of lists of integers representing
    the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    # Create the pascal triangle
    pascal = [[1]]
    for i in range(1, n):
        # Create the next row with the first 1
        row = [1]
        for j in range(1, i):
            # Append the sum of the two elements above
            row.append(pascal[i - 1][j - 1] + pascal[i - 1][j])
        # Append the last 1 of the row
        row.append(1)
        # Append the row to the pascal triangle
        pascal.append(row)
    return pascal
