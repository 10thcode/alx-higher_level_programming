#!/usr/bin/python3

def best_score(a_dictionary):
    key = None
    highest = 0

    if a_dictionary:
        for k, v in a_dictionary.items():
            if v > highest:
                key = k
                highest = v

    return key
