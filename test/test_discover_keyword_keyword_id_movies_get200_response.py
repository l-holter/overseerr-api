# coding: utf-8

"""
    Overseerr API

    This is the documentation for the Overseerr API backend.  Two primary authentication methods are supported:  - **Cookie Authentication**: A valid sign-in to the `/auth/plex` or `/auth/local` will generate a valid authentication cookie. - **API Key Authentication**: Sign-in is also possible by passing an `X-Api-Key` header along with a valid API Key generated by Overseerr. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from overseerr_api.models.discover_keyword_keyword_id_movies_get200_response import DiscoverKeywordKeywordIdMoviesGet200Response  # noqa: E501

class TestDiscoverKeywordKeywordIdMoviesGet200Response(unittest.TestCase):
    """DiscoverKeywordKeywordIdMoviesGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DiscoverKeywordKeywordIdMoviesGet200Response:
        """Test DiscoverKeywordKeywordIdMoviesGet200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DiscoverKeywordKeywordIdMoviesGet200Response`
        """
        model = DiscoverKeywordKeywordIdMoviesGet200Response()  # noqa: E501
        if include_optional:
            return DiscoverKeywordKeywordIdMoviesGet200Response(
                page = 1,
                results = [
                    overseerr_api.models.movie_result.MovieResult(
                        adult = False, 
                        backdrop_path = '', 
                        genre_ids = [
                            1.337
                            ], 
                        id = 1234, 
                        media_info = overseerr_api.models.media_info.MediaInfo(
                            created_at = '2020-09-12T10:00:27.000Z', 
                            id = 1.337, 
                            requests = [
                                overseerr_api.models.media_request.MediaRequest(
                                    created_at = '2020-09-12T10:00:27.000Z', 
                                    id = 123, 
                                    is4k = False, 
                                    media = overseerr_api.models.media_info.MediaInfo(
                                        created_at = '2020-09-12T10:00:27.000Z', 
                                        id = 1.337, 
                                        status = 0, 
                                        tmdb_id = 1.337, 
                                        tvdb_id = 1.337, 
                                        updated_at = '2020-09-12T10:00:27.000Z', ), 
                                    modified_by = null, 
                                    profile_id = 1.337, 
                                    requested_by = overseerr_api.models.user.User(
                                        avatar = '', 
                                        created_at = '2020-09-02T05:02:23.000Z', 
                                        email = 'hey@itsme.com', 
                                        id = 1, 
                                        permissions = 0, 
                                        plex_token = '', 
                                        plex_username = '', 
                                        request_count = 5, 
                                        updated_at = '2020-09-02T05:02:23.000Z', 
                                        user_type = 1, 
                                        username = '', ), 
                                    root_folder = '', 
                                    server_id = 1.337, 
                                    status = 0, 
                                    updated_at = '2020-09-12T10:00:27.000Z', )
                                ], 
                            status = 0, 
                            tmdb_id = 1.337, 
                            tvdb_id = 1.337, 
                            updated_at = '2020-09-12T10:00:27.000Z', ), 
                        media_type = '', 
                        original_language = 'en', 
                        original_title = 'Original Movie Title', 
                        overview = 'Overview of the movie', 
                        popularity = 10, 
                        poster_path = '', 
                        release_date = '', 
                        title = 'Movie Title', 
                        video = False, 
                        vote_average = 1.337, 
                        vote_count = 1.337, )
                    ],
                total_pages = 20,
                total_results = 200
            )
        else:
            return DiscoverKeywordKeywordIdMoviesGet200Response(
        )
        """

    def testDiscoverKeywordKeywordIdMoviesGet200Response(self):
        """Test DiscoverKeywordKeywordIdMoviesGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()