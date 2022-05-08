#!/usr/bin/env python3
""" module to test utils """
import unittest
from parameterized import parameterized
import utils


class TestAccessNestedMap(unittest.TestCase):
    """ Class for access nested map class """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, result):
        """ test for access nested map method """
        self.assertEqual(utils.access_nested_map(nested_map, path), result)
    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ test for raise exception """
        with self.assertRaises(KeyError):
            utils.access_nested_map(nested_map, path)
