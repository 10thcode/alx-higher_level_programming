#!/usr/bin/python3
"""
This module defines a function that appends a string at the end of a text
file (UTF8) and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file

    Args:
        filename (str): the name of the file
        text (str): the text to appended to the file
    Return (int): the number of characters added
    """
    if type(filename) is str and filename and type(text) is str and text:
        with open(filename, mode="a", encoding="utf-8") as file:
            return file.write(text)
