#!/usr/bin/python3
"""
This module defines a function that returns the
JSON representation of an object (string)
"""

import json


def to_json_string(my_obj):
    """
    Gets the JSON representation of an object

    Args:
        my_obj (object): the object to be converted to a JSON string

    Return (str): the JSON representation of @my_obj
    """
    return json.dumps(my_obj)
