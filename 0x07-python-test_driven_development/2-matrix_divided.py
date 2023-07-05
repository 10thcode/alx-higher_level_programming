#!/usr/bin/python3
"""
This module contain a function that divide all element of a metrix
>>> print(matrix_divided([[1, 2, 3], [4, 5, 6]], 3))
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
"""


def matrix_divided(matrix=[[]], div=1):
    """
    A function that divides all elements of a matrix.
    """
    if div != div or div == float("inf") or \
            div == -float("inf") or type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list or len(matrix) == 0 or \
            type(matrix[0]) is not list:
        raise TypeError("matrix must be a matrix" +
                        " (list of lists) of integers/floats")
    new_matrix = []
    for item in matrix:
        if type(item) is not list:
            raise TypeError("matrix must be a matrix" +
                            " (list of lists) of integers/floats")
        if len(matrix[0]) != len(item):
            raise TypeError("Each row of the matrix must have the same size")
        new_item = []
        for element in item:
            if type(element) not in [int, float]:
                raise TypeError("matrix must be a matrix" +
                                " (list of lists) of integers/floats")
            new_item.append(round(element / div, 2))
        new_matrix.append(new_item)
    return new_matrix
