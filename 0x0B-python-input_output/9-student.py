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

    def to_json(self):
        """ Retrieves a dictionary representation of a Student instance """
        return (self.__dict__)
