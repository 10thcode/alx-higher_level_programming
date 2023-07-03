#!/usr/bin/python3
""" Utility for a rectangle. """


class Rectangle():
    """ Blueprint for a rectangle. """
    def __init__(self, width=0, height=0):
        """
        Constructor for Rectangle class.

        Args:
            width (int): the width of the rectangle. width >= 0.
            height (int): the height of the rectangle. height >= 0.
        """
        self.width = width
        self.height = height

    def __str__(self):
        """ String representation of the rectangle with the character #. """
        if self.height == 0 or self.width == 0:
            return ""
        rect = ""
        for i in range(self.height):
            rect += ("#" * self.width) + '\n'
        return rect[:-1]

    def __repr__(self):
        """ String representation of the rectangle
        to be able to recreate a new instance. """
        return "Rectangle({}, {})".format(self.width, self.height)

    @property
    def width(self):
        """ Retrieve the value of __width. """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the value of __width.

        Args:
            value (int): the value fot the __width variable. value >= 0.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Retrieve the value of __height. """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the value of __height.

        Args:
            value (int): the value for the __height variable.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Calculates the area of a rectangle. """
        return self.height * self.width

    def perimeter(self):
        """ Calculates the perimeter of a rectangle. """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
