#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    if matrix:
        for li in matrix:
            new_matrix.append([item**2 for item in li])

    return new_matrix
