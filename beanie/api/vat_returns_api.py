# coding: utf-8

"""
    Beanie ERP API

    An API specification for interacting with the Beanie ERP system  # noqa: E501

    OpenAPI spec version: 0.2
    Contact: dev@bean.ie
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from beanie.api_client import ApiClient


class VatReturnsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_vat_return(self, vat_returns, **kwargs):  # noqa: E501
        """add_vat_return  # noqa: E501

        Creates a new vat return in the system  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_vat_return(vat_returns, async=True)
        >>> result = thread.get()

        :param async bool
        :param VatReturnInput vat_returns: VAT return to add to the system (required)
        :return: VatReturn
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.add_vat_return_with_http_info(vat_returns, **kwargs)  # noqa: E501
        else:
            (data) = self.add_vat_return_with_http_info(vat_returns, **kwargs)  # noqa: E501
            return data

    def add_vat_return_with_http_info(self, vat_returns, **kwargs):  # noqa: E501
        """add_vat_return  # noqa: E501

        Creates a new vat return in the system  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_vat_return_with_http_info(vat_returns, async=True)
        >>> result = thread.get()

        :param async bool
        :param VatReturnInput vat_returns: VAT return to add to the system (required)
        :return: VatReturn
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['vat_returns']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_vat_return" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'vat_returns' is set
        if ('vat_returns' not in params or
                params['vat_returns'] is None):
            raise ValueError("Missing the required parameter `vat_returns` when calling `add_vat_return`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'vat_returns' in params:
            body_params = params['vat_returns']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/vat_returns', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VatReturn',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def find_vat_return_by_id(self, id, **kwargs):  # noqa: E501
        """Find VAT return by ID  # noqa: E501

        Returns a single vat return if the user has access  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.find_vat_return_by_id(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: ID of vat return to fetch (required)
        :return: VatReturn
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.find_vat_return_by_id_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.find_vat_return_by_id_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def find_vat_return_by_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """Find VAT return by ID  # noqa: E501

        Returns a single vat return if the user has access  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.find_vat_return_by_id_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: ID of vat return to fetch (required)
        :return: VatReturn
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method find_vat_return_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `find_vat_return_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/vat_returns/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VatReturn',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)