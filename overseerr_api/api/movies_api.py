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

from pydantic import StrictFloat, StrictInt, StrictStr

from typing import Optional, Union

from overseerr_api.models.discover_keyword_keyword_id_movies_get200_response import DiscoverKeywordKeywordIdMoviesGet200Response
from overseerr_api.models.movie_details import MovieDetails
from overseerr_api.models.movie_movie_id_ratings_get200_response import MovieMovieIdRatingsGet200Response
from overseerr_api.models.movie_movie_id_ratingscombined_get200_response import MovieMovieIdRatingscombinedGet200Response

from overseerr_api.api_client import ApiClient
from overseerr_api.api_response import ApiResponse
from overseerr_api.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class MoviesApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def movie_movie_id_get(self, movie_id : Union[StrictFloat, StrictInt], language : Optional[StrictStr] = None, **kwargs) -> MovieDetails:  # noqa: E501
        """Get movie details  # noqa: E501

        Returns full movie details in a JSON object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.movie_movie_id_get(movie_id, language, async_req=True)
        >>> result = thread.get()

        :param movie_id: (required)
        :type movie_id: float
        :param language:
        :type language: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: MovieDetails
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the movie_movie_id_get_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.movie_movie_id_get_with_http_info(movie_id, language, **kwargs)  # noqa: E501

    @validate_arguments
    def movie_movie_id_get_with_http_info(self, movie_id : Union[StrictFloat, StrictInt], language : Optional[StrictStr] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Get movie details  # noqa: E501

        Returns full movie details in a JSON object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.movie_movie_id_get_with_http_info(movie_id, language, async_req=True)
        >>> result = thread.get()

        :param movie_id: (required)
        :type movie_id: float
        :param language:
        :type language: str
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
        :rtype: tuple(MovieDetails, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'movie_id',
            'language'
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
                    " to method movie_movie_id_get" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['movie_id'] is not None:
            _path_params['movieId'] = _params['movie_id']


        # process the query parameters
        _query_params = []
        if _params.get('language') is not None:  # noqa: E501
            _query_params.append(('language', _params['language']))

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
            '200': "MovieDetails",
        }

        return self.api_client.call_api(
            '/movie/{movieId}', 'GET',
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
    def movie_movie_id_ratings_get(self, movie_id : Union[StrictFloat, StrictInt], **kwargs) -> MovieMovieIdRatingsGet200Response:  # noqa: E501
        """Get movie ratings  # noqa: E501

        Returns ratings based on the provided movieId in a JSON object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.movie_movie_id_ratings_get(movie_id, async_req=True)
        >>> result = thread.get()

        :param movie_id: (required)
        :type movie_id: float
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: MovieMovieIdRatingsGet200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the movie_movie_id_ratings_get_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.movie_movie_id_ratings_get_with_http_info(movie_id, **kwargs)  # noqa: E501

    @validate_arguments
    def movie_movie_id_ratings_get_with_http_info(self, movie_id : Union[StrictFloat, StrictInt], **kwargs) -> ApiResponse:  # noqa: E501
        """Get movie ratings  # noqa: E501

        Returns ratings based on the provided movieId in a JSON object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.movie_movie_id_ratings_get_with_http_info(movie_id, async_req=True)
        >>> result = thread.get()

        :param movie_id: (required)
        :type movie_id: float
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
        :rtype: tuple(MovieMovieIdRatingsGet200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'movie_id'
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
                    " to method movie_movie_id_ratings_get" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['movie_id'] is not None:
            _path_params['movieId'] = _params['movie_id']


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
            '200': "MovieMovieIdRatingsGet200Response",
        }

        return self.api_client.call_api(
            '/movie/{movieId}/ratings', 'GET',
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
    def movie_movie_id_ratingscombined_get(self, movie_id : Union[StrictFloat, StrictInt], **kwargs) -> MovieMovieIdRatingscombinedGet200Response:  # noqa: E501
        """Get RT and IMDB movie ratings combined  # noqa: E501

        Returns ratings from RottenTomatoes and IMDB based on the provided movieId in a JSON object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.movie_movie_id_ratingscombined_get(movie_id, async_req=True)
        >>> result = thread.get()

        :param movie_id: (required)
        :type movie_id: float
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: MovieMovieIdRatingscombinedGet200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the movie_movie_id_ratingscombined_get_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.movie_movie_id_ratingscombined_get_with_http_info(movie_id, **kwargs)  # noqa: E501

    @validate_arguments
    def movie_movie_id_ratingscombined_get_with_http_info(self, movie_id : Union[StrictFloat, StrictInt], **kwargs) -> ApiResponse:  # noqa: E501
        """Get RT and IMDB movie ratings combined  # noqa: E501

        Returns ratings from RottenTomatoes and IMDB based on the provided movieId in a JSON object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.movie_movie_id_ratingscombined_get_with_http_info(movie_id, async_req=True)
        >>> result = thread.get()

        :param movie_id: (required)
        :type movie_id: float
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
        :rtype: tuple(MovieMovieIdRatingscombinedGet200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'movie_id'
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
                    " to method movie_movie_id_ratingscombined_get" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['movie_id'] is not None:
            _path_params['movieId'] = _params['movie_id']


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
            '200': "MovieMovieIdRatingscombinedGet200Response",
        }

        return self.api_client.call_api(
            '/movie/{movieId}/ratingscombined', 'GET',
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
    def movie_movie_id_recommendations_get(self, movie_id : Union[StrictFloat, StrictInt], page : Optional[Union[StrictFloat, StrictInt]] = None, language : Optional[StrictStr] = None, **kwargs) -> DiscoverKeywordKeywordIdMoviesGet200Response:  # noqa: E501
        """Get recommended movies  # noqa: E501

        Returns list of recommended movies based on provided movie ID in a JSON object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.movie_movie_id_recommendations_get(movie_id, page, language, async_req=True)
        >>> result = thread.get()

        :param movie_id: (required)
        :type movie_id: float
        :param page:
        :type page: float
        :param language:
        :type language: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: DiscoverKeywordKeywordIdMoviesGet200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the movie_movie_id_recommendations_get_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.movie_movie_id_recommendations_get_with_http_info(movie_id, page, language, **kwargs)  # noqa: E501

    @validate_arguments
    def movie_movie_id_recommendations_get_with_http_info(self, movie_id : Union[StrictFloat, StrictInt], page : Optional[Union[StrictFloat, StrictInt]] = None, language : Optional[StrictStr] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Get recommended movies  # noqa: E501

        Returns list of recommended movies based on provided movie ID in a JSON object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.movie_movie_id_recommendations_get_with_http_info(movie_id, page, language, async_req=True)
        >>> result = thread.get()

        :param movie_id: (required)
        :type movie_id: float
        :param page:
        :type page: float
        :param language:
        :type language: str
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
        :rtype: tuple(DiscoverKeywordKeywordIdMoviesGet200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'movie_id',
            'page',
            'language'
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
                    " to method movie_movie_id_recommendations_get" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['movie_id'] is not None:
            _path_params['movieId'] = _params['movie_id']


        # process the query parameters
        _query_params = []
        if _params.get('page') is not None:  # noqa: E501
            _query_params.append(('page', _params['page']))

        if _params.get('language') is not None:  # noqa: E501
            _query_params.append(('language', _params['language']))

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
            '200': "DiscoverKeywordKeywordIdMoviesGet200Response",
        }

        return self.api_client.call_api(
            '/movie/{movieId}/recommendations', 'GET',
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
    def movie_movie_id_similar_get(self, movie_id : Union[StrictFloat, StrictInt], page : Optional[Union[StrictFloat, StrictInt]] = None, language : Optional[StrictStr] = None, **kwargs) -> DiscoverKeywordKeywordIdMoviesGet200Response:  # noqa: E501
        """Get similar movies  # noqa: E501

        Returns list of similar movies based on the provided movieId in a JSON object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.movie_movie_id_similar_get(movie_id, page, language, async_req=True)
        >>> result = thread.get()

        :param movie_id: (required)
        :type movie_id: float
        :param page:
        :type page: float
        :param language:
        :type language: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: DiscoverKeywordKeywordIdMoviesGet200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the movie_movie_id_similar_get_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.movie_movie_id_similar_get_with_http_info(movie_id, page, language, **kwargs)  # noqa: E501

    @validate_arguments
    def movie_movie_id_similar_get_with_http_info(self, movie_id : Union[StrictFloat, StrictInt], page : Optional[Union[StrictFloat, StrictInt]] = None, language : Optional[StrictStr] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Get similar movies  # noqa: E501

        Returns list of similar movies based on the provided movieId in a JSON object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.movie_movie_id_similar_get_with_http_info(movie_id, page, language, async_req=True)
        >>> result = thread.get()

        :param movie_id: (required)
        :type movie_id: float
        :param page:
        :type page: float
        :param language:
        :type language: str
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
        :rtype: tuple(DiscoverKeywordKeywordIdMoviesGet200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'movie_id',
            'page',
            'language'
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
                    " to method movie_movie_id_similar_get" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['movie_id'] is not None:
            _path_params['movieId'] = _params['movie_id']


        # process the query parameters
        _query_params = []
        if _params.get('page') is not None:  # noqa: E501
            _query_params.append(('page', _params['page']))

        if _params.get('language') is not None:  # noqa: E501
            _query_params.append(('language', _params['language']))

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
            '200': "DiscoverKeywordKeywordIdMoviesGet200Response",
        }

        return self.api_client.call_api(
            '/movie/{movieId}/similar', 'GET',
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
