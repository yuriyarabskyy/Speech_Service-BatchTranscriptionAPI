# coding: utf-8

"""
    Speech Services API v2.0

    Speech Services API v2.0.  # noqa: E501

    OpenAPI spec version: v2.0
    Contact: crservice@microsoft.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.voice_datasets_api import VoiceDatasetsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestVoiceDatasetsApi(unittest.TestCase):
    """VoiceDatasetsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.voice_datasets_api.VoiceDatasetsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_voice_dataset(self):
        """Test case for delete_voice_dataset

        Deletes the voice dataset with the given id.  # noqa: E501
        """
        pass

    def test_get_supported_locales_for_voice_datasets(self):
        """Test case for get_supported_locales_for_voice_datasets

        Gets a list of supported locales for custom voice data imports.  # noqa: E501
        """
        pass

    def test_get_voice_datasets(self):
        """Test case for get_voice_datasets

        Gets all voice datasets of a user.  # noqa: E501
        """
        pass

    def test_update_voice_dataset(self):
        """Test case for update_voice_dataset

        Updates the mutable details of the voice dataset identified by its ID.  # noqa: E501
        """
        pass

    def test_upload_voice_dataset(self):
        """Test case for upload_voice_dataset

        Uploads data and creates a new voice data object.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
