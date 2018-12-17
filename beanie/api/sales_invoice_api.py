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


class SalesInvoiceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_sales_invoice(self, sales_invoices, **kwargs):  # noqa: E501
        """add_sales_invoice  # noqa: E501

        Creates a new sales invoice in the system  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_sales_invoice(sales_invoices, async=True)
        >>> result = thread.get()

        :param async bool
        :param SalesInvoiceInput sales_invoices: Sales invoice to add to the system (required)
        :return: SalesInvoice
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.add_sales_invoice_with_http_info(sales_invoices, **kwargs)  # noqa: E501
        else:
            (data) = self.add_sales_invoice_with_http_info(sales_invoices, **kwargs)  # noqa: E501
            return data

    def add_sales_invoice_with_http_info(self, sales_invoices, **kwargs):  # noqa: E501
        """add_sales_invoice  # noqa: E501

        Creates a new sales invoice in the system  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_sales_invoice_with_http_info(sales_invoices, async=True)
        >>> result = thread.get()

        :param async bool
        :param SalesInvoiceInput sales_invoices: Sales invoice to add to the system (required)
        :return: SalesInvoice
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sales_invoices']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_sales_invoice" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sales_invoices' is set
        if ('sales_invoices' not in params or
                params['sales_invoices'] is None):
            raise ValueError("Missing the required parameter `sales_invoices` when calling `add_sales_invoice`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'sales_invoices' in params:
            body_params = params['sales_invoices']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/sales_invoices', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SalesInvoice',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def find_sales_invoice_by_id(self, id, **kwargs):  # noqa: E501
        """Find Sales invoice by ID  # noqa: E501

        Returns a single sales invoice if the user has access  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.find_sales_invoice_by_id(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: ID of sales invoice to fetch (required)
        :return: SalesInvoice
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.find_sales_invoice_by_id_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.find_sales_invoice_by_id_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def find_sales_invoice_by_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """Find Sales invoice by ID  # noqa: E501

        Returns a single sales invoice if the user has access  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.find_sales_invoice_by_id_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: ID of sales invoice to fetch (required)
        :return: SalesInvoice
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
                    " to method find_sales_invoice_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `find_sales_invoice_by_id`")  # noqa: E501

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
            '/sales_invoices/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SalesInvoice',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def find_sales_invoices(self, **kwargs):  # noqa: E501
        """All sales invoice  # noqa: E501

        Returns all sales invoice from the system that the user has access to  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.find_sales_invoices(async=True)
        >>> result = thread.get()

        :param async bool
        :param list[str] tags: tags to filter by
        :param int limit: Maximum number of results to return
        :return: list[SalesInvoice]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.find_sales_invoices_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.find_sales_invoices_with_http_info(**kwargs)  # noqa: E501
            return data

    def find_sales_invoices_with_http_info(self, **kwargs):  # noqa: E501
        """All sales invoice  # noqa: E501

        Returns all sales invoice from the system that the user has access to  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.find_sales_invoices_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param list[str] tags: tags to filter by
        :param int limit: Maximum number of results to return
        :return: list[SalesInvoice]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tags', 'limit']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method find_sales_invoices" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'tags' in params:
            query_params.append(('tags', params['tags']))  # noqa: E501
            collection_formats['tags'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/sales_invoices', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SalesInvoice]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
