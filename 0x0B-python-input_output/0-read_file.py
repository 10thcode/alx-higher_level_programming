#!/usr/bin/python3
"""
This module defines a function that reads
a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    Reads a text file and prints it to stdout

    Args:
        filename (str): the name of the file
    """
    if filename:
        with open(filename, mode="r", encoding="utf-8") as file:
            print(file.read(), end="")
