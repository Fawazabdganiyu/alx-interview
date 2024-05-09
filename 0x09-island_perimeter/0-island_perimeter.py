#!/usr/bin/python3
"""Island perimeter calculation"""


def island_perimeter(grid):
    """Calculate the perimeter of an island

    Args:
        grid(list): A list of list of integers,
            - 0 represents water
            - 1 represents land
            - Each cell is square, with a side length of 1
            - Cells are connected horizontally/vertically (not diagonally).
            - Grid is rectangular, with its width and height not exceeding 10
            - The grid is completely surrounded by water
            - There is only one island (or nothing).
            - The island doesn’t have “lakes” (water inside that
              isn’t connected to the water surrounding the island).

    Returns:
        int: The perimeter of the grid(island)
    """
    if not grid or not isinstance(grid, list):
        return 0

    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # Perimeter of a land cell is 4
            if grid[i][j] == 1:
                perimeter += 4
                # Deduct the shared boundary to the top
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                # Deduct the shared boundary to the left
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
