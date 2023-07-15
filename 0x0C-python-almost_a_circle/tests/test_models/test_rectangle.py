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
