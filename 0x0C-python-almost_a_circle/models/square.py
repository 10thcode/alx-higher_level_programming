#!/usr/bin/python3
"""
This module defines a Square class
"""
from .rectangle import Rectangle


class Square(Rectangle):
    """
    A Square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for Square class

        Args:
            size (int): the size of the square
            x (int): position of the squre on x-axis
            y (int): position of the squre on y-axis
            id (int): ID of the object
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Gets details about Square.

        Returns:
            str: Details about a the Square class.
        """
        fmt = "[Square] ({}) {}/{} - {}"
        return fmt.format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """
        Retrieve the size value of Square

        Returns:
            int: the size value of a Square
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the size value of Square

        Args:
            value (int): the value used to set the size
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update fields in Square class

        Args:
            args (tuple): Values used to update the fields in Square class
        """
        if len(args) > 0 and type(args[0]) is int:
            try:
                self.id = args[0]
            except IndexError:
                pass
            try:
                self.size = args[1]
            except IndexError:
                pass
            try:
                self.x = args[2]
            except IndexError:
                pass
            try:
                self.y = args[3]
            except IndexError:
                pass
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Gets the dictionary representation of a Square

        Returns:
            dict: the dictionary representation of a Square
        """
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
