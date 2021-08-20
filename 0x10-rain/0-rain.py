#!/usr/bin/python3
"""sumary_line"""


def rain(walls):
    """[summary]

    Args:
        walls ([list]): [List of integers]
    """
    len_walls = len(walls)
    if len_walls == 0:
        return 0

    rainwater = 0
    for x in range(len_walls):
        if walls[x] != max(walls):
            max_lef = 0
            max_right = 0
            for y in range(0, x):
                if max_lef < walls[y]:
                    max_lef = walls[y]
            for z in range(x, len_walls):
                if max_right < walls[z]:
                    max_right = walls[z]
            if max_lef != 0 and max_right != 0:
                if max_lef < max_right and max_lef > walls[x]:
                    rainwater += max_lef - walls[x]
                elif max_right <= max_lef and max_right > walls[x]:
                    rainwater += max_right - walls[x]
    return rainwater
