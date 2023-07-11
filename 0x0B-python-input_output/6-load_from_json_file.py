#!/usr/bin/python3
"""
This module defines a function that creates
an Object from a “JSON file”
"""

import json


def load_from_json_file(filename):
    """
    Creates an Object from a JSON file

    Args:
        filename (str): the name of the JSON file
    """
    if type(filename) is str and filename:
        with open(filename, mode="r", encoding="utf-8") as file:
            return json.load(file)
