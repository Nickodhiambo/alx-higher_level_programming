#!/usr/bin/python3
"""Defines unittests for the Rectangle subclass"""
from models.base import Base
from models.rectangle import Rectangle
import unittest
import sys
import io

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
            Rectangle({"a": 1, "b": 2}, 1)

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

    def test_bytes_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(b'Python', 2)

    def test_bytearray_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(bytearray(b'abcdefg'), 2)

    def test_memoryview_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(memoryview(b'abcedfg'), 2)


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
            Rectangle(1, {"a": 1, "b": 2})

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

    def test_bytes_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, b'Python')

    def test_bytearray_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, bytearray(b'abcdefg'))

    def test_memoryview_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, memoryview(b'abcedfg'))


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
            Rectangle(1, 2, {"a": 1, "b": 2})

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

    def test_bytes_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, b'Python')

    def test_bytearray_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, bytearray(b'abcdefg'))

    def test_memoryview_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, memoryview(b'abcedfg'))


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
            Rectangle(1, 2, 3, {"a": 1, "b": 2})

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

    def test_bytes_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, b'Python')

    def test_bytearray_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, bytearray(b'abcdefg'))

    def test_memoryview_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, memoryview(b'abcedfg'))


class TestInitializationOrder(unittest.TestCase):
    """Checks attributes are initialized in correct order"""
    def test_width_before_height(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("2", "3")

    def test_width_before_X(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 1, "1")

    def test_width_before_Y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(10), 1, 2, -1)

    def test_height_before_X(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "5", -1, 2)

    def test_height_before_Y(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -2, 3, -4)

    def test_X_before_Y(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 2, -3, -4)


class TestUpdateArgs(unittest.TestCase):
    """Tests the args parameter of the update method of rectangle class"""
    def test_update_zero_args(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update()
        self.assertEqual("[Rectangle] (1) 1/1 - 1/1", str(r))

    def test_update_one_arg(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(10)
        self.assertEqual("[Rectangle] (10) 1/1 - 1/1", str(r))

    def test_update_two_args(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(10, 2)
        self.assertEqual("[Rectangle] (10) 1/1 - 2/1", str(r))

    def test_update_three_args(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(10, 2, 3)
        self.assertEqual("[Rectangle] (10) 1/1 - 2/3", str(r))

    def test_update_four_args(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(10, 2, 3, 4)
        self.assertEqual("[Rectangle] (10) 4/1 - 2/3", str(r))

    def test_update_five_args(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(10, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (10) 4/5 - 2/3", str(r))

    def test_update_more_than_five(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(10, 2, 3, 4, 5, 6,)
        self.assertEqual("[Rectangle] (10) 4/5 - 2/3", str(r))

    def test_id_as_none(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(None)
        self.assertEqual("[Rectangle] ({}) 1/1 - 1/1".format(r.id), str(r))

    def test_id_as_none_more_args(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(None, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] ({}) 4/5 - 2/3".format(r.id), str(r))

    def test_two_instances(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(10, 10, 10, 10, 10)
        r.update(10, 20, 30, 40, 50)
        self.assertEqual("[Rectangle] (10) 40/50 - 20/30", str(r))

    def test_update_invalid_width_type(self):
        r = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(2, "width")

    def test_update_zero_width_value(self):
        r = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(98, 0)

    def test_update_negative_width(self):
        r = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(98, -1)

    def test_update_invalid_height_type(self):
        r = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(2, 3, "height")

    def test_update_zero_height_value(self):
        r = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(98, 1, 0)

    def test_update_negative_height(self):
        r = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(98, 1, -1)

    def test_update_invalid_X_type(self):
        r = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(2, 3, 4, "x")

    def test_update_negative_X(self):
        r = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(98, 1, 2, -1)

    def test_update_invalid_Y_type(self):
        r = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(2, 3, 4, 5, "y")

    def test_update_negative_Y(self):
        r = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(98, 1, 2, 3, -10)

    def test_update_width_then_height(self):
        r = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(98, "width", "height")

    def test_update_width_then_x(self):
        r = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(98, "width", 1, "x")

    def test_update_width_then_y(self):
        r = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(98, "width", 1, 2, "y")

    def test_height_then_x(self):
        r = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(98, 1, "height", "x")

    def test_height_then_y(self):
        r = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(98, 1, "height", 2, "y")

    def test_x_then_y(self):
        r = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(98, 1, 2, "x", "y")


class TestUpdateKwargs(unittest.TestCase):
    """unittests for the kwargs parameter of rect update method"""
    def test_one_kwarg(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(id=98)
        self.assertEqual("[Rectangle] (98) 1/1 - 1/1", str(r))

    def test_two_kwargs(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(width=2, id=98)
        self.assertEqual("[Rectangle] (98) 1/1 - 2/1", str(r))

    def test_three_kwargs(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(height=3, id=98, width=2)
        self.assertEqual("[Rectangle] (98) 1/1 - 2/3", str(r))

    def test_four_kwargs(self):
        r = Rectangle(1, 1, 1, 1, 10)
        r.update(id=98, x=4, width=2, height=3)
        self.assertEqual("[Rectangle] (98) 4/1 - 2/3", str(r))

    def test_five_kwargs(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(y=5, x=4, height=3, width=2, id=1)
        self.assertEqual("[Rectangle] (1) 4/5 - 2/3", str(r))

    def test_kwargs_id_none(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(id=None)
        self.assertEqual("[Rectangle] ({}) 1/1 - 1/1".format(r.id), str(r))

    def test_kwargs_id_none_more_args(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(id=None, width=2, height=7)
        self.assertEqual("[Rectangle] ({}) 1/1 - 2/7".format(r.id), str(r))

    def test_kwargs_two_instantiations(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(id=98, y=20, height=4)
        r.update(id=89, x=10, width=6)
        self.assertEqual("[Rectangle] (89) 10/20 - 6/4", str(r))

    def test_kwargs_invalid_width_type(self):
        r = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(width="width")

    def test_kwargs_zero_width(self):
        r = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=0)

    def test_kwargs_negative_width(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=-5)

    def test_kwargs_invalid_height_type(self):
        r = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(height="height")

    def test_kwargs_zero_height(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=0)

    def test_kwargs_negative_height(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=-10)

    def test_kwargs_invalid_x_type(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(x="x")

    def test_kwargs_negative_x(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(x=-1)

    def test_kwargs_invalid_y_type(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(y="y")

    def test_kwargs_negative_y_type(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(y=-2)

    def test_args_kwargs_combo(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(89, 5, height=4, x=2)
        self.assertEqual("[Rectangle] (89) 1/1 - 5/1", str(r))

    def test_kwargs_all_wrong_keys(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(i=10, j=20, k=30, l=40, m=50)
        self.assertEqual("[Rectangle] (1) 1/1 - 1/1", str(r))

    def test_kwargs_some_wrong_keys(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(id=100, i=2, j=3, width=5, y=6)
        self.assertEqual("[Rectangle] (100) 1/6 - 5/1", str(r))


class TestDictRep(unittest.TestCase):
    """unittests for rect method that returns dict representation of rect"""
    def test_correct_dict_output(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        dict_output = {"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}
        self.assertDictEqual(dict_output, rect.to_dictionary())

    def test_pass_arg_to_method(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            rect.to_dictionary(1)

class Test_Str_Disp_Methods:
    """Unittests for str and display methods of rectangle class"""

    @staticmethod
    def print_to_stdout(rect, cmd):
        disp = io.StringIO()

        if cmd == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return disp
    
    # Test __str__ method
    def test_print_width_height(self):
        r = Rectangle(1, 2)
        disp = Test_Str_Disp_Methods.print_to_stdout_stdout(r, "print")
        fmt = "[Rectangle] ({}) 0/0 - 4/6\n".format(r.id)
        self.assertEqual(fmt, disp.getvalue())

    def test_print_width_height_x(self):
        r = Rectangle(1, 2, 3)
        fmt = "[Rectangle] ({}) 3/0 - 1/2".format(r.id)
        self.assertEqual(fmt, r.__str__())

    def test_print_width_height_x_y(self):
        r = Rectangle(1, 2, 3, 4)
        fmt = "[Rectangle] ({}) 3/4 - 1/2".format(r.id)
        self.assertEqual(fmt, str(r))

    def test_print_width_height_x_y_id(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (5) 4/5 - 1/2", str(r))

    def test_print_with_changed_attributes(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.width = 6
        r.height = 7
        r.x = 8
        r.y = 9
        self.assertEqual("[Rectangle] (4) 8/9 - 6/7", str(r))

    def test_str_method_one_arg_passed(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r.__str__(10)

    # Test display method
    def test_disp_width_height(self):
        rect = Rectangle(1, 2, 0, 0, 0)
        disp = Test_Str_Disp_Methods.print_to_stdout(rect, "display")
        self.assertEqual("#\n#\n", disp.getvalue())

    def test_display_width_height_x(self):
        r = Rectangle(1, 2, 1, 0, 0)
        disp = Test_Str_Disp_Methods.print_to_stdout(r, "display")
        self.assertEqual(" #\n #\n", disp.getvalue())

    def test_display_width_height_y(self):
        r = Rectangle(2, 3, 0, 1, 1)
        disp = Test_Str_Disp_Methods.print_to_stdout(r, "display")
        display = "\n##\n##\n##"
        self.assertEqual(display, disp.getvalue())

    def test_display_width_height_x_y(self):
        r = Rectangle(2, 3, 2, 2, 1)
        disp = Test_Str_Disp_Methods.print_to_stdout(r, "display")
        display = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(display, disp.getvalue())

    def test_display_one_arg(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r.display(10)
