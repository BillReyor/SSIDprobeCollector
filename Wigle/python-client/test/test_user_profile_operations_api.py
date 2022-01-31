# coding: utf-8

"""
    WiGLE API

    Search, upload, and integrate statistics from WiGLE. Use API Name+Token from https://wigle.net/account  # noqa: E501

    OpenAPI spec version: 3.1
    Contact: WiGLE-admin@wigle.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.user_profile_operations_api import UserProfileOperationsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestUserProfileOperationsApi(unittest.TestCase):
    """UserProfileOperationsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.user_profile_operations_api.UserProfileOperationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_token(self):
        """Test case for api_token

        Get all authorization tokens for the logged-in user  # noqa: E501
        """
        pass

    def test_user(self):
        """Test case for user

        Get the user object for the current logged-in user  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
