#!/usr/bin/python3
""" Geometry utility """


class BaseGeometry():
    """ Geometry utility class """
    def area(self):
        """ Raises an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name="", value=0):
        """
        Validates a value

        Args:
            name (string): a text to be printed as part of an exception
            value (int): the value to be validated
        """
        if type(name) is not str:
            raise TypeError("name must be a string")
        if name == "":
            raise ValueError("name cannot be empty")
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ Rectangle utility class """
    def __init__(self, width, height):
        """
        Rectangle contructor

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Calculates the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


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

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
