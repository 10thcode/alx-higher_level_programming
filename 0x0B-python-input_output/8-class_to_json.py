#!/usr/bin/python3
"""
This module defines a function that returns the dictionary description
with simple data structure (list, dictionary, string, integer
and boolean) for JSON serialization of an object
"""


def class_to_json(obj):
    """
    Gets a dictionary description with simple data structure for
    JSON serialization of an object

    Args:
        obj (class instance): an instance of a class

    Return (dict): a dictionary for JSON serialization
    """
    return (obj.__dict__)
