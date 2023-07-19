#!/usr/bin/python3
""" This module defines a test class for the Base class """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):

    def test_single_obj_with_id(self):
        base = Base(10)
        self.assertEqual(10, base.id)

    def test_single_obj_without_id(self):
        base = Base()
        self.assertEqual(7, base.id)

    def test_two_obj_with_id(self):
        base = Base(10)
        base2 = Base(5)
        self.assertEqual(5, base2.id)

    def test_two_obj_with_first_id(self):
        base = Base(5)
        base2 = Base()
        self.assertEqual(9, base2.id)

    def test_two_obj_with_second_id(self):
        base = Base()
        base2 = Base(3)
        self.assertEqual(3, base2.id)

    def test_two_obj_without_ids(self):
        base = Base()
        base2 = Base()
        self.assertEqual(12, base2.id)

    def test_single_obj_with_neg_id(self):
        base = Base(-5)
        self.assertEqual(-5, base.id)

    def test_two_obj_with_neg_ids(self):
        base = Base(-1)
        base2 = Base(-2)
        self.assertEqual(-2, base2.id)

    def test_to_json_string_with_valid_dictionary(self):
        rect = Rectangle(10, 7, 2, 8, 1)
        dictionary = rect.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(sorted('[{"x": 2, "width": 10, "id": 1, "height": 7'
                                ', "y": 8}]'), sorted(json_dictionary))

    def test_to_json_string_with_argument_none(self):
        json_string = Base.to_json_string(None)
        self.assertEqual("[]", json_string)

    def test_to_json_string_with_empty_dictionary(self):
        json_string = Base.to_json_string({})
        self.assertEqual("[]", json_string)

    def test_from_json_string_from_valid_string(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_str = Rectangle.to_json_string(list_input)
        output = Rectangle.from_json_string(json_str)
        self.assertEqual(list_input, output)

    def test_from_json_string_from_none(self):
        output = Rectangle.from_json_string(None)
        self.assertEqual([], output)

    def test_from_json_string_from_empty(self):
        output = Rectangle.from_json_string("")
        self.assertEqual([], output)

    def test_create_rectangle(self):
        rect = Rectangle(3, 5, 1, 1)
        obj_dict = rect.to_dictionary()
        rect2 = Rectangle.create(**obj_dict)
        self.assertEqual("[Rectangle] (1) 1/1 - 3/5", str(rect2))

    def test_create_square(self):
        square = Square(3, 5, 1, 1)
        obj_dict = square.to_dictionary()
        square2 = Square.create(**obj_dict)
        self.assertEqual("[Square] (1) 5/1 - 3", str(square2))

    def test_rectangle_load_from_file(self):
        Rectangle.save_to_file([Rectangle(10, 7, 2, 8, 1), Rectangle(2, 4)])
        actual = Rectangle.load_from_file()
        self.assertEqual(2, len(actual))

    def test_square_load_from_file(self):
        Square.save_to_file([Square(5, 1, 1, 1)])
        actual = Square.load_from_file()
        self.assertEqual(1, len(actual))

    def test_save_to_file_with_none(self):
        text = ""
        Square.save_to_file(None)
        with open("Square.json") as file:
            text = file.read()
        self.assertEqual("[]", text)

    def test_save_to_file_with_empty_list(self):
        with self.assertRaises(ValueError):
            Square.save_to_file([])