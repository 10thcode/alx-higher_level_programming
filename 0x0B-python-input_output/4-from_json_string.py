#!/usr/bin/python3
"""
This module defines a function that returns an object
(Python data structure) represented by a JSON string
"""

import json


def from_json_string(my_str):
    """
    Gets an object represented by a JSON string

    Args:
        my_str (str): the JSON string

    Return (obj): Python data structure of @my_str
    """
    if type(my_str) and my_str:
        return json.loads(my_str)
