#!/usr/bin/python3
"""
This module define a function that prints My name is <first name> <last name>
>>> say_my_name("Black", "Genius")
My name is Black Genius
"""


def say_my_name(first_name="", last_name=""):
    """
    A function that prints My name is <first name> <last name>
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    if first_name == "" and last_name == "":
        raise ValueError("no name was provided")
    print("My name is {} {}".format(first_name, last_name))
