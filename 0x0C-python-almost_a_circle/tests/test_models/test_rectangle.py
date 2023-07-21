#!/usr/bin/python3
""" This module defines a test class for the Rectangle class """
import unittest
from models.rectangle import Rectangle
from os.path import isfile


class TestRectangle(unittest.TestCase):

    def test_width_from_valid_values_with_id(self):
        rect = Rectangle(10, 5, 1, 1, 10)
        self.assertEqual(10, rect.width)

    def test_height_from_valid_values_with_id(self):
        rect = Rectangle(10, 5, 1, 1, 10)
        self.assertEqual(5, rect.height)

    def test_x_from_valid_values_with_id(self):
        rect = Rectangle(10, 5, 1, 1, 10)
        self.assertEqual(1, rect.x)

    def test_y_from_valid_values_with_id(self):
        rect = Rectangle(10, 5, 1, 1, 10)
        self.assertEqual(1, rect.y)

    def test_id_from_valid_values_with_id(self):
        rect = Rectangle(10, 5, 1, 1, 10)
        self.assertEqual(10, rect.id)

    def test_width_from_invalid_type(self):
        with self.assertRaises(TypeError):
            rect = Rectangle("10", 5, 1, 1, 10)

    def test_height_from_invalid_type(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(10, "5", 1, 1, 10)

    def test_x_from_invalid_x(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(10, 5, "1", 1, 10)

    def test_y_from_invalid_y(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(10, 5, 1, "1", 10)

    def test_id_without_obj_id(self):
        rect = Rectangle(10, 5, 1, 1)
        self.assertEqual(14, rect.id)

    def test_width_from_invalid_value(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(-10, 5, 1, 1, 10)

    def test_width_from_zero_value(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(0, 5, 1, 1, 1)

    def test_height_from_zero_value(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(10, 0, 1, 1, 10)

    def test_height_from_negative_value(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(10, -1)

    def test_x_from_invalid_value(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(10, 5, -1, 1, 10)

    def test_y_from_invalid_value(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(10, 5, 1, -1, 10)

    def test_one_positional_arg_provided(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(10)

    def test_no_positional_arg_provided(self):
        with self.assertRaises(TypeError):
            rect = Rectangle()

    def test_area(self):
        rect = Rectangle(10, 5, 1, 1, 10)
        self.assertEqual(50, rect.area())

    def test_display_nno_padding(self):
        rect = Rectangle(1, 1, 0, 0, 10)
        self.assertTrue(rect.display())

    def test_magic_str_with_valid_values(self):
        rect = Rectangle(10, 5, 1, 1, 10)
        self.assertEqual("[Rectangle] (10) 1/1 - 10/5", str(rect))

    def test_magic_str_without_axis_nor_id(self):
        rect = Rectangle(10, 5)
        self.assertEqual("[Rectangle] (15) 0/0 - 10/5", str(rect))

    def test_magic_str_without_id(self):
        rect = Rectangle(10, 5, 1, 1)
        self.assertEqual("[Rectangle] (16) 1/1 - 10/5", str(rect))

    def test_display_with_padding(self):
        rect = Rectangle(1, 1, 1, 1, 10)
        self.assertTrue(rect.display())

    def test_update_with_one_arg(self):
        rect = Rectangle(10, 10, 10, 10)
        rect.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(rect))

    def test_update_with_two_args(self):
        rect = Rectangle(10, 10, 10, 10)
        rect.update(89, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(rect))

    def test_update_with_three_args(self):
        rect = Rectangle(10, 10, 10, 10)
        rect.update(89, 2, 3)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(rect))

    def test_update_with_four_args(self):
        rect = Rectangle(10, 10, 10, 10)
        rect.update(89, 2, 3, 4)
        self.assertEqual("[Rectangle] (89) 4/10 - 2/3", str(rect))

    def test_update_with_five_args(self):
        rect = Rectangle(10, 10, 10, 10)
        rect.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(rect))

    def test_update_with_one_args_and_kwargs(self):
        rect = Rectangle(10, 10, 10, 10)
        rect.update(5, width=990)
        self.assertEqual("[Rectangle] (5) 10/10 - 10/10", str(rect))

    def test_update_with_empty_args_and_one_kwargs(self):
        rect = Rectangle(10, 10, 10, 10)
        rect.update((), width=990)
        self.assertEqual("[Rectangle] (20) 10/10 - 990/10", str(rect))

    def test_update_with_empty_args_and_two_kwargs(self):
        rect = Rectangle(10, 10, 10, 10)
        rect.update((), width=990, id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 990/10", str(rect))

    def test_update_with_two_args_and_one_kwargs(self):
        rect = Rectangle(10, 10, 10, 10)
        rect.update(4, 5, width=990)
        self.assertEqual("[Rectangle] (4) 10/10 - 5/10", str(rect))

    def test_update_with_all_args_and_all_kwargs(self):
        rect = Rectangle(10, 10, 10, 10)
        rect.update(1, 1, 1, 1, 1, id=19, width=19, height=19, x=19, y=19)
        self.assertEqual("[Rectangle] (1) 1/1 - 1/1", str(rect))

    def test_to_dictionary_with_all_attributes_present(self):
        rect = Rectangle(10, 2, 1, 1, 1)
        actual = rect.to_dictionary()
        self.assertEqual({"id": 1, "width": 10, "height": 2, "x": 1,
                         "y": 1}, actual)

    def test_to_dictionary_with_only_width_and_height_specified(self):
        rect = Rectangle(10, 2)
        actual = rect.to_dictionary()
        self.assertEqual({"id": 18, "width": 10, "height": 2, "x": 0,
                         "y": 0}, actual)

    def test_to_dictionary_with_no_id_specified(self):
        rect = Rectangle(10, 2, 9, 9)
        actual = rect.to_dictionary()
        self.assertEqual({"id": 17, "width": 10, "height": 2, "x": 9,
                         "y": 9}, actual)

    def test_save_to_file_with_none(self):
        output = Rectangle.save_to_file(None)
        self.assertEqual("[]", output)

    def test_save_to_file_with_empty_list(self):
        output = Rectangle.save_to_file([])
        self.assertEqual("[]", output)
