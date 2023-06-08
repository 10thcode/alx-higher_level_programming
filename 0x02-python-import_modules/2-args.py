#!/usr/bin/python3

import sys


def main():
    argc = len(sys.argv) - 1
    if len(sys.argv) == 2:
        print("{} argument:".format(argc))
    elif argc == 0:
        print("{} arguments.".format(argc))
    else:
        print("{} arguments:".format(argc))

    for i in range(1, argc + 1):
        print("{}: {}".format(i, sys.argv[i]))


if __name__ == "__main__":
    main()
