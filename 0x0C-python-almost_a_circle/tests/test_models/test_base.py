#!/usr/bin/python3
"""
This module provides a test suite for Base class
"""
import unittest
from models.base import Base
from os import path


class TestBase(unittest.TestCase):
    """
    Test suite for Base class
    """
    def test_with_one_arg(self):
        """
        Test with one argument passed to Base class
        """
        base = Base(3)
        self.assertEqual(base.id, 3)
        base = Base(4)
        self.assertEqual(base.id, 4)

    def test_with_more_than_one_arg(self):
        """
        Test with more than one argument passed to Base class
        """
        with self.assertRaises(TypeError):
            base = Base(2, 4)

    def test_to_json_string_method_with_incorrect_arg_type(self):
        """
        Test the to_json_string() static method of Base class with incorrect
        argument type
        """
        base = Base(34)

        with self.assertRaises(TypeError):
            base.to_json_string()

        with self.assertRaises(TypeError):
            base.to_json_string("Hello")

        with self.assertRaises(TypeError):
            base.to_json_string([2, 2])

    def test_to_json_string_method_return_type(self):
        """
        Test the return type of the to_json_string() static method of
        Base class
        """
        base = Base(34)
        self.assertIsInstance(base.to_json_string([{2: 3, 3: 4}]), str)

    def test_to_json_string_method_return_value(self):
        """
        Test the return value of the to_json_string() static method of
        Base class
        """
        base = Base()
        self.assertEqual("[]", base.to_json_string(None))
        self.assertEqual("[]", base.to_json_string([]))
        self.assertEqual('[{"hello": 1, "world": 2}]',
                         base.to_json_string([{'hello': 1, 'world': 2}]))

    def test_save_to_file_method_with_incorrect_arg_type(self):
        """
        Test the save_to_file_method class method of Base class
        with incorrect type passed as arguement
        """
        from models.rectangle import Rectangle
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

        with self.assertRaises(TypeError):
            Rectangle.save_to_file("Hello World")

        with self.assertRaises(TypeError):
            Rectangle.save_to_file(["Hello", "World"])

    def test_save_to_file_method(self):
        """
        Test the save_to_file() class method of Base class
        """
        from models.rectangle import Rectangle
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        self.assertTrue(path.isfile("Rectangle.json"))

        from models.square import Square
        s1 = Square(10, 7, 2, 8)
        s2 = Square(2, 4)
        Square.save_to_file([s1, s2])
        self.assertTrue(path.isfile("Square.json"))

    def test_from_json_string(self):
        """
        Test the from_json_string() static method of Base class
        """
        base = Base()

        with self.assertRaises(TypeError):
            base.from_json_string()

        with self.assertRaises(TypeError):
            base.from_json_string(2)

        output = base.from_json_string(None)
        self.assertListEqual(output, [])

        json_string = "[2, 4, 6, 8]"
        output = base.from_json_string(json_string)
        self.assertListEqual(output, [2, 4, 6, 8])

    def test_create_method_with_incorrect_type_in_dictionary(self):
        """
        Test the create() class method of Base class with incorrect types in
        the dictionary
        """
        from models.rectangle import Rectangle

        with self.assertRaises(TypeError):
            dictionary = {"id": 21, "width": "Hello"}
            rect = Rectangle.create(**dictionary)

        with self.assertRaises(TypeError):
            dictionary = {"id": 21, "width": 3, "height": []}
            rect = Rectangle.create(**dictionary)

        with self.assertRaises(TypeError):
            dictionary = {"id": 21, "width": 3, "height": 3, "x": "World"}
            rect = Rectangle.create(**dictionary)

        with self.assertRaises(TypeError):
            dictionary = {"id": 21, "width": 3, "height": 3, "x": 0, "y": "Hi"}
            rect = Rectangle.create(**dictionary)

        from models.square import Square

        with self.assertRaises(TypeError):
            dictionary = {"id": 21, "size": "Hello"}
            square = Square.create(**dictionary)

        with self.assertRaises(TypeError):
            dictionary = {"id": 21, "size": 3, "x": "World"}
            square = Square.create(**dictionary)

        with self.assertRaises(TypeError):
            dictionary = {"id": 21, "size": 3, "x": 0, "y": "Hi"}
            square = Square.create(**dictionary)

    def test_create_method_with_incorrect_values(self):
        """
        Test the create() classs method of Base class with incorrect values
        in the dictionary
        """
        from models.rectangle import Rectangle

        with self.assertRaises(ValueError):
            dictionary = {"id": 21, "width": -3}
            rect = Rectangle.create(**dictionary)

        with self.assertRaises(ValueError):
            dictionary = {"id": 21, "width": 3, "height": 0}
            rect = Rectangle.create(**dictionary)

        with self.assertRaises(ValueError):
            dictionary = {"id": 21, "width": 3, "height": 0, "x": -1}
            rect = Rectangle.create(**dictionary)

        with self.assertRaises(ValueError):
            dictionary = {"id": 21, "width": 3, "height": 0, "x": 1, "y": -2}
            rect = Rectangle.create(**dictionary)

        from models.square import Square

        with self.assertRaises(ValueError):
            dictionary = {"id": 21, "size": -3}
            square = Square.create(**dictionary)

        with self.assertRaises(ValueError):
            dictionary = {"id": 21, "size": 3, "x": -1}
            square = Square.create(**dictionary)

        with self.assertRaises(ValueError):
            dictionary = {"id": 21, "size": 3, "x": 1, "y": -2}
            square = Square.create(**dictionary)

    def test_create_method(self):
        """
        Test the create() class method of Base class
        """
        from models.rectangle import Rectangle
        dictionary = {"id": 21, "width": 3, "height": 2, "x": 1, "y": 1}
        rect = Rectangle.create(**dictionary)
        self.assertEqual(rect.id, 21)
        self.assertEqual(rect.width, 3)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 1)

        from models.square import Square
        dictionary = {"id": 33, "size": 2, "x": 5, "y": 3}
        square = Square.create(**dictionary)
        self.assertEqual(square.id, 33)
        self.assertEqual(square.size, 2)
        self.assertEqual(square.x, 5)
        self.assertEqual(square.y, 3)

    def test_load_from_file(self):
        """
        Test the load_from_file() class method of Base class
        """
        from models.rectangle import Rectangle
        rect = Rectangle.load_from_file()

        self.assertIsInstance(rect, list)
