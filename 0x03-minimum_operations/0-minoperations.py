#!/usr/bin/python3

""" In a text file, there is a single character H. Your text editor can execute
    only two operations in this file: Copy All and Paste. Given a number n,
    write a method that calculates the fewest number of operations needed to
    result in exactly n H characters in the file.
"""


import math


def factors(n):
    """ calculates the factors of n number
    """
    mylist = []
    while n % 2 == 0:
        mylist.append(2)
        n = n / 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            mylist.append(i)
            n = n / i
    if n > 2:
        mylist.append(n)
    return mylist


def minOperations(n):
    """ calculate the minimum operations
    """
    if type(n) != int or n < 2:
        return 0
    else:
        numOperations = sum(factors(n))
        return int(numOperations)
