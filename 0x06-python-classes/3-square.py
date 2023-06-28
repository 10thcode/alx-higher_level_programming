#!/usr/bin/python3
""" Utitility for a square """


class Square:
    """ Blueprint for a square """
    def __init__(self, size=0):
        """
        Construct a square

        Args:
            size (int): size of a square
        """
        if type(size) == int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """
        Calculates the area of a square

        Return:
            int: Area of a square
        """
        return self.__size ** 2
