#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        tuple_a = fix_tuple(tuple_a)
    if len(tuple_b) < 2:
        tuple_b = fix_tuple(tuple_b)
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])


def fix_tuple(tpl):
    if len(tpl) == 1:
        return (tpl[0], 0)
    return (0, 0)
