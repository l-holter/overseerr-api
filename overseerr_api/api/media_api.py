# coding: utf-8

"""
    Overseerr API

    This is the documentation for the Overseerr API backend.  Two primary authentication methods are supported:  - **Cookie Authentication**: A valid sign-in to the `/auth/plex` or `/auth/local` will generate a valid authentication cookie. - **API Key Authentication**: Sign-in is also possible by passing an `X-Api-Key` header along with a valid API Key generated by Overseerr. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError

from typing_extensions import Annotated
from pydantic import Field, StrictFloat, StrictInt, StrictStr

from typing import Optional, Union

from overseerr_api.models.media_get200_response import MediaGet200Response
from overseerr_api.models.media_info import MediaInfo
from overseerr_api.models.media_media_id_status_post_request import MediaMediaIdStatusPostRequest
from overseerr_api.models.media_media_id_watch_data_get200_response import MediaMediaIdWatchDataGet200Response

from overseerr_api.api_client import ApiClient
from overseerr_api.api_response import ApiResponse
from overseerr_api.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class MediaApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def media_get(self, take : Optional[Union[StrictFloat, StrictInt]] = None, skip : Optional[Union[StrictFloat, StrictInt]] = None, filter : Optional[StrictStr] = None, sort : Optional[StrictStr] = None, **kwargs) -> MediaGet200Response:  # noqa: E501
        """Get media  # noqa: E501

        Returns all media (can be filtered and limited) in a JSON object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.media_get(take, skip, filter, sort, async_req=True)
        >>> result = thread.get()

        :param take:
        :type take: float
        :param skip:
        :type skip: float
        :param filter:
        :type filter: str
        :param sort:
        :type sort: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: MediaGet200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the media_get_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.media_get_with_http_info(take, skip, filter, sort, **kwargs)  # noqa: E501

    @validate_arguments
    def media_get_with_http_info(self, take : Optional[Union[StrictFloat, StrictInt]] = None, skip : Optional[Union[StrictFloat, StrictInt]] = None, filter : Optional[StrictStr] = None, sort : Optional[StrictStr] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Get media  # noqa: E501

        Returns all media (can be filtered and limited) in a JSON object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.media_get_with_http_info(take, skip, filter, sort, async_req=True)
        >>> result = thread.get()

        :param take:
        :type take: float
        :param skip:
        :type skip: float
        :param filter:
        :type filter: str
        :param sort:
        :type sort: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(MediaGet200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'take',
            'skip',
            'filter',
            'sort'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method media_get" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('take') is not None:  # noqa: E501
            _query_params.append(('take', _params['take']))

        if _params.get('skip') is not None:  # noqa: E501
            _query_params.append(('skip', _params['skip']))

        if _params.get('filter') is not None:  # noqa: E501
            _query_params.append(('filter', _params['filter']))

        if _params.get('sort') is not None:  # noqa: E501
            _query_params.append(('sort', _params['sort']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['apiKey', 'cookieAuth']  # noqa: E501

        _response_types_map = {
            '200': "MediaGet200Response",
        }

        return self.api_client.call_api(
            '/media', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def media_media_id_delete(self, media_id : Annotated[StrictStr, Field(..., description="Media ID")], **kwargs) -> None:  # noqa: E501
        """Delete media item  # noqa: E501

        Removes a media item. The `MANAGE_REQUESTS` permission is required to perform this action.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.media_media_id_delete(media_id, async_req=True)
        >>> result = thread.get()

        :param media_id: Media ID (required)
        :type media_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the media_media_id_delete_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.media_media_id_delete_with_http_info(media_id, **kwargs)  # noqa: E501

    @validate_arguments
    def media_media_id_delete_with_http_info(self, media_id : Annotated[StrictStr, Field(..., description="Media ID")], **kwargs) -> ApiResponse:  # noqa: E501
        """Delete media item  # noqa: E501

        Removes a media item. The `MANAGE_REQUESTS` permission is required to perform this action.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.media_media_id_delete_with_http_info(media_id, async_req=True)
        >>> result = thread.get()

        :param media_id: Media ID (required)
        :type media_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'media_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method media_media_id_delete" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['media_id'] is not None:
            _path_params['mediaId'] = _params['media_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # authentication setting
        _auth_settings = ['apiKey', 'cookieAuth']  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/media/{mediaId}', 'DELETE',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def media_media_id_status_post(self, media_id : Annotated[StrictStr, Field(..., description="Media ID")], status : Annotated[StrictStr, Field(..., description="New status")], media_media_id_status_post_request : Optional[MediaMediaIdStatusPostRequest] = None, **kwargs) -> MediaInfo:  # noqa: E501
        """Update media status  # noqa: E501

        Updates a media item's status and returns the media in JSON format  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.media_media_id_status_post(media_id, status, media_media_id_status_post_request, async_req=True)
        >>> result = thread.get()

        :param media_id: Media ID (required)
        :type media_id: str
        :param status: New status (required)
        :type status: str
        :param media_media_id_status_post_request:
        :type media_media_id_status_post_request: MediaMediaIdStatusPostRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: MediaInfo
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the media_media_id_status_post_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.media_media_id_status_post_with_http_info(media_id, status, media_media_id_status_post_request, **kwargs)  # noqa: E501

    @validate_arguments
    def media_media_id_status_post_with_http_info(self, media_id : Annotated[StrictStr, Field(..., description="Media ID")], status : Annotated[StrictStr, Field(..., description="New status")], media_media_id_status_post_request : Optional[MediaMediaIdStatusPostRequest] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Update media status  # noqa: E501

        Updates a media item's status and returns the media in JSON format  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.media_media_id_status_post_with_http_info(media_id, status, media_media_id_status_post_request, async_req=True)
        >>> result = thread.get()

        :param media_id: Media ID (required)
        :type media_id: str
        :param status: New status (required)
        :type status: str
        :param media_media_id_status_post_request:
        :type media_media_id_status_post_request: MediaMediaIdStatusPostRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(MediaInfo, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'media_id',
            'status',
            'media_media_id_status_post_request'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method media_media_id_status_post" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['media_id'] is not None:
            _path_params['mediaId'] = _params['media_id']

        if _params['status'] is not None:
            _path_params['status'] = _params['status']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['media_media_id_status_post_request'] is not None:
            _body_params = _params['media_media_id_status_post_request']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['apiKey', 'cookieAuth']  # noqa: E501

        _response_types_map = {
            '200': "MediaInfo",
        }

        return self.api_client.call_api(
            '/media/{mediaId}/{status}', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def media_media_id_watch_data_get(self, media_id : Annotated[StrictStr, Field(..., description="Media ID")], **kwargs) -> MediaMediaIdWatchDataGet200Response:  # noqa: E501
        """Get watch data  # noqa: E501

        Returns play count, play duration, and users who have watched the media.  Requires the `ADMIN` permission.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.media_media_id_watch_data_get(media_id, async_req=True)
        >>> result = thread.get()

        :param media_id: Media ID (required)
        :type media_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: MediaMediaIdWatchDataGet200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the media_media_id_watch_data_get_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.media_media_id_watch_data_get_with_http_info(media_id, **kwargs)  # noqa: E501

    @validate_arguments
    def media_media_id_watch_data_get_with_http_info(self, media_id : Annotated[StrictStr, Field(..., description="Media ID")], **kwargs) -> ApiResponse:  # noqa: E501
        """Get watch data  # noqa: E501

        Returns play count, play duration, and users who have watched the media.  Requires the `ADMIN` permission.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.media_media_id_watch_data_get_with_http_info(media_id, async_req=True)
        >>> result = thread.get()

        :param media_id: Media ID (required)
        :type media_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(MediaMediaIdWatchDataGet200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'media_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method media_media_id_watch_data_get" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['media_id'] is not None:
            _path_params['mediaId'] = _params['media_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['apiKey', 'cookieAuth']  # noqa: E501

        _response_types_map = {
            '200': "MediaMediaIdWatchDataGet200Response",
        }

        return self.api_client.call_api(
            '/media/{mediaId}/watch_data', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
