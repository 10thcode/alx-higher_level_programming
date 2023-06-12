#!/usr/bin/python3

def no_c(my_string):
    li = [char for char in my_string if char != "c" and char != "C"]
    new_string = "".join(li)
    return new_string
