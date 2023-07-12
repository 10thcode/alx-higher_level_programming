#!/usr/bin/python3
"""
This module defines a function that inserts a line of text
to a file, after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each
    line containing a specific string

    Args:
        filename (str): the name of the file
        search_string (str): the specific string to search
        new_string (str): the new string to be inserted
    """
    if type(filename) is str and filename and\
            type(search_string) is str and search_string and\
            type(new_string) is str and new_string:
        lines = []
        with open(filename, mode="r", encoding="utf-8") as file:
            for line in file:
                lines.append(line)
                if search_string in line:
                    lines.append(new_string)
        with open(filename, mode="w", encoding="utf-8") as file:
            file.writelines(lines)
