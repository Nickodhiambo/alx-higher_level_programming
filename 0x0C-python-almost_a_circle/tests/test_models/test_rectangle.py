#!/usr/bin/python3
"""Defines unittests for the Rectangle subclass"""
from models.base import Base
from models.rectangle import Rectangle
import unittest


class TestRectangleInstantiation(unittest.TestCase):
    """Defines unittests for Rectangle class"""
    def test_is_base_subclass(self):
        self.assertIsInstance(Rectangle(1, 1), Base)

    def test_rect_inst_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_rect_inst_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_rect_inst_two_args(self):
        rect1 = Rectangle(1, 1)
        rect2 = Rectangle(2, 3)
        self.assertEqual(rect2.id, (rect1.id + 1))

    def test_rect_inst_three_args(self):
        rect1 = Rectangle(1, 2, 3)
        rect2 = Rectangle(3, 4, 5)
        self.assertEqual(rect2.id, (rect1.id + 1))

    def test_rect_inst_four_args(self):
        rect1 = Rectangle(1, 2, 3, 4)
        rect2 = Rectangle(4, 5, 6, 7)
        self.assertEqual(rect2.id, (rect1.id + 1))

    def test_rect_inst_five_args(self):
        self.assertEqual(10, Rectangle(6, 7, 8, 9, 10).id)

    def test_rect_inst_more_than_five(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_if_width_is_private(self):
        with self.assertRaises(AttributeError):
            Rectangle((1, 1).__width)

    def test_if_height_is_private(self):
        with self.assertRaises(AttributeError):
            Rectangle((1, 1).__height)

    def test_if_x_is_private(self):
        with self.assertRaises(AttributeError):
            Rectangle((1, 2, 3).__x)

    def test_if_y_is_private(self):
        with self.assertRaises(AttributeError):
            Rectangle((1, 2, 3, 4).__y)

    def test_width_getter(self):
        rect = Rectangle(1, 2)
        self.assertEqual(1, rect.width)

    def test_width_setter(self):
        rect = Rectangle(1, 2)
        rect.width = 3
        self.assertEqual(3, rect.width)

    def test_height_getter(self):
        rect = Rectangle(1, 2)
        self.assertEqual(2, rect.height)

    def test_height_setter(self):
        rect = Rectangle(1, 2)
        rect.height = 4
        self.assertEqual(4, rect.height)

    def test_x_getter(self):
        rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(3, rect.x)

    def test_x_setter(self):
        rect = Rectangle(1, 2, 3, 4)
        rect.x = 4
        self.assertEqual(4, rect.x)

    def test_y_getter(self):
        rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(4, rect.y)

    def test_y_setter(self):
        rect = Rectangle(1, 2, 3, 4)
        rect.y = 5
        self.assertEqual(5, rect.y)

class TestArea(unittest.TestCase):
    """Area unittests"""
    def test_small_dimensions(self):
        r = Rectangle(1, 1)
        self.assertEqual(1, r.area())

    def test_large_dimensions(self):
        r = Rectangle(1000000, 1000000)
        self.assertEqual(1000000000000, r.area())

    def test_changed_dimensions(self):
        r = Rectangle(1, 2)
        r.width = 10
        r.height = 10
        self.assertEqual(100, r.area())

    def test_area_one_arg_passed(self):
        r = Rectangle(1, 1)
        with self.assertRaises(TypeError):
            r.area(1)

class TestValidateWidth(unittest.TestCase):
    """Checks if width input is of correct type and value"""
    def test_none_as_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 1)

    def test_str_as_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("str", 1)

    def test_float_as_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(1.1, 1)

    def test_list_as_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 1)

    def test_dict_as_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"a":1, "b":2}, 1)

    def test_boolean_as_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 1)

    def test_complex_as_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(1), 1)

    def test_tuple_as_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 1, 1), 1)

    def test_set_as_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2, 3}, 1)

    def test_frozenset_as_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({1, 2, 3, 1}), 1)

    def test_range_as_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(1), 1)

    def test_inf_as_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 1)

    def test_nan_as_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 1)

    def test_zero_as_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 1)

    def test_negative_as_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 1)


class TestValidateHeight(unittest.TestCase):
    """Checks if height input is of corrct type and value"""
    def test_none_as_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, None)

    def test_str_as_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "str")

    def test_float_as_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 1.1)

    def test_list_as_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, [1, 2, 3])

    def test_dict_as_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {"a":1, "b":2})

    def test_boolean_as_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, True)

    def test_complex_as_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, complex(1))

    def test_tuple_as_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, (1, 1, 1))

    def test_set_as_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {1, 2, 3})

    def test_frozenset_as_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, frozenset({1, 2, 3, 1}))

    def test_range_as_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, range(1))

    def test_inf_as_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, float('inf'))

    def test_nan_as_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, float('nan'))

    def test_zero_as_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)

    def test_negative_as_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -1)

class TestValidate_X(unittest.TestCase):
    """Checks if inputted x is of correct type and value"""
    def test_none_as_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, None)

    def test_str_as_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "str")

    def test_float_as_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, 3.1)

    def test_list_as_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, [1, 2, 3])

    def test_dict_as_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {"a":1, "b":2})

    def test_boolean_as_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, True)

    def test_complex_as_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, complex(1))

    def test_tuple_as_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, (1, 1, 1))

    def test_set_as_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {1, 2, 3})

    def test_frozenset_as_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, frozenset({1, 2, 3, 1}))

    def test_range_as_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, range(1))

    def test_inf_as_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, float('inf'))

    def test_nan_as_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, float('nan'))

    def test_negative_as_X(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 2, -3)


class TestValidate_Y(unittest.TestCase):
    """Checks if inputted y is of correct type and value"""
    def test_none_as_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, None)

    def test_str_as_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, "str")

    def test_float_as_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, 4.1)

    def test_list_as_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, [1, 2, 3])

    def test_dict_as_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, {"a":1, "b":2})

    def test_boolean_as_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, True)

    def test_complex_as_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, complex(1))

    def test_tuple_as_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, (1, 1, 1))

    def test_set_as_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, {1, 2, 3})

    def test_frozenset_as_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, frozenset({1, 2, 3, 1}))

    def test_range_as_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, range(1))

    def test_inf_as_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, float('inf'))

    def test_nan_as_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, float('nan'))

    def test_negative_as_Y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 2, 3, -4)
