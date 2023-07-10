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
