#!/usr/bin/python3

def roman_to_int(roman_string):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    sum = 0
    prev_letter = ""

    if not roman_string or type(roman_string) is not str:
        return (0)

    for current_letter in roman_string.upper():
        if (prev_letter):
            if (roman[prev_letter] < roman[current_letter]):
                sum -= (roman[prev_letter] * 2)
        sum += roman[current_letter]
        prev_letter = current_letter

    return (sum)
