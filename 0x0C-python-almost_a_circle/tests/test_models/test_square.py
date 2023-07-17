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

class TestInitializationOrder(unittest.TestCase):
    """Tests the order of initialization of square attributes"""
    def size_then_x(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, "x")

    def size_then_y(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1, "y")

    def x_then_y(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(2, -3, "y")

class TestArea(unittest.TestCase):
    """Tests various computation options for area of square"""
    def test_small_dimensions(self):
        sq = Square(1)
        self.assertEqual(1, sq.area())

    def test_large_dimensions(self):
        sq = Square(1000000)
        self.assertEqual(1000000000000, sq.area())

    def test_changed_attributes(self):
        sq = Square(10, 2, 3, 98)
        sq.size = 100
        self.assertEqual(10000, sq.area())

    def test_extra_arg_to_area(self):
        sq = Square(10, 20, 30, 40)
        with self.assertRaises(TypeError):
            sq.area(50)

class TestUpdateArgs(unittest.TestCase):
    """Tests the args parameter of the update method of square class"""
    def test_update_zero_args(self):
        sq = Square(1, 1, 1, 1)
        sq.update()
        self.assertEqual("[Square] (1) 1/1 - 1", str(sq))

    def test_update_one_arg(self):
        sq = Square(1, 1, 1, 1)
        sq.update(10)
        self.assertEqual("[Square] (10) 1/1 - 1", str(sq))

    def test_update_two_args(self):
        sq = Square(1, 1, 1, 1)
        sq.update(10, 2)
        self.assertEqual("[Square] (10) 1/1 - 2", str(sq))

    def test_update_three_args(self):
        sq = Square(1, 1, 1, 1)
        sq.update(10, 2, 3)
        self.assertEqual("[Square] (10) 3/1 - 2", str(sq))

    def test_update_four_args(self):
        sq = Square(1, 1, 1, 1)
        sq.update(10, 2, 3, 4)
        self.assertEqual("[Square] (10) 3/4 - 2", str(sq))

    def test_update_more_than_four(self):
        sq = Square(1, 1, 1, 1)
        sq.update(10, 2, 3, 4, 5)
        self.assertEqual("[Square] (10) 3/4 - 2", str(sq))

    def test_id_as_none(self):
        sq = Square(1, 1, 1, 1)
        sq.update(None)
        self.assertEqual("[Square] ({}) 1/1 - 1".format(sq.id), str(sq))

    def test_id_as_none_more_args(self):
        sq = Square(1, 1, 1, 1)
        sq.update(None, 2, 3, 4)
        self.assertEqual("[Square] ({}) 3/4 - 2".format(sq.id), str(sq))

    def test_two_instances(self):
        sq = Square(1, 1, 1, 1)
        sq.update(10, 10, 10, 10)
        sq.update(10, 20, 30, 40)
        self.assertEqual("[Square] (10) 30/40 - 20", str(sq))

    def test_update_invalid_size_type(self):
        sq = Square(1, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq.update(2, "size")

    def test_update_zero_size_value(self):
        sq = Square(1, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sq.update(98, 0)

    def test_update_negative_size(self):
        sq = Square(1, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sq.update(98, -1)

    def test_update_invalid_X_type(self):
        sq = Square(1, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sq.update(2, 3, "x")

    def test_update_negative_X(self):
        sq = Square(1, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            sq.update(98, 1, -1)

    def test_update_invalid_Y_type(self):
        sq = Square(1, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            sq.update(2, 3, 4, "y")

    def test_update_negative_Y(self):
        sq = Square(1, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            sq.update(98, 1, 2, -10)

    def test_update_size_then_x(self):
        sq = Square(1, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq.update(98, "size", "x")

    def test_update_size_then_y(self):
        sq = Square(1, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq.update(98, "size", 1, "y")

    def test_x_then_y(self):
        sq = Square(1, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sq.update(98, 1, "x", "y")
