#!/usr/bin/python3
"""Defines unittests for base.py module"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestBaseInstances(unittest.TestCase):
    """Tests different instantiations of the Base class defined
    in base.py module
    """
    def test_no_args_instances(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, (b1.id + 1))

    def test_three_no_args_instances(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b3.id, (b1.id + 2))

    def test_none_as_arg(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b2.id, (b1.id + 1))

    def test_specified_id_instance(self):
        b1 = Base(12)
        self.assertEqual(12, b1.id)

    def test_specified_id_no_args_combo(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b3.id, (b1.id + 1))

    def test_specified_id_none_as_arg_combo(self):
        b1 = Base(None)
        b2 = Base(12)
        b3 = Base(None)
        self.assertEqual(b3.id, (b1.id + 1))

    def test_if_id_is_public(self):
        b1 = Base(12)
        b1.id = 13
        self.assertEqual(13, b1.id)

    def test_if_nb_objects_is_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_objects)

    def test_str_id(self):
        self.assertEqual("hello", Base("hello").id)

    def test_float_id(self):
        self.assertEqual(5.5, Base(5.5).id)

    def test_complex_id(self):
        self.assertEqual(complex(5), Base(complex(5)).id)

    def test_dict_id(self):
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def test_bool_id(self):
        self.assertEqual(True, Base(True).id)

    def test_list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_tuple_id(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_frozenset_id(self):
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)

    def test_range_id(self):
        self.assertEqual(range(5), Base(range(5)).id)

    def test_bytes_id(self):
        self.assertEqual(b'Python', Base(b'Python').id)

    def test_bytearray_id(self):
        self.assertEqual(bytearray(b'abcefg'), Base(bytearray(b'abcefg')).id)

    def test_memoryview_id(self):
        self.assertEqual(memoryview(b'abcefg'), Base(memoryview(b'abcefg')).id)

    def test_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)

if __name__ == "__main__":
    unittest.main()
