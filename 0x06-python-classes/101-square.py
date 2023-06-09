#!/usr/bin/python3
""" Utitility for a square """


class Square:
    """ Blueprint for a square """
    def __init__(self, size=0, position=(0, 0)):
        """
        Construct a square

        Args:
            size (int): size of a square
            position (Tuple[int]): position of a square
        """
        self.size = size
        self.position = position

    def __str__(self):
        """ Prints a square on stdout """
        squares = ""
        if self.size == 0:
            return squares
        for i in range(0, self.position[1]):
            squares += "\n"
        for i in range(0, self.size):
            squares += (" " * self.position[0]) + ("#" * self.size) + "\n"
        return squares[:-1]

    @property
    def size(self):
        """ Retrieve __size attribute """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Retrieve __size attribute

        Args:
            value (int): the value to assign to __size
        """
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        """ Retrieve __position attribut """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set __position attribute

        Args:
            value (tuple[int]): Position to print the square
        """
        if len(value) == 2 and type(value[0]) is int and \
                type(value[1]) is int and min(value) >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """
        Calculates the area of a square

        Return:
            int: Area of a square
        """
        return self.size ** 2

    def my_print(self):
        """ Prints a square on stdout """
        if self.size == 0:
            print()
            return None
        for i in range(0, self.position[1]):
            print()
        for i in range(0, self.size):
            print("{}{}".format(" " * self.position[0], "#" * self.size))
