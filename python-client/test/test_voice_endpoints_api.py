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
from swagger_client.api.voice_endpoints_api import VoiceEndpointsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestVoiceEndpointsApi(unittest.TestCase):
    """VoiceEndpointsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.voice_endpoints_api.VoiceEndpointsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_voice_deployment(self):
        """Test case for create_voice_deployment

        Creates a new voice endpoint object.  # noqa: E501
        """
        pass

    def test_delete_deployment(self):
        """Test case for delete_deployment

        Delete the specified voice endpoint.  # noqa: E501
        """
        pass

    def test_get_supported_locales_for_voice_endpoints(self):
        """Test case for get_supported_locales_for_voice_endpoints

        Gets a list of supported locales for custom voice Endpoints.  # noqa: E501
        """
        pass

    def test_get_voice_deployment(self):
        """Test case for get_voice_deployment

        Gets the details of a Custom Voice endpoint.  # noqa: E501
        """
        pass

    def test_get_voice_deployments(self):
        """Test case for get_voice_deployments

        Gets a list of voice endpoint details.  # noqa: E501
        """
        pass

    def test_update_voice_endpoint(self):
        """Test case for update_voice_endpoint

        Updates the name and description of the endpoint identified by the given ID.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()