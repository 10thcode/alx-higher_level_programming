#!/usr/bin/python3
"""
This module define a function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text=""):
    """
    A function that prints a text with 2 new lines
    after each of these characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    if text == "":
        raise ValueError("no argument was passed")
    skip_space = True
    for letter in text:
        if letter == " " and skip_space:
            continue
        if letter not in [".", "?", ":"]:
            print("{}".format(letter), end="")
            skip_space = False
        else:
            print("{}".format(letter), end="\n\n")
            skip_space = True
