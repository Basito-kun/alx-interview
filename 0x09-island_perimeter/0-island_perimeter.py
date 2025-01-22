#!/usr/bin/python3
"""
A script that returns the perimeter of an island.
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    Args:
        grid (list of list of int): A 2D list representing the map where
                                    0 represents water and 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # Land found
                # Start with a full perimeter for this cell (4 sides)
                perimeter += 4
                # Check the neighboring cells to subtract shared sides
                if i > 0 and grid[i - 1][j] == 1:  # Check top
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:  # Check left
                    perimeter -= 2

    return perimeter
