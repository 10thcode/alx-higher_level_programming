#!/usr/bin/python3
'''
Defines a function find_peak()
'''


def find_peak(list_of_integers):
    '''
    Finds a peak in a list of unsorted integers.

    Args:
        list_of_integers: list of interger

    Return:
        int: the peak in a list_of_integers.
    '''
    list_of_integers.sort()
    return list_of_integers[-1] if list_of_integers else None
