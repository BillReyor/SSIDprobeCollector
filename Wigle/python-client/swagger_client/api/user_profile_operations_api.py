# coding: utf-8

"""
    WiGLE API

    Search, upload, and integrate statistics from WiGLE. Use API Name+Token from https://wigle.net/account  # noqa: E501

    OpenAPI spec version: 3.1
    Contact: WiGLE-admin@wigle.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class UserProfileOperationsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_token(self, **kwargs):  # noqa: E501
        """Get all authorization tokens for the logged-in user  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_token(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str type: Token types - 'API', 'COMMAPI', or 'ANDROID'
        :return: AuthTokensResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_token_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_token_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_token_with_http_info(self, **kwargs):  # noqa: E501
        """Get all authorization tokens for the logged-in user  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_token_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str type: Token types - 'API', 'COMMAPI', or 'ANDROID'
        :return: AuthTokensResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_token" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/profile/apiToken', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AuthTokensResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def user(self, **kwargs):  # noqa: E501
        """Get the user object for the current logged-in user  # noqa: E501

        See basic user information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Person
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.user_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.user_with_http_info(**kwargs)  # noqa: E501
            return data

    def user_with_http_info(self, **kwargs):  # noqa: E501
        """Get the user object for the current logged-in user  # noqa: E501

        See basic user information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Person
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/profile/user', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Person',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)