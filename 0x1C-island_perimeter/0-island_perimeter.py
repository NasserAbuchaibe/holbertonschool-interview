#!/usr/bin/python3
""" Island Perimeter
"""


def island_perimeter(grid):
    """[summary]

    Args:
        grid ([type]): [description]

    Returns:
        [type]: [description]
    """

    perimetrer = 0
    len_grid = len(grid)
    for x in range(len_grid):
        for y in range(len(grid[x])):
            if (grid[x][y] == 1):
                if (x <= 0 or grid[x - 1][y] == 0):
                    perimetrer += 1
                if (x >= len(grid) - 1 or grid[x + 1][y] == 0):
                    perimetrer += 1
                if (y <= 0 or grid[x][y - 1] == 0):
                    perimetrer += 1
                if (y >= len(grid[x]) - 1 or grid[x][y + 1] == 0):
                    perimetrer += 1
    return perimetrer
