#!/usr/bin/python3
"""
This is a script that adds all arguments to a Python list,
and then save them to a file
"""


if __name__ == "__main__":
    save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
    load_from_json_file = __import__("6-load_from_json_file").\
        load_from_json_file
    from sys import argv
    from os import path

    filename = "add_item.json"
    argv.pop(0)
    if not path.isfile(filename):
        save_to_json_file(argv, filename)
    else:
        li = load_from_json_file(filename)
        li += argv
        save_to_json_file(li, filename)
