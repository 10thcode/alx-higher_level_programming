#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dict = {}

    for item in a_dictionary.keys():
        new_dict[item] = a_dictionary[item] * 2

    return new_dict
