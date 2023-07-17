#!/usr/bin/python3
"""Unittests for square subclass"""
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest


class TestSquareInstantiations(unittest.TestCase):
    """Tests various instantiations of square model"""
    def test_is_base_subclass(self):
        self.assertIsInstance(Square(1), Base)

    def test_is_rect_subclass(self):
        self.assertIsInstance(Square(1), Rectangle)

    def test_square_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_square_one_arg(self):
        sq1 = Square(1)
        sq2 = Square(2)
        self.assertEqual(sq2.id, (sq1.id + 1))

    def test_square_two_args(self):
        sq1 = Square(1, 2)
        sq2 = Square(3, 4)
        self.assertEqual(sq2.id, (sq1.id + 1))

    def test_square_three_args(self):
        sq1 = Square(1, 2, 3)
        sq2 = Square(4, 5, 6)
        self.assertEqual(sq2.id, (sq1.id + 1))

    def test_square_four_args(self):
        sq = Square(7, 8, 9, 10)
        self.assertEqual(10, sq.id)

    def test_more_than_four(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_if_size_is_private(self):
        with self.assertRaises(AttributeError):
            print(Square(1, 1, 1, 1).__size)

    def test_size_getter(self):
        self.assertEqual(1, Square(1, 2, 3, 4).size)

    def test_size_setter(self):
        sq = Square(1)
        sq.size = 2
        self.assertEqual(2, sq.size)

    def test_width_getter(self):
        self.assertEqual(3, Square(3).width)

    def test_height_getter(self):
        self.assertEqual(4, Square(4).height)

    def test_x_getter(self):
        self.assertEqual(0, Square(1).x)

    def test_y_getter(self):
        self.assertEqual(0, Square(1).y)


class TestValidateSize(unittest.TestCase):
    """Checks if size input is of correct type and value"""
    def test_none_as_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_str_as_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("str")

    def test_float_as_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(1.1)

    def test_list_as_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1, 2, 3])

    def test_dict_as_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"a":1, "b":2})

    def test_boolean_as_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True)

    def test_complex_as_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(complex(1))

    def test_tuple_as_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 1, 1))

    def test_set_as_Square(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1, 2, 3})

    def test_frozenset_as_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(frozenset({1, 2, 3, 1}))

    def test_range_as_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(range(1))

    def test_inf_as_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('inf'))

    def test_negative_as_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)

    def test_size_as_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)


class TestValidate_X(unittest.TestCase):
    """Checks if inputted x is of correct type and value"""
    def test_none_as_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, None)

    def test_str_as_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "str")

    def test_float_as_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, 3.1)

    def test_list_as_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, [1, 2, 3])

    def test_dict_as_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {"a":1, "b":2})

    def test_boolean_as_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, True)

    def test_complex_as_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, complex(1))

    def test_tuple_as_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, (1, 1, 1))

    def test_set_as_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {1, 2, 3})

    def test_frozenset_as_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, frozenset({1, 2, 3, 1}))

    def test_range_as_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, range(1))

    def test_inf_as_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, float('inf'))

    def test_nan_as_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, float('nan'))

    def test_negative_as_X(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -3)

class TestValidate_Y(unittest.TestCase):
    """Checks if inputted y is of correct type and value"""
    def test_none_as_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, None)

    def test_str_as_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "str")

    def test_float_as_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, 4.1)

    def test_list_as_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, [1, 2, 3])

    def test_dict_as_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, {"a":1, "b":2})

    def test_boolean_as_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, True)

    def test_complex_as_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, complex(1))

    def test_tuple_as_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, (1, 1, 1))

    def test_set_as_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, {1, 2, 3})

    def test_frozenset_as_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, frozenset({1, 2, 3, 1}))

    def test_range_as_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, range(1))

    def test_inf_as_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, float('inf'))

    def test_nan_as_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, float('nan'))

    def test_negative_as_Y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 2, -4)
