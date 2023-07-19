#!/usr/bin/python3
""" This module defines a test class for the Square class """
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_width_from_valid_values_with_id(self):
        square = Square(10, 1, 1, 10)
        self.assertEqual(10, square.width)

    def test_height_from_valid_values_with_id(self):
        square = Square(10, 1, 1, 10)
        self.assertEqual(10, square.height)

    def test_x_from_valid_values_with_id(self):
        square = Square(10, 1, 1, 10)
        self.assertEqual(1, square.x)

    def test_y_from_valid_values_with_id(self):
        square = Square(10, 1, 1, 10)
        self.assertEqual(1, square.y)

    def test_id_from_valid_values_with_id(self):
        square = Square(10, 1, 1, 10)
        self.assertEqual(10, square.id)

    def test_width_from_invalid_type(self):
        with self.assertRaises(TypeError):
            Square("10", 1, 1, 10)

    def test_x_from_invalid_x(self):
        with self.assertRaises(TypeError):
            Square(10, "1", 1, 10)

    def test_y_from_invalid_y(self):
        with self.assertRaises(TypeError):
            Square(10, 1, "1", 10)

    def test_id_without_obj_id(self):
        square = Square(10, 1, 1)
        self.assertEqual(31, square.id)

    def test_id_from_invalid_value(self):
        with self.assertRaises(ValueError):
            Square(-10, 1, 1, 10)

    def test_width_from_negative_value(self):
        with self.assertRaises(ValueError):
            Square(0, 1, 1, 10)

    def test_x_from_invalid_value(self):
        with self.assertRaises(ValueError):
            Square(10, -1, 1, 10)

    def test_y_from_invalid_value(self):
        with self.assertRaises(ValueError):
            Square(10, 1, -1, 10)

    def test_height_one_positional_arg_provided(self):
        square = Square(10)
        self.assertEqual(10, square.height)

    def test_no_positional_arg_provided(self):
        with self.assertRaises(TypeError):
            Square()

    def test_size_attribute_with_valid_size(self):
        square = Square(5)
        square.size = 10
        self.assertEqual(10, square.size)

    def test_size_attribute_with_valid_size_from_init(self):
        square = Square(10)
        self.assertEqual(10, square.size)

    def test_width_attribute_with_valid_size(self):
        square = Square(5)
        self.assertEqual(10, square.width)

    def test_height_attribute_with_valid_size(self):
        square = Square(5)
        self.assertEqual(10, square.height)

    def test_width_attribute_with_valid_size(self):
        square = Square(5)
        square.size = 10
        self.assertEqual(10, square.width)

    def test_height_attribute_with_valid_size(self):
        square = Square(5)
        square.size = 10
        self.assertEqual(10, square.height)

    def test_size_attribute_with_invalid_size_type(self):
        with self.assertRaises(TypeError):
            square = Square(5)
            square.size = "10"

    def test_size_attribute_with_invalid_size_value(self):
        with self.assertRaises(ValueError):
            square = Square(5)
            square.size = 0

    def test_update_with_one_arg(self):
        square = Square(5)
        square.update(10)
        self.assertEqual("[Square] (10) 0/0 - 5", str(square))

    def test_update_with_two_args(self):
        square = Square(5)
        square.update(1, 2)
        self.assertEqual("[Square] (1) 0/0 - 2", str(square))

    def test_update_with_three_args(self):
        square = Square(5)
        square.update(1, 2, 3)
        self.assertEqual("[Square] (1) 3/0 - 2", str(square))

    def test_update_with_four_args(self):
        square = Square(5)
        square.update(1, 2, 3, 4)
        self.assertEqual("[Square] (1) 3/4 - 2", str(square))

    def test_update_with_one_args_and_kwargs(self):
        square = Square(5)
        square.update(10, size=990)
        self.assertEqual("[Square] (10) 0/0 - 5", str(square))

    def test_update_with_empty_args_and_one_kwargs(self):
        square = Square(5)
        square.update((), size=10)
        self.assertEqual("[Square] (38) 0/0 - 10", str(square))

    def test_update_with_empty_args_and_two_kwargs(self):
        square = Square(5)
        square.update(x=3, y=4)
        self.assertEqual("[Square] (39) 3/4 - 5", str(square))

    def test_update_with_two_args_and_one_kwargs(self):
        square = Square(5)
        square.update(2, 3)
        self.assertEqual("[Square] (2) 0/0 - 3", str(square))

    def test_update_with_all_args_and_all_kwargs(self):
        square = Square(10, 10, 10, 10)
        square.update(1, 1, 1, 1, id=19, size=19, x=19, y=19)
        self.assertEqual("[Square] (1) 1/1 - 1", str(square))

    def test_to_dictionary_with_all_attributes_present(self):
        square = Square(10, 1, 1, 1)
        actual = square.to_dictionary()
        self.assertEqual({"id": 1, "size": 10, "x": 1, "y": 1}, actual)

    def test_to_dictionary_with_only_size_specified(self):
        square = Square(10)
        actual = square.to_dictionary()
        self.assertEqual({"id": 37, "size": 10, "x": 0, "y": 0}, actual)

    def test_to_dictionary_with_no_id_specified(self):
        square = Square(10, 9, 9)
        actual = square.to_dictionary()
        self.assertEqual({"id": 36, "size": 10, "x": 9, "y": 9}, actual)