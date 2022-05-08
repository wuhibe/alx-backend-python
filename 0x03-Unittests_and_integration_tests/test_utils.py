#!/usr/bin/env python3
""" module to test utils """
import unittest
from unittest.mock import patch
from parameterized import parameterized
import utils


class TestAccessNestedMap(unittest.TestCase):
    """ Test class for access nested map method """
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


class TestGetJson(unittest.TestCase):
    """ Test class for get_json method """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.get_json')
    def test_get_json(self, url, payload, patch):
        """ test for get method with patched return """
        patch.return_value = payload
        self.assertEqual(utils.get_json(url), payload)
