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


class StatisticsAndInformationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def countries(self, **kwargs):  # noqa: E501
        """Get statistics organized by country  # noqa: E501

        Fetches all countries and basic stats  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.countries(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: CountriesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.countries_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.countries_with_http_info(**kwargs)  # noqa: E501
            return data

    def countries_with_http_info(self, **kwargs):  # noqa: E501
        """Get statistics organized by country  # noqa: E501

        Fetches all countries and basic stats  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.countries_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: CountriesResponse
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
                    " to method countries" % key
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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/stats/countries', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CountriesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def country_region(self, **kwargs):  # noqa: E501
        """Get statistics for a specified country, organized by region, postal code, and encryption  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.country_region(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str country: the two-letter code of the country for which you'd like a regional breakdown. Defaults to 'US'
        :return: RegionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.country_region_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.country_region_with_http_info(**kwargs)  # noqa: E501
            return data

    def country_region_with_http_info(self, **kwargs):  # noqa: E501
        """Get statistics for a specified country, organized by region, postal code, and encryption  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.country_region_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str country: the two-letter code of the country for which you'd like a regional breakdown. Defaults to 'US'
        :return: RegionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['country']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method country_region" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'country' in params:
            query_params.append(('country', params['country']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/stats/regions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RegionResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def general_stats(self, **kwargs):  # noqa: E501
        """Get a named map of general statistics  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.general_stats(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: dict(str, object)
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.general_stats_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.general_stats_with_http_info(**kwargs)  # noqa: E501
            return data

    def general_stats_with_http_info(self, **kwargs):  # noqa: E501
        """Get a named map of general statistics  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.general_stats_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: dict(str, object)
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
                    " to method general_stats" % key
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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/stats/general', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='dict(str, object)',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def group_stats(self, **kwargs):  # noqa: E501
        """Get group standings  # noqa: E501

        Fetches a list of all teams. Authenticated users receive additional group info for the group they administer.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.group_stats(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: GroupStatResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.group_stats_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.group_stats_with_http_info(**kwargs)  # noqa: E501
            return data

    def group_stats_with_http_info(self, **kwargs):  # noqa: E501
        """Get group standings  # noqa: E501

        Fetches a list of all teams. Authenticated users receive additional group info for the group they administer.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.group_stats_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: GroupStatResponse
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
                    " to method group_stats" % key
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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/stats/group', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GroupStatResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def site_stats(self, **kwargs):  # noqa: E501
        """Get a named map of site-level statistics  # noqa: E501

        A big hash of short-named statistics used in providing site-wide information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.site_stats(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: dict(str, object)
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.site_stats_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.site_stats_with_http_info(**kwargs)  # noqa: E501
            return data

    def site_stats_with_http_info(self, **kwargs):  # noqa: E501
        """Get a named map of site-level statistics  # noqa: E501

        A big hash of short-named statistics used in providing site-wide information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.site_stats_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: dict(str, object)
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
                    " to method site_stats" % key
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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/stats/site', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='dict(str, object)',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def stats(self, **kwargs):  # noqa: E501
        """Get user standings  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stats(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sort: The criteria by which to sort the results. Values are ['discovered', 'total', 'monthcount', 'prevmonthcount', 'gendisc', 'gentotal', 'firsttransid', 'lasttransid']
        :param int pagestart: The first record to request according to the 'sort' parameter
        :param int pageend: The last record to request according to the 'sort' parameter
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.stats_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.stats_with_http_info(**kwargs)  # noqa: E501
            return data

    def stats_with_http_info(self, **kwargs):  # noqa: E501
        """Get user standings  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stats_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sort: The criteria by which to sort the results. Values are ['discovered', 'total', 'monthcount', 'prevmonthcount', 'gendisc', 'gentotal', 'firsttransid', 'lasttransid']
        :param int pagestart: The first record to request according to the 'sort' parameter
        :param int pageend: The last record to request according to the 'sort' parameter
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sort', 'pagestart', 'pageend']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method stats" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/stats/standings', 'GET',
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

    def user_statistics(self, **kwargs):  # noqa: E501
        """Get user statistics  # noqa: E501

        Get statistics and badge image for the authenticated user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_statistics(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user: the name of the user for whom to get stats
        :return: UserStatsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.user_statistics_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.user_statistics_with_http_info(**kwargs)  # noqa: E501
            return data

    def user_statistics_with_http_info(self, **kwargs):  # noqa: E501
        """Get user statistics  # noqa: E501

        Get statistics and badge image for the authenticated user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_statistics_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user: the name of the user for whom to get stats
        :return: UserStatsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_statistics" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user' in params:
            query_params.append(('user', params['user']))  # noqa: E501

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
            '/api/v2/stats/user', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserStatsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)