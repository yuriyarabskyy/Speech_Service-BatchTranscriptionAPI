# coding: utf-8

"""
    Speech Services API v2.0

    Speech Services API v2.0.  # noqa: E501

    OpenAPI spec version: v2.0
    Contact: crservice@microsoft.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from cris_client.api_client import ApiClient


class CustomSpeechSubscriptionsManagementApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def post_move_to_subscription(self, move_to_subscription_definition, **kwargs):  # noqa: E501
        """Initiates a task that moves all entities associated with the authenticated subscription to another one.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_move_to_subscription(move_to_subscription_definition, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MoveToSubscriptionDefinition move_to_subscription_definition: The details of the subscription the entities are moved to. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_move_to_subscription_with_http_info(move_to_subscription_definition, **kwargs)  # noqa: E501
        else:
            (data) = self.post_move_to_subscription_with_http_info(move_to_subscription_definition, **kwargs)  # noqa: E501
            return data

    def post_move_to_subscription_with_http_info(self, move_to_subscription_definition, **kwargs):  # noqa: E501
        """Initiates a task that moves all entities associated with the authenticated subscription to another one.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_move_to_subscription_with_http_info(move_to_subscription_definition, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MoveToSubscriptionDefinition move_to_subscription_definition: The details of the subscription the entities are moved to. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['move_to_subscription_definition']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_move_to_subscription" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'move_to_subscription_definition' is set
        if ('move_to_subscription_definition' not in params or
                params['move_to_subscription_definition'] is None):
            raise ValueError("Missing the required parameter `move_to_subscription_definition` when calling `post_move_to_subscription`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'move_to_subscription_definition' in params:
            body_params = params['move_to_subscription_definition']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['subscription_key']  # noqa: E501

        return self.api_client.call_api(
            '/api/common/v2.0/subscriptions', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
