#!/usr/bin/python3
""" Geometry utility """


class BaseGeometry():
    """ Geometry utility class """
    def area(self):
        """ Raises an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates a value

        Args:
            name (string): a text to be printed as part of an exception
            value (int): the value to be validated
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
