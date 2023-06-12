#!/usr/bin/python3

def multiple_returns(sentence):
    lenght = len(sentence)
    if lenght == 0:
        c = None
    else:
        c = sentence[0]
    return (lenght, c)
