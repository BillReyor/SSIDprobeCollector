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
from swagger_client.api.network_observation_file_upload_and_status__api import NetworkObservationFileUploadAndStatus_Api  # noqa: E501
from swagger_client.rest import ApiException


class TestNetworkObservationFileUploadAndStatus_Api(unittest.TestCase):
    """NetworkObservationFileUploadAndStatus_Api unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.network_observation_file_upload_and_status__api.NetworkObservationFileUploadAndStatus_Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_kml_for_trans_id(self):
        """Test case for get_kml_for_trans_id

        Download a KML summary of a file  # noqa: E501
        """
        pass

    def test_get_trans_logs_for_user(self):
        """Test case for get_trans_logs_for_user

        Get the status of files uploaded by the current user  # noqa: E501
        """
        pass

    def test_upload(self):
        """Test case for upload

        Upload a file  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
