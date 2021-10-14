#!/usr/bin/python3
"""N queens"""
import sys


def check_position(pos, list_s):
    """[check_position]

    Args:
        pos ([list]): [position list]
        list_s ([list]): [list]

    Returns:
        [bool]: [description]
    """
    for element in list_s:
        con1 = element[1] == pos[1]
        con2 = (element[0] + element[1] == pos[0] + pos[1])
        con3 = (element[0] - element[1] == pos[0] - pos[1])
        if con1 or con2 or con3:
            return False
    return True


def nqueens(number, val_r, list_s):
    """[nqueens]

    Args:
        number ([int]): [size table]
        val_r ([int): [0]
        list_s ([list]): [list]
    """
    if (val_r == number):
        print(list_s)
    else:
        for val_c in range(number):
            pos = [val_r, val_c]
            check = check_position(pos, list_s)
            if check:
                list_s.append(pos)
                nqueens(number, val_r + 1, list_s)
                list_s.remove(pos)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        number = int(sys.argv[1])
    except:
        print("N must be a number\n")
        exit(1)
    if number < 4:
        print("N must be at least 4\n")
        exit(1)
    list_s = []
    nqueens(number, 0, list_s)
