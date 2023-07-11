#!/usr/bin/python3
"""
This module defines a class Student that defines a student by
"""


class Student():
    """ A student class """
    def __init__(self, first_name, last_name, age):
        """
        Student constructor

        Args:
            first_name (str): The student first name
            last_name (str): The student last name
            age (int): The student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves a dictionary representation of a Student instance """
        if type(attrs) is not list:
            return (self.__dict__)

        for item in attrs:
            if type(item) is not str or not item:
                return (self.__dict__)

        return {key: value for key, value in self.__dict__.items()
                if key in attrs}
