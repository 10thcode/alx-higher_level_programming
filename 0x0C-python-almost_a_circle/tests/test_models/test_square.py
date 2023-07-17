#!/usr/bin/python3
"""
This module provide test suite for Square class
"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    Test suite for Square class
    """
    def test_with_incorrect_number_of_agrs(self):
        """
        Test with no arguments passed to Sqaure class
        """
        with self.assertRaises(TypeError):
            square = Square()

        with self.assertRaises(TypeError):
            square = Square(4, 5, 6, 7, 8)

    def test_with_incorrect_arg_types(self):
        """
        Test with incorrect arguments types passed to Square class
        """
        with self.assertRaises(TypeError):
            square = Square("Hello")

        with self.assertRaises(TypeError):
            square = Square(3, [3, 4])

        with self.assertRaises(TypeError):
            square = Square(3, 4, (4, 5))

    def test_with_incorrect_assignment_types(self):
        """
        Test with incorrect types assigned to Square class attributes
        """
        square = Square(3, 2, 2)

        with self.assertRaises(TypeError):
            square.size = "Hello"

        with self.assertRaises(TypeError):
            square.x = []

        with self.assertRaises(TypeError):
            square.y = {4, 5}

    def test_with_incorrect_assignment_values(self):
        """
        Test with incorrect values assigned to Square class attributes
        """
        square = Square(3)

        with self.assertRaises(ValueError):
            square.size = 0

        with self.assertRaises(ValueError):
            square.x = -1

        with self.assertRaises(ValueError):
            square.y = -5

    def test_with_incorrect_arg_values(self):
        """
        Test with incorrect values passed as arguments to Square class
        """
        with self.assertRaises(ValueError):
            square = Square(0)

        with self.assertRaises(ValueError):
            square = Square(3, -1)

        with self.assertRaises(ValueError):
            square = Square(3, 1, -4)

    def test_with_correct_values_and_types(self):
        """
        Test with corsquare types and values passed as argument or assigned to
        Square class
        """
        square = Square(4)
        self.assertEqual(square.size, 4)

        square = Square(2, 3, 4, 51)
        self.assertEqual(square.size, 2)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 4)
        self.assertEqual(square.id, 51)

        square.size = 5
        self.assertEqual(square.size, 5)

        square.x = 0
        self.assertEqual(square.x, 0)

        square.y = 0
        self.assertEqual(square.y, 0)

    def test_str_magic_method(self):
        """
        Test __str__ magic method of Square class
        """
        square = Square(4, id=32)
        self.assertEqual(str(square), "[Square] (32) 0/0 - 4")

        square = Square(5, 2, 1, id=29)
        self.assertEqual(str(square), "[Square] (29) 2/1 - 5")

    def test_update_method_args_with_incorrect_types(self):
        """
        Test the update() public method *args with incorrect types
        in Square class
        """
        square = Square(3)

        with self.assertRaises(TypeError):
            square.update(1, "Hello")

        with self.assertRaises(TypeError):
            square.update(1, 3, [])

        with self.assertRaises(TypeError):
            square.update(1, 3, 2, (4,))

    def test_update_method_args_with_incorrect_values(self):
        """
        Test the update() public method *args with incorrect values
        in Square class
        """
        square = Square(34)

        with self.assertRaises(ValueError):
            square.update(1, 0)

        with self.assertRaises(ValueError):
            square.update(1, 3, -2)

        with self.assertRaises(ValueError):
            square.update(1, 3, 2, -3)

    def test_update_method_args_with_correct_values_and_types(self):
        """
        Test the update() public method with corsquare *args in Square class
        """
        square = Square(3, 4, 4, 5)

        square.update(10)
        self.assertEqual(square.id, 10)

        square.update(11, 5)
        self.assertEqual(square.id, 11)
        self.assertEqual(square.size, 5)

        square.update(4, 2, 6, 6)
        self.assertEqual(square.id, 4)
        self.assertEqual(square.size, 2)
        self.assertEqual(square.x, 6)
        self.assertEqual(square.y, 6)

    def test_update_method_kwargs_with_incorrect_types(self):
        """
        Test update() public method **kwargs with incorrect types
        in Square class
        """
        square = Square(10, 3, 4, 21)

        with self.assertRaises(TypeError):
            square.update(size=["string"])

        with self.assertRaises(TypeError):
            square.update(x=(3, 5))

        with self.assertRaises(TypeError):
            square.update(y=[])

    def test_update_method_kwargs_with_incorrect_values(self):
        """
        Test update() public method **kwargs with incorrect values
        in Square class
        """
        square = Square(10, 3, 4, 21)

        with self.assertRaises(ValueError):
            square.update(size=0)

        with self.assertRaises(ValueError):
            square.update(x=-1)

        with self.assertRaises(ValueError):
            square.update(y=-1)

    def test_update_method_kwargs_with_correct_values_and_types(self):
        """
        Test public methos update() with kwargs with corsquare values and types
        in Square class
        """
        square = Square(10, 3, 4, 21)

        square.update(size=5)
        self.assertEqual(square.size, 5)

        square.update(size=3, y=0, x=1, id=4)
        self.assertEqual(square.size, 3)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 0)
        self.assertEqual(square.id, 4)

        square.update(3, 4, size=6, y=1, x=0)
        self.assertEqual(square.size, 4)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 0)
        self.assertEqual(square.id, 3)

    def test_to_dictionary_method(self):
        """
        Test the to_dictionary public method in Square class
        """
        square = Square(3, 0, 0, 77)
        dictionary = square.to_dictionary()

        self.assertIsInstance(dictionary, dict)

        self.assertIn("id", dictionary)
        self.assertIn("size", dictionary)
        self.assertIn("x", dictionary)
        self.assertIn("y", dictionary)

        self.assertEqual(dictionary["id"], 77)
        self.assertEqual(dictionary["size"], 3)
        self.assertEqual(dictionary["x"], 0)
        self.assertEqual(dictionary["y"], 0)
