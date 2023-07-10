#!/usr/bin/python3
"""
This module defines a function that returns True if the object is
exactly an instance of the specified class, otherwise False
"""


def is_same_class(obj, a_class):
    """
    A function that returns True if the object is exactly an
    instance of the specified class ; otherwise False.
    """
    return type(obj) is a_class
