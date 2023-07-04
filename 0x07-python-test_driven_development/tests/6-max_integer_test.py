#!/usr/bin/python3
"""This module contains several tests that check for the largest
integer in a list of integers"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """contains several unittest for max integer in list"""
    def test_ordered_list(self):
        """Checks for max int in an ordered list"""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Checks for max int in an unordered list"""
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_empty_list(self):
        """Checks for max int in an empty list"""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_floats_list(self):
        """Checks for max int in a list of floats"""
        floats = [1.2, 2.4, 4.6, 8.1, -10.22]
        self.assertEqual(max_integer(floats), 8.1)

    def test_floats_ints_list(self):
        """Finds max num in a list of floats and ints"""
        floats_and_ints = [1, 2.4, 5, 6.6]
        self.assertEqual(max_integer(floats_and_ints), 6.6)

    def test_list_of_strings(self):
        """Tests a list containing strings only"""
        list_of_strings = ["Hello", "World"]
        self.assertEqual(max_integer(list_of_strings), "World")
