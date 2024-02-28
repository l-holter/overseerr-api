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

from overseerr_api.models.tv_result import TvResult  # noqa: E501

class TestTvResult(unittest.TestCase):
    """TvResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvResult:
        """Test TvResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvResult`
        """
        model = TvResult()  # noqa: E501
        if include_optional:
            return TvResult(
                backdrop_path = '',
                first_air_date = '',
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
                name = 'TV Show Name',
                origin_country = [
                    ''
                    ],
                original_language = 'en',
                original_name = 'Original TV Show Name',
                overview = 'Overview of the movie',
                popularity = 10,
                poster_path = '',
                vote_average = 1.337,
                vote_count = 1.337
            )
        else:
            return TvResult(
        )
        """

    def testTvResult(self):
        """Test TvResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
