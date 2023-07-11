#!/usr/bin/python3
"""
This module defines a function that writes an
Object to a text file, using a JSON representation
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes and Object to a text file

    Args:
        my_obj (obj): the python object
        filename (str): the name of the file
    """
    if type(filename) is str and filename:
        with open(filename, mode="w", encoding="utf-8") as file:
            json.dump(my_obj, file)
