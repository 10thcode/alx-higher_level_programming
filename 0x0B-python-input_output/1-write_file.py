#!/usr/bin/python3
"""
This module defines a function that writes a string to a text
file (UTF8) and returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file

    Args:
        filename (str): the name of the file
        text (str): the text to be written to the file

    Return (int): the number of characters written
    """
    if type(filename) is str and filename and type(text) is str and text:
        with open(filename, mode="w", encoding="utf-8") as file:
            return file.write(text)
