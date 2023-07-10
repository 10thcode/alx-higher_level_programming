#!/usr/bin/python3
"""
This module defines a class MyList that inherits from list
"""


class MyList(list):
    """ a class that inherits from list """
    def print_sorted(self):
        """ prints the list, but sorted (ascending sort) """
        print(sorted(super().copy()))
