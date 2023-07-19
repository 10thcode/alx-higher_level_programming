#!/usr/bin/python3
"""
This module defines a Rectangle class.
"""
from .base import Base


class Rectangle(Base):
    """
    A rectangle class.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for the Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """
        Gets details about Rectangle.

        Returns:
            str: Details about a the Rectangle class.
        """
        fmt = "[Rectangle] ({}) {}/{} - {}/{}"
        return fmt.format(self.id, self.x, self.y, self.width, self.height)

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.

        Returns:
            int: The value of the width of the triangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width value of the rectangle.

        Args:
            value (int): The value for the width of the rectangle.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.

        Returns:
            int: The value of the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height value of the rectangle.

        Args:
            value (int): The value of the height of the rectangle.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Retrieves the value of x.

        Returns:
            int: The value of x.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets the value of x.

        Args:
            value (int): The value used to set x.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Retrieves the value of y.

        Returns:
            int: The value of y.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets the value of y.

        Args:
            value (int): The value used to set y.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculates the area value of a rectangle

        Return:
            int: the area of a rectangle
        """
        return self.width * self.height

    def display(self):
        """
        Prints a rectangle with the character #
        """
        print("{}".format(
            (("\n" * self.y) + ((" " * self.x) + ("#" * self.width) + "\n")
             * self.height)), end="")

        return True

    def update(self, *args, **kwargs):
        """
        Update fields in Rectangle class

        Args:
            args (tuple): Values used to update the fields in Rectangle class
        """
        if len(args) > 0 and type(args[0]) is int:
            try:
                self.id = args[0]
            except IndexError:
                pass
            try:
                self.width = args[1]
            except IndexError:
                pass
            try:
                self.height = args[2]
            except IndexError:
                pass
            try:
                self.x = args[3]
            except IndexError:
                pass
            try:
                self.y = args[4]
            except IndexError:
                pass
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Gets the dictionary representation of a Rectangle

        Returns:
            dict: the dictionary representation of a Rectangle
        """
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
