#!/usr/bin/python3
""" This module defines a class MyInt that inherits from int """


class MyInt(int):
    """ A class MyInt that inherits from int """
    def __eq__(self, other):
        return False if self.real == other.real else True

    def __ne__(self, other):
        return False if self.real != other.real else True
