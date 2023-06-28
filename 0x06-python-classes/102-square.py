#!/usr/bin/python3
""" Utitility for a square """


class Square:
    """ Blueprint for a square """
    def __init__(self, size=0):
        """
        Construct a square

        Args:
            size (int or float): size of a square
        """
        if type(size) in [int, float]:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be a number")

    def __eq__(self, other):
        """ Handle self == other """
        return True if self.area() == other.area() else False

    def __ne__(self, other):
        """ Handle self != other """
        return True if self.area() != other.area() else False

    def __lt__(self, other):
        """ Handle self < other """
        return True if self.area() < other.area() else False

    def __gt__(self, other):
        """ Handle self > other """
        return True if self.area() > other.area() else False

    def __le__(self, other):
        """ Handle self <= other """
        return True if self.area() <= other.area() else False

    def __ge__(self, other):
        """ Handle self >= other """
        return True if self.area() >= other.area() else False

    @property
    def size(self):
        """ Retrieve __size attribute """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Retrieve __size attribute

        Args:
            value (int): the value to assign to __size
        """
        if type(value) == int:
            if value >= 0:
                self.__size = value
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
