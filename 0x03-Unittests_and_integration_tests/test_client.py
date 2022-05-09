#!/usr/bin/env python3
""" module to test client """
import unittest
from unittest.mock import patch, PropertyMock
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

    def test_public_repos_url(self):
        """ to unit-test GithubOrgClient._public_repos_url """
        with patch.object(GithubOrgClient, "org",
                          new_callable=PropertyMock) as mock:
            mock.return_value = {"repos_url": "known payload"}
            kp = "known payload"
            test_client = GithubOrgClient(kp)
            test_return = test_client._public_repos_url
            self.assertEqual(test_return, kp)
            mock.assert_called_once

    @patch("client.get_json")
    def test_public_repos(self, mock):
        """ to unit-test GithubOrgClient.public_repos """
        mock.return_value = [{"name": "holberton"}]
        with patch.object(GithubOrgClient,
                          "_public_repos_url",
                          new_callable=PropertyMock,
                          return_value="https://api.github.com/") as mock_pub:
            test_client = GithubOrgClient("hoberton")
            test_return = test_client.public_repos()
            self.assertEqual(test_return, ["holberton"])
            mock.assert_called_once
            mock_pub.assert_called_once
