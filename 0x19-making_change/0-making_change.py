#!/usr/bin/python3
""" 0x19. Making Change
"""


def makeChange(coins, total):
    """[summary]

    Args:
        coins ([list]): [the values of the coins in your possession]
        total ([int]): [description]

    Returns:
        [int]: [description]
    """
    if total <= 0:
        return 0

    array = [float('inf')] * (total + 1)
    array[0] = 0

    len_array = len(array)
    len_coins = len(coins)

    for x in range(1, len_array):
        for y in range(len_coins):
            if coins[y] <= x:
                array[x] = min(array[x], array[x - coins[y]] + 1)

    return array[x] if array[x] != float('inf') else -1
