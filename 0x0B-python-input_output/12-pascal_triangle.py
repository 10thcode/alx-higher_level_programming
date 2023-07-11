#!/usr/bin/python3
"""
This module defines a function that returns a list of lists
of integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    Gets a list of lists of integers representing the Pascla's triangle of n

    Args:
        n (int): number of list to form the triangle

    Return (list(list[int])): the Pascal triangle of n lists
    """
    list_ll = []
    if n <= 0:
        return list_ll

    list_ll.append([1])

    for count in range(n - 1):
        list_l = [1]
        i = 0
        while (i + 1 < len(list_ll[count])):
            list_l.append(list_ll[count][i] + list_ll[count][i + 1])
            i += 1
        list_l.append(1)
        list_ll.append(list_l)

    return (list_ll)
