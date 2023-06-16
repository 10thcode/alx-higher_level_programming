#!/usr/bin/python3

def weight_average(my_list=[]):
    """
    Calculates the weighted average of all integers tuple

    Args:
        my_list: A list of tuples

    Returns:
        float: The weighted average
    """
    total = 0
    weight_total = 0
    if not my_list:
        return 0
    for my_tuple in my_list:
        total += (my_tuple[0] * my_tuple[1])
        weight_total += my_tuple[1]
    return total / weight_total
