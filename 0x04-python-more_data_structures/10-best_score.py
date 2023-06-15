#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return (None)

    key = 0
    highest = 0

    for item in a_dictionary.values():
        highest = item
        break;
    
    for k, v in a_dictionary.items():
        if v > highest:
            key = k
            highest = v

    return key
