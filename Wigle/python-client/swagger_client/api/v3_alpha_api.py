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


class V3ALPHAApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def bt(self, bt_network_id, **kwargs):  # noqa: E501
        """Request detail for a bluetooth network  # noqa: E501

        Location and detail properties for bluetooth networks. Detail endpoints are NOT included in COMMAPI subscriptions at this time.  Daily query limit subject to user DETAIL limit.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bt(bt_network_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str bt_network_id: Network ID. (required)
        :return: BtDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.bt_with_http_info(bt_network_id, **kwargs)  # noqa: E501
        else:
            (data) = self.bt_with_http_info(bt_network_id, **kwargs)  # noqa: E501
            return data

    def bt_with_http_info(self, bt_network_id, **kwargs):  # noqa: E501
        """Request detail for a bluetooth network  # noqa: E501

        Location and detail properties for bluetooth networks. Detail endpoints are NOT included in COMMAPI subscriptions at this time.  Daily query limit subject to user DETAIL limit.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bt_with_http_info(bt_network_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str bt_network_id: Network ID. (required)
        :return: BtDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bt_network_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method bt" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bt_network_id' is set
        if self.api_client.client_side_validation and ('bt_network_id' not in params or
                                                       params['bt_network_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `bt_network_id` when calling `bt`")  # noqa: E501

        if self.api_client.client_side_validation and ('bt_network_id' in params and not re.search(r'^([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}$', params['bt_network_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `bt_network_id` when calling `bt`, must conform to the pattern `/^([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'bt_network_id' in params:
            path_params['btNetworkId'] = params['bt_network_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['user']  # noqa: E501

        return self.api_client.call_api(
            '/api/v3/detail/bt/{btNetworkId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BtDetail',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def cdma_cell(self, sid, nid, bsid, **kwargs):  # noqa: E501
        """Request detail for a CDMA network  # noqa: E501

        Location and detail properties for CDMA networks. Detail endpoints are NOT included in COMMAPI subscriptions at this time.  Daily query limit subject to user DETAIL limit.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cdma_cell(sid, nid, bsid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sid: CDMA System ID. (required)
        :param str nid: CDMA Network ID. (required)
        :param str bsid: CDMA Base Station ID. (required)
        :return: CellDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.cdma_cell_with_http_info(sid, nid, bsid, **kwargs)  # noqa: E501
        else:
            (data) = self.cdma_cell_with_http_info(sid, nid, bsid, **kwargs)  # noqa: E501
            return data

    def cdma_cell_with_http_info(self, sid, nid, bsid, **kwargs):  # noqa: E501
        """Request detail for a CDMA network  # noqa: E501

        Location and detail properties for CDMA networks. Detail endpoints are NOT included in COMMAPI subscriptions at this time.  Daily query limit subject to user DETAIL limit.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cdma_cell_with_http_info(sid, nid, bsid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sid: CDMA System ID. (required)
        :param str nid: CDMA Network ID. (required)
        :param str bsid: CDMA Base Station ID. (required)
        :return: CellDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sid', 'nid', 'bsid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cdma_cell" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sid' is set
        if self.api_client.client_side_validation and ('sid' not in params or
                                                       params['sid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `sid` when calling `cdma_cell`")  # noqa: E501
        # verify the required parameter 'nid' is set
        if self.api_client.client_side_validation and ('nid' not in params or
                                                       params['nid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `nid` when calling `cdma_cell`")  # noqa: E501
        # verify the required parameter 'bsid' is set
        if self.api_client.client_side_validation and ('bsid' not in params or
                                                       params['bsid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `bsid` when calling `cdma_cell`")  # noqa: E501

        if self.api_client.client_side_validation and ('sid' in params and not re.search(r'^[0-9]{1,5}$', params['sid'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `sid` when calling `cdma_cell`, must conform to the pattern `/^[0-9]{1,5}$/`")  # noqa: E501
        if self.api_client.client_side_validation and ('nid' in params and not re.search(r'^[0-9]{1,5}$', params['nid'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `nid` when calling `cdma_cell`, must conform to the pattern `/^[0-9]{1,5}$/`")  # noqa: E501
        if self.api_client.client_side_validation and ('bsid' in params and not re.search(r'^[0-9]{1,9}$', params['bsid'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `bsid` when calling `cdma_cell`, must conform to the pattern `/^[0-9]{1,9}$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'sid' in params:
            path_params['sid'] = params['sid']  # noqa: E501
        if 'nid' in params:
            path_params['nid'] = params['nid']  # noqa: E501
        if 'bsid' in params:
            path_params['bsid'] = params['bsid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['user']  # noqa: E501

        return self.api_client.call_api(
            '/api/v3/detail/cell/CDMA/{sid}/{nid}/{bsid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CellDetail',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def cell(self, operator, lac, cid, type, **kwargs):  # noqa: E501
        """Request detail for a GSM, LTE, or WCDMA network  # noqa: E501

        Location and detail properties for non-CDMA cell types. Note that the type parameter is sensitive to current type in the WiGLE database - this means that LTE and WCDMA networks may have been reported as GSM in some packages, a fallback query to GSM is recommended if the LTE/WCDMA network appears to be absent. Detail endpoints are NOT included in COMMAPI subscriptions at this time.  Daily query limit subject to user DETAIL limit.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cell(operator, lac, cid, type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str operator: GSM/LTE/WCDMA Operator ID (required)
        :param str lac: GSM/LTE/WCDMA Location Area Code (required)
        :param str cid: GSM/LTE/WCDMA Cell ID (required)
        :param str type: Network Type: GSM/LTE/WCDMA (required)
        :return: BtDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.cell_with_http_info(operator, lac, cid, type, **kwargs)  # noqa: E501
        else:
            (data) = self.cell_with_http_info(operator, lac, cid, type, **kwargs)  # noqa: E501
            return data

    def cell_with_http_info(self, operator, lac, cid, type, **kwargs):  # noqa: E501
        """Request detail for a GSM, LTE, or WCDMA network  # noqa: E501

        Location and detail properties for non-CDMA cell types. Note that the type parameter is sensitive to current type in the WiGLE database - this means that LTE and WCDMA networks may have been reported as GSM in some packages, a fallback query to GSM is recommended if the LTE/WCDMA network appears to be absent. Detail endpoints are NOT included in COMMAPI subscriptions at this time.  Daily query limit subject to user DETAIL limit.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cell_with_http_info(operator, lac, cid, type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str operator: GSM/LTE/WCDMA Operator ID (required)
        :param str lac: GSM/LTE/WCDMA Location Area Code (required)
        :param str cid: GSM/LTE/WCDMA Cell ID (required)
        :param str type: Network Type: GSM/LTE/WCDMA (required)
        :return: BtDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['operator', 'lac', 'cid', 'type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cell" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'operator' is set
        if self.api_client.client_side_validation and ('operator' not in params or
                                                       params['operator'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `operator` when calling `cell`")  # noqa: E501
        # verify the required parameter 'lac' is set
        if self.api_client.client_side_validation and ('lac' not in params or
                                                       params['lac'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `lac` when calling `cell`")  # noqa: E501
        # verify the required parameter 'cid' is set
        if self.api_client.client_side_validation and ('cid' not in params or
                                                       params['cid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `cid` when calling `cell`")  # noqa: E501
        # verify the required parameter 'type' is set
        if self.api_client.client_side_validation and ('type' not in params or
                                                       params['type'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `type` when calling `cell`")  # noqa: E501

        if self.api_client.client_side_validation and ('operator' in params and not re.search(r'^[0-9]{1,6}$', params['operator'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `operator` when calling `cell`, must conform to the pattern `/^[0-9]{1,6}$/`")  # noqa: E501
        if self.api_client.client_side_validation and ('lac' in params and not re.search(r'^[0-9]{1,5}$', params['lac'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `lac` when calling `cell`, must conform to the pattern `/^[0-9]{1,5}$/`")  # noqa: E501
        if self.api_client.client_side_validation and ('cid' in params and not re.search(r'^[0-9]{1,9}$', params['cid'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `cid` when calling `cell`, must conform to the pattern `/^[0-9]{1,9}$/`")  # noqa: E501
        if self.api_client.client_side_validation and ('type' in params and not re.search(r'^(GSM|LTE|WCDMA)$', params['type'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `type` when calling `cell`, must conform to the pattern `/^(GSM|LTE|WCDMA)$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'operator' in params:
            path_params['operator'] = params['operator']  # noqa: E501
        if 'lac' in params:
            path_params['lac'] = params['lac']  # noqa: E501
        if 'cid' in params:
            path_params['cid'] = params['cid']  # noqa: E501
        if 'type' in params:
            path_params['type'] = params['type']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['user']  # noqa: E501

        return self.api_client.call_api(
            '/api/v3/detail/cell/{type}/{operator}/{lac}/{cid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BtDetail',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def cell_channel(self, type, latitude1, latitude2, longitude1, longitude2, **kwargs):  # noqa: E501
        """Request list of channels for GSM, LTE, or WCDMA transmitters in specified region  # noqa: E501

        List of known channels and QoS values for any of the non-CDMA cell types in a bounding box. Note that the type parameter is sensitive to current type in the WiGLE database - this means that LTE and WCDMA networks may have been reported as GSM in some packages, a fallback query to GSM is recommended if the LTE/WCDMA network appears to be absent. Channel endpoints are NOT included in COMMAPI subscriptions at this time. Region cannot be large than 99 square miles (~256 sq km). Daily query limit subject to user DETAIL limit. Designed to support cell-site simulator detection.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cell_channel(type, latitude1, latitude2, longitude1, longitude2, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str type: Network Type: GSM/LTE/WCDMA (required)
        :param float latitude1: First bounding latitude (required)
        :param float latitude2: Second bounding latitude (required)
        :param float longitude1: First bounding longitude (required)
        :param float longitude2: Second bounding longitude (required)
        :return: ChannelDetailResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.cell_channel_with_http_info(type, latitude1, latitude2, longitude1, longitude2, **kwargs)  # noqa: E501
        else:
            (data) = self.cell_channel_with_http_info(type, latitude1, latitude2, longitude1, longitude2, **kwargs)  # noqa: E501
            return data

    def cell_channel_with_http_info(self, type, latitude1, latitude2, longitude1, longitude2, **kwargs):  # noqa: E501
        """Request list of channels for GSM, LTE, or WCDMA transmitters in specified region  # noqa: E501

        List of known channels and QoS values for any of the non-CDMA cell types in a bounding box. Note that the type parameter is sensitive to current type in the WiGLE database - this means that LTE and WCDMA networks may have been reported as GSM in some packages, a fallback query to GSM is recommended if the LTE/WCDMA network appears to be absent. Channel endpoints are NOT included in COMMAPI subscriptions at this time. Region cannot be large than 99 square miles (~256 sq km). Daily query limit subject to user DETAIL limit. Designed to support cell-site simulator detection.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cell_channel_with_http_info(type, latitude1, latitude2, longitude1, longitude2, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str type: Network Type: GSM/LTE/WCDMA (required)
        :param float latitude1: First bounding latitude (required)
        :param float latitude2: Second bounding latitude (required)
        :param float longitude1: First bounding longitude (required)
        :param float longitude2: Second bounding longitude (required)
        :return: ChannelDetailResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['type', 'latitude1', 'latitude2', 'longitude1', 'longitude2']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cell_channel" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'type' is set
        if self.api_client.client_side_validation and ('type' not in params or
                                                       params['type'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `type` when calling `cell_channel`")  # noqa: E501
        # verify the required parameter 'latitude1' is set
        if self.api_client.client_side_validation and ('latitude1' not in params or
                                                       params['latitude1'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `latitude1` when calling `cell_channel`")  # noqa: E501
        # verify the required parameter 'latitude2' is set
        if self.api_client.client_side_validation and ('latitude2' not in params or
                                                       params['latitude2'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `latitude2` when calling `cell_channel`")  # noqa: E501
        # verify the required parameter 'longitude1' is set
        if self.api_client.client_side_validation and ('longitude1' not in params or
                                                       params['longitude1'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `longitude1` when calling `cell_channel`")  # noqa: E501
        # verify the required parameter 'longitude2' is set
        if self.api_client.client_side_validation and ('longitude2' not in params or
                                                       params['longitude2'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `longitude2` when calling `cell_channel`")  # noqa: E501

        if self.api_client.client_side_validation and ('type' in params and not re.search(r'^(GSM|LTE|WCDMA)$', params['type'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `type` when calling `cell_channel`, must conform to the pattern `/^(GSM|LTE|WCDMA)$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'type' in params:
            path_params['type'] = params['type']  # noqa: E501

        query_params = []
        if 'latitude1' in params:
            query_params.append(('latitude1', params['latitude1']))  # noqa: E501
        if 'latitude2' in params:
            query_params.append(('latitude2', params['latitude2']))  # noqa: E501
        if 'longitude1' in params:
            query_params.append(('longitude1', params['longitude1']))  # noqa: E501
        if 'longitude2' in params:
            query_params.append(('longitude2', params['longitude2']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['user']  # noqa: E501

        return self.api_client.call_api(
            '/api/v3/cellChannel/{type}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ChannelDetailResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def wifi(self, wifi_network_id, **kwargs):  # noqa: E501
        """Request detail for a WiFi network  # noqa: E501

        Location and detail properties for WiFi networks. Detail endpoints are NOT included in COMMAPI subscriptions at this time.  Daily query limit subject to user DETAIL limit.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.wifi(wifi_network_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str wifi_network_id: Network ID. (required)
        :return: WiFiDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.wifi_with_http_info(wifi_network_id, **kwargs)  # noqa: E501
        else:
            (data) = self.wifi_with_http_info(wifi_network_id, **kwargs)  # noqa: E501
            return data

    def wifi_with_http_info(self, wifi_network_id, **kwargs):  # noqa: E501
        """Request detail for a WiFi network  # noqa: E501

        Location and detail properties for WiFi networks. Detail endpoints are NOT included in COMMAPI subscriptions at this time.  Daily query limit subject to user DETAIL limit.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.wifi_with_http_info(wifi_network_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str wifi_network_id: Network ID. (required)
        :return: WiFiDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['wifi_network_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method wifi" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'wifi_network_id' is set
        if self.api_client.client_side_validation and ('wifi_network_id' not in params or
                                                       params['wifi_network_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `wifi_network_id` when calling `wifi`")  # noqa: E501

        if self.api_client.client_side_validation and ('wifi_network_id' in params and not re.search(r'^([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}$', params['wifi_network_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `wifi_network_id` when calling `wifi`, must conform to the pattern `/^([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'wifi_network_id' in params:
            path_params['wifiNetworkId'] = params['wifi_network_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['user']  # noqa: E501

        return self.api_client.call_api(
            '/api/v3/detail/wifi/{wifiNetworkId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WiFiDetail',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
