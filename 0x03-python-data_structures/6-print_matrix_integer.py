#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for li in matrix:
        for item in li:
            if li.index(item) == len(li) - 1:
                print("{:d}".format(item), end="")
            else:
                print("{:d}".format(item), end=" ")
        print()
