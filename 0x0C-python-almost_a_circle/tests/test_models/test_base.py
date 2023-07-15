#!/usr/bin/python3
"""Defines unittests for base.py module"""
import unittest
from models.base import Base


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
