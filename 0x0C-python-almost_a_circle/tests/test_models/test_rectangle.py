#!/usr/bin/python3
"""
This module provides a test suite for Rectangle class
"""
import unittest
from models.rectangle import Rectangle
import sys
from io import StringIO


class TestRectangle(unittest.TestCase):
    """
    Test suite for Rectangle class
    """
    def test_with_less_than_two_args(self):
        """
        Test with less that two arguments passed to Rectangle class
        """
        with self.assertRaises(TypeError):
            rect = Rectangle(5)

        with self.assertRaises(TypeError):
            rect = Rectangle()

    def test_with_only_two_args(self):
        """
        Test with only two arguments passed to Rectangle class
        """
        rect = Rectangle(10, 2)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)

    def test_with_all_args(self):
        """
        Test with all arguments passed to Rectangle class
        """
        rect = Rectangle(10, 2, 0, 3, 2)
        self.assertEqual(rect.id, 2)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 3)

    def test_with_more_than_five_args(self):
        """
        Test with more than five args passed to Rectangle class
        """
        with self.assertRaises(TypeError):
            rect = Rectangle(2, 4, 6, 8, 10, 12)

    def test_with_incorrect_arg_types(self):
        """
        Test with incorrect types passed as argument to Rectangle class
        """
        with self.assertRaises(TypeError):
            rect = Rectangle("3", 2, 4, 4)

        with self.assertRaises(TypeError):
            rect = Rectangle(3, [], 3, 4)

        with self.assertRaises(TypeError):
            rect = Rectangle(3, 2, "hello", 4)

        with self.assertRaises(TypeError):
            rect = Rectangle(3, 2, 4, (3, 4))

    def test_with_incorrect_assignment_types(self):
        """
        Test with incorrect types assigned to Rectangle class attributes
        """
        rect = Rectangle(3, 2, 1, 1, 21)

        with self.assertRaises(TypeError):
            rect.width = "hello"

        with self.assertRaises(TypeError):
            rect.height = [2, 3]

        with self.assertRaises(TypeError):
            rect.x = (2, 3)

        with self.assertRaises(TypeError):
            rect.y = {3, 4, 5}

    def test_with_incorrect_arg_values(self):
        """
        Test with incorrect values passed as argument to Rectangle class
        """
        with self.assertRaises(ValueError):
            rect = Rectangle(-4, 2, 4, 5)

        with self.assertRaises(ValueError):
            rect = Rectangle(10, 0, 0, 0)

        with self.assertRaises(ValueError):
            rect = Rectangle(2, 10, -2, 0)

        with self.assertRaises(ValueError):
            rect = Rectangle(2, 10, 2, -1)

    def test_with_incorrect_assignment_values(self):
        """
        Test with incorrect values assigned to Rectangle class attributes
        """
        rect = Rectangle(2, 10, 0, 0)

        with self.assertRaises(ValueError):
            rect.width = 0

        with self.assertRaises(ValueError):
            rect.height = -10

        with self.assertRaises(ValueError):
            rect.x = -1

        with self.assertRaises(ValueError):
            rect.y = -8

    def test_with_correct_types_and_values(self):
        """
        Test with correct types and values pass as arguments or
        set to Rectangle attributes
        """
        rect = Rectangle(2, 3, 4, 5)
        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.height, 3)
        self.assertEqual(rect.x, 4)
        self.assertEqual(rect.y, 5)

        rect.width = 5
        self.assertEqual(rect.width, 5)

        rect.height = 6
        self.assertEqual(rect.height, 6)

        rect.x = 2
        self.assertEqual(rect.x, 2)

        rect.y = 3
        self.assertEqual(rect.y, 3)

    def test_area_method(self):
        """
        Test public method area() in Rectangle class
        """
        rect = Rectangle(2, 4)
        self.assertEqual(rect.area(), 8)

        rect.width = 4
        rect.height = 10
        self.assertEqual(rect.area(), 40)

        rect = Rectangle(6, 2, 0, 0, 21)
        self.assertEqual(rect.area(), 12)

    def test_display_methon(self):
        """
        Test public method display() in Rectangle class
        """
        sys.stdout = StringIO()
        rect = Rectangle(2, 4)
        rect.display()
        output = sys.stdout.getvalue()
        self.assertEqual(output, "##\n##\n##\n##\n")
        sys.stdout = sys.__stdout__

        sys.stdout = StringIO()
        rect.width = 1
        rect.height = 2
        rect.display()
        output = sys.stdout.getvalue()
        self.assertEqual(output, "#\n#\n")
        sys.stdout = sys.__stdout__

        sys.stdout = StringIO()
        rect = Rectangle(3, 4, 0, 0, 22)
        rect.display()
        output = sys.stdout.getvalue()
        self.assertEqual(output, "###\n###\n###\n###\n")
        sys.stdout = sys.__stdout__

        sys.stdout = StringIO()
        rect = Rectangle(2, 3, 2, 2, 3)
        rect.display()
        output = sys.stdout.getvalue()
        self.assertEqual(output, "\n\n  ##\n  ##\n  ##\n")
        sys.stdout = sys.__stdout__

        sys.stdout = StringIO()
        rect.x = 1
        rect.y = 1
        rect.display()
        output = sys.stdout.getvalue()
        self.assertEqual(output, "\n ##\n ##\n ##\n")
        sys.stdout = sys.__stdout__

    def test_str_magic_method(self):
        """
        Test the __str__ magic method in Rectangle class
        """
        rect = Rectangle(3, 4, id=2)
        self.assertEqual(str(rect), "[Rectangle] (2) 0/0 - 3/4")

        rect = Rectangle(3, 4, 4, 5, 3)
        self.assertEqual(str(rect), "[Rectangle] (3) 4/5 - 3/4")

        rect.width = 10
        rect.height = 6
        rect.x = 9
        rect.y = 7
        self.assertEqual(str(rect), "[Rectangle] (3) 9/7 - 10/6")

    def test_update_method_args_with_incorrect_types(self):
        """
        Test the update() public method *args with incorrect types
        in Rectangle class
        """
        rect = Rectangle(3, 4)

        with self.assertRaises(TypeError):
            rect.update(1, "Hello")

        with self.assertRaises(TypeError):
            rect.update(1, 3, [])

        with self.assertRaises(TypeError):
            rect.update(1, 3, 2, (4,))

        with self.assertRaises(TypeError):
            rect.update(1, 3, 2, 4, {"s": 4, "y": 3})

    def test_update_method_args_with_incorrect_values(self):
        """
        Test the update() public method *args with incorrect values
        in Rectangle class
        """
        rect = Rectangle(3, 4)

        with self.assertRaises(ValueError):
            rect.update(1, 0)

        with self.assertRaises(ValueError):
            rect.update(1, 3, -2)

        with self.assertRaises(ValueError):
            rect.update(1, 3, 2, -3)

        with self.assertRaises(ValueError):
            rect.update(1, 3, 2, 4, -9)

    def test_update_method_args_with_correct_values_and_types(self):
        """
        Test the update() public method with correct *args in Rectangle class
        """
        rect = Rectangle(3, 2, 4, 4, 5)

        rect.update(10)
        self.assertEqual(rect.id, 10)

        rect.update(11, 4, 5)
        self.assertEqual(rect.id, 11)
        self.assertEqual(rect.width, 4)
        self.assertEqual(rect.height, 5)

        rect.update(4, 3, 2, 6, 6)
        self.assertEqual(rect.id, 4)
        self.assertEqual(rect.width, 3)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 6)
        self.assertEqual(rect.y, 6)

    def test_update_method_kwargs_with_incorrect_types(self):
        """
        Test update() public method **kwargs with incorrect types
        in Rectangle class
        """
        rect = Rectangle(10, 3, 4, 5, 21)

        with self.assertRaises(TypeError):
            rect.update(width=["string"])

        with self.assertRaises(TypeError):
            rect.update(height=["Hello"])

        with self.assertRaises(TypeError):
            rect.update(x=(3, 5))

        with self.assertRaises(TypeError):
            rect.update(y=[])

    def test_update_method_kwargs_with_incorrect_values(self):
        """
        Test update() public method **kwargs with incorrect values
        in Rectangle class
        """
        rect = Rectangle(10, 3, 4, 5, 21)

        with self.assertRaises(ValueError):
            rect.update(width=0)

        with self.assertRaises(ValueError):
            rect.update(height=0)

        with self.assertRaises(ValueError):
            rect.update(x=-1)

        with self.assertRaises(ValueError):
            rect.update(y=-1)

    def test_update_method_kwargs_with_correct_values_and_types(self):
        """
        Test public methos update() with kwargs with correct values and types
        in Rectangle class
        """
        rect = Rectangle(10, 3, 4, 5, 21)

        rect.update(height=5)
        self.assertEqual(rect.height, 5)

        rect.update(height=3, width=4, y=0, x=1, id=4)
        self.assertEqual(rect.height, 3)
        self.assertEqual(rect.width, 4)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 0)
        self.assertEqual(rect.id, 4)

        rect.update(3, 4, height=6, y=1, x=0)
        self.assertEqual(rect.height, 3)
        self.assertEqual(rect.width, 4)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 0)
        self.assertEqual(rect.id, 3)

    def test_to_dictionary_method(self):
        """
        Test the to_dictionary public method in Rectangle class
        """
        rect = Rectangle(3, 4, 0, 0, 77)
        dictionary = rect.to_dictionary()

        self.assertIsInstance(dictionary, dict)

        self.assertIn("id", dictionary)
        self.assertIn("width", dictionary)
        self.assertIn("height", dictionary)
        self.assertIn("x", dictionary)
        self.assertIn("y", dictionary)

        self.assertEqual(dictionary["id"], 77)
        self.assertEqual(dictionary["width"], 3)
        self.assertEqual(dictionary["height"], 4)
        self.assertEqual(dictionary["x"], 0)
        self.assertEqual(dictionary["y"], 0)
