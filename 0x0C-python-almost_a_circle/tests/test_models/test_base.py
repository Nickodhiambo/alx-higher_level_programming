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

class TestJsonSerialization(unittest.TestCase):
    """Unittests for serializing json data format"""
    #Rectangle
    def test_to_json_string_common_case(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_to_json_string_one_dict(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 53)

    def test_to_json_string_two_dicts(self):
        r1 = Rectangle(2, 3, 5, 19, 2)
        r2 = Rectangle(4, 2, 4, 1, 12)
        list_of_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)

    #Square
    def test_to_json_string_common_case(self):
        s = Square(1, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_to_json_string_one_dict(self):
        s = Square(10, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([s.to_dictionary()])) == 39)

    def test_to_json_string_two_dicts(self):
        s1 = Square(10, 2, 3, 4)
        s2 = Square(4, 5, 21, 2)
        list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)

    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_zero_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)
