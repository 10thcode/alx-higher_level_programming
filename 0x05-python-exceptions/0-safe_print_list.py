#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for idx in range(i, x):
            print("{}".format(my_list[idx]), end="")
            i += 1
    except IndexError:
        pass
    finally:
        print()
    return i
