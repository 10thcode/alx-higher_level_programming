#!/usr/bin/python3
""" Geometry utility """

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ A square utility class """
    def __init__(self, size):
        """
        Square constructor

        Args:
            size (int): the size of the square
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ Calculates the area of a square """
        return self.__size ** 2
