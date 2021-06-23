# coding: utf-8

"""
    GSI Floating-Point 32 API

    **Introduction**<br> GSI Technology’s floating-point similarity search API provides an accessible gateway to running searches on GSI’s Gemini® Associative Processing Unit (APU).<br> It works in conjunction with the GSI system management solution which enables users to work with multiple APU boards simultaneously for improved performance.<br><br> **Dataset and Query Format**<br> Dataset embeddings can be in 32- or 64-bit floating point format, and any number of features, e.g. 256 or 512 (there is no upper limit).<br> Query embeddings must have the same floating-point format and number of features as used in the dataset.<br> GSI performs the search and delivers the top-k most similar results.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class DemoApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def apis_add_neural_matrix(self, body, **kwargs):  # noqa: E501
        """Add a neural matrix into the list. For demo use only.  # noqa: E501

        Add a neural matrix into the list.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.apis_add_neural_matrix(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AddNeuralMatrixRequest body: (required)
        :return: AddNeuralMatrixResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.apis_add_neural_matrix_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.apis_add_neural_matrix_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def apis_add_neural_matrix_with_http_info(self, body, **kwargs):  # noqa: E501
        """Add a neural matrix into the list. For demo use only.  # noqa: E501

        Add a neural matrix into the list.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.apis_add_neural_matrix_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AddNeuralMatrixRequest body: (required)
        :return: AddNeuralMatrixResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method apis_add_neural_matrix" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `apis_add_neural_matrix`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/demo/neuralmatrix/add', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AddNeuralMatrixResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def apis_get_neural_matrix_list(self, **kwargs):  # noqa: E501
        """Get the list of available neural matrices.  # noqa: E501

        Get the list of available neural matrices.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.apis_get_neural_matrix_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: GetNeuralMatrixListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.apis_get_neural_matrix_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.apis_get_neural_matrix_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def apis_get_neural_matrix_list_with_http_info(self, **kwargs):  # noqa: E501
        """Get the list of available neural matrices.  # noqa: E501

        Get the list of available neural matrices.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.apis_get_neural_matrix_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: GetNeuralMatrixListResponse
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
                    " to method apis_get_neural_matrix_list" % key
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
            '/demo/neuralmatrix/list', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetNeuralMatrixListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def apis_get_queries_list(self, **kwargs):  # noqa: E501
        """Get the list of available queries.  # noqa: E501

        Get the list of available queries.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.apis_get_queries_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: GetQueriesListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.apis_get_queries_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.apis_get_queries_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def apis_get_queries_list_with_http_info(self, **kwargs):  # noqa: E501
        """Get the list of available queries.  # noqa: E501

        Get the list of available queries.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.apis_get_queries_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: GetQueriesListResponse
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
                    " to method apis_get_queries_list" % key
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
            '/demo/query/list', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetQueriesListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def apis_import_queries(self, body, **kwargs):  # noqa: E501
        """Import a queries file.  # noqa: E501

        Import a queries file.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.apis_import_queries(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ImportQueriesRequest body: (required)
        :return: ImportQueriesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.apis_import_queries_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.apis_import_queries_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def apis_import_queries_with_http_info(self, body, **kwargs):  # noqa: E501
        """Import a queries file.  # noqa: E501

        Import a queries file.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.apis_import_queries_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ImportQueriesRequest body: (required)
        :return: ImportQueriesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method apis_import_queries" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `apis_import_queries`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/demo/query/import', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ImportQueriesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def apis_remove_query(self, query_id, **kwargs):  # noqa: E501
        """Remove a query file from list  # noqa: E501

        Removes a query based on query ID from list of queries file  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.apis_remove_query(query_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str query_id: Query UID identifies the specific query. (required)
        :return: QueriesFileResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.apis_remove_query_with_http_info(query_id, **kwargs)  # noqa: E501
        else:
            (data) = self.apis_remove_query_with_http_info(query_id, **kwargs)  # noqa: E501
            return data

    def apis_remove_query_with_http_info(self, query_id, **kwargs):  # noqa: E501
        """Remove a query file from list  # noqa: E501

        Removes a query based on query ID from list of queries file  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.apis_remove_query_with_http_info(query_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str query_id: Query UID identifies the specific query. (required)
        :return: QueriesFileResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method apis_remove_query" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query_id' is set
        if ('query_id' not in params or
                params['query_id'] is None):
            raise ValueError("Missing the required parameter `query_id` when calling `apis_remove_query`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'query_id' in params:
            path_params['query_id'] = params['query_id']  # noqa: E501

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
            '/demo/query/remove/{query_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='QueriesFileResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
