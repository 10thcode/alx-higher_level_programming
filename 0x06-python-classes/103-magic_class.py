#!/usr/bin/python3
""" Utility for performing calculations on a circle """

import math


class MagicClass:
    """ Circle utility blueprint """
    def __init__(self, radius=0):
        """ MagicClass constructor """
        if type(radius) != int and type(radius) != float:
            raise TypeError('radius must be a number')
        else:
            self.radius = radius

    def area(self):
        """ Calculates the area of a circle """
        return (self.radius ** 2) * math.pi

    def circumference(self):
        """ Calculates the circumference of a circle """
        return (2 * math.pi) * self.radius
