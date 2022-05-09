#!/usr/bin/env python3
""" module to test client """
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ class to test GithubOrgClient """
    @parameterized.expand([
        ("google", {"payload": True}),
        ("abc", {"payload": False}),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, return_val, patch):
        """ test the correct return of org method """
        patch.return_value = return_val
        goc = GithubOrgClient(org_name)
        test_return = goc.org
        self.assertEqual(test_return, patch.return_value)
        patch.assert_called_once
