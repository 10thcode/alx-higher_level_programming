#!/usr/bin/python3

for first_digit in range(0, 10):
    for last_digit in range(0, 10):
        if first_digit != last_digit and last_digit > first_digit:
            if (first_digit == 8 and last_digit == 9):
                print("{}{}".format(first_digit, last_digit))
            else:
                print("{}{}".format(first_digit, last_digit), end=", ")
