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


class NetworkObservationFileUploadAndStatus_Api(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_kml_for_trans_id(self, transid, **kwargs):  # noqa: E501
        """Download a KML summary of a file  # noqa: E501

        Get a KML summary approximation for a successfully processed file uploaded by the current user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_kml_for_trans_id(transid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str transid: The unique transaction ID for the file (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_kml_for_trans_id_with_http_info(transid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_kml_for_trans_id_with_http_info(transid, **kwargs)  # noqa: E501
            return data

    def get_kml_for_trans_id_with_http_info(self, transid, **kwargs):  # noqa: E501
        """Download a KML summary of a file  # noqa: E501

        Get a KML summary approximation for a successfully processed file uploaded by the current user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_kml_for_trans_id_with_http_info(transid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str transid: The unique transaction ID for the file (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['transid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_kml_for_trans_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'transid' is set
        if self.api_client.client_side_validation and ('transid' not in params or
                                                       params['transid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `transid` when calling `get_kml_for_trans_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'transid' in params:
            path_params['transid'] = params['transid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.google-earth.kml+xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/file/kml/{transid}', 'GET',
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

    def get_trans_logs_for_user(self, **kwargs):  # noqa: E501
        """Get the status of files uploaded by the current user  # noqa: E501

        Results in response model paginated at 100 results per page  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_trans_logs_for_user(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int pagestart: Most recent record to fetch descending chronologically. Defaults to 0
        :param int pageend: Number of results to fetch from offset. Defaults to 100
        :return: TranslogResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_trans_logs_for_user_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_trans_logs_for_user_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_trans_logs_for_user_with_http_info(self, **kwargs):  # noqa: E501
        """Get the status of files uploaded by the current user  # noqa: E501

        Results in response model paginated at 100 results per page  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_trans_logs_for_user_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int pagestart: Most recent record to fetch descending chronologically. Defaults to 0
        :param int pageend: Number of results to fetch from offset. Defaults to 100
        :return: TranslogResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['pagestart', 'pageend']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_trans_logs_for_user" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'pagestart' in params:
            query_params.append(('pagestart', params['pagestart']))  # noqa: E501
        if 'pageend' in params:
            query_params.append(('pageend', params['pageend']))  # noqa: E501

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
            '/api/v2/file/transactions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TranslogResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def upload(self, file, **kwargs):  # noqa: E501
        """Upload a file  # noqa: E501

        Transmit a file for processing and incorporation into the database. Supports DStumbler, G-Mon, inSSIDer, Kismac, Kismet, MacStumbler, NetStumbler, Pocket Warrior, Wardrive-Android, WiFiFoFum, WiFi-Where, WiGLE WiFi Wardriving, and Apple consolidated DB formats. One or more files may be enclosed within a zip, tar, or tar.gz archive. Files may not exceed 180MiB, and archives WILL IGNORE more than 200 member files. For documentation on WiGLE Wireless CSV files, see https://api.wigle.net/csvFormat.html  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upload(file, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file file: multipart/form-data file; proper formulation requires both filename and payload. (required)
        :param str donate: Allow commercial use of the file contents - 'on' to allow.
        :return: UploadResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.upload_with_http_info(file, **kwargs)  # noqa: E501
        else:
            (data) = self.upload_with_http_info(file, **kwargs)  # noqa: E501
            return data

    def upload_with_http_info(self, file, **kwargs):  # noqa: E501
        """Upload a file  # noqa: E501

        Transmit a file for processing and incorporation into the database. Supports DStumbler, G-Mon, inSSIDer, Kismac, Kismet, MacStumbler, NetStumbler, Pocket Warrior, Wardrive-Android, WiFiFoFum, WiFi-Where, WiGLE WiFi Wardriving, and Apple consolidated DB formats. One or more files may be enclosed within a zip, tar, or tar.gz archive. Files may not exceed 180MiB, and archives WILL IGNORE more than 200 member files. For documentation on WiGLE Wireless CSV files, see https://api.wigle.net/csvFormat.html  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upload_with_http_info(file, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file file: multipart/form-data file; proper formulation requires both filename and payload. (required)
        :param str donate: Allow commercial use of the file contents - 'on' to allow.
        :return: UploadResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file', 'donate']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upload" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file' is set
        if self.api_client.client_side_validation and ('file' not in params or
                                                       params['file'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `file` when calling `upload`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in params:
            local_var_files['file'] = params['file']  # noqa: E501
        if 'donate' in params:
            form_params.append(('donate', params['donate']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/file/upload', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UploadResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
