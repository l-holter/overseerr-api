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

from overseerr_api.models.movie_details import MovieDetails  # noqa: E501

class TestMovieDetails(unittest.TestCase):
    """MovieDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MovieDetails:
        """Test MovieDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MovieDetails`
        """
        model = MovieDetails()  # noqa: E501
        if include_optional:
            return MovieDetails(
                adult = True,
                backdrop_path = '',
                budget = 1000000,
                collection = overseerr_api.models.movie_details_collection.MovieDetails_collection(
                    backdrop_path = '', 
                    id = 1, 
                    name = 'A collection', 
                    poster_path = '', ),
                credits = overseerr_api.models.movie_details_credits.MovieDetails_credits(
                    cast = [
                        overseerr_api.models.cast.Cast(
                            cast_id = 1, 
                            character = 'Some Character Name', 
                            credit_id = '', 
                            gender = 1.337, 
                            id = 123, 
                            name = 'Some Persons Name', 
                            order = 1.337, 
                            profile_path = '', )
                        ], 
                    crew = [
                        overseerr_api.models.crew.Crew(
                            credit_id = '', 
                            department = '', 
                            gender = 1.337, 
                            id = 123, 
                            job = '', 
                            name = 'Some Persons Name', 
                            profile_path = '', )
                        ], ),
                external_ids = overseerr_api.models.external_ids.ExternalIds(
                    facebook_id = '', 
                    freebase_id = '', 
                    freebase_mid = '', 
                    imdb_id = '', 
                    instagram_id = '', 
                    tvdb_id = 1.337, 
                    tvrage_id = 1.337, 
                    twitter_id = '', ),
                genres = [
                    overseerr_api.models.genre.Genre(
                        id = 1, 
                        name = 'Adventure', )
                    ],
                homepage = '',
                id = 123,
                imdb_id = 'tt123',
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
                original_language = '',
                original_title = '',
                overview = '',
                popularity = 1.337,
                poster_path = '',
                production_companies = [
                    overseerr_api.models.production_company.ProductionCompany(
                        id = 1, 
                        logo_path = '', 
                        name = '', 
                        origin_country = '', )
                    ],
                production_countries = [
                    overseerr_api.models.movie_details_production_countries_inner.MovieDetails_productionCountries_inner(
                        iso_3166_1 = '', 
                        name = '', )
                    ],
                related_videos = [
                    overseerr_api.models.related_video.RelatedVideo(
                        key = '9qhL2_UxXM0', 
                        name = 'Trailer for some movie (1978)', 
                        site = 'YouTube', 
                        size = 1080, 
                        type = 'Trailer', 
                        url = 'https://www.youtube.com/watch?v=9qhL2_UxXM0/', )
                    ],
                release_date = '',
                releases = overseerr_api.models.movie_details_releases.MovieDetails_releases(
                    results = [
                        overseerr_api.models.movie_details_releases_results_inner.MovieDetails_releases_results_inner(
                            iso_3166_1 = 'US', 
                            rating = '', 
                            release_dates = [
                                overseerr_api.models.movie_details_releases_results_inner_release_dates_inner.MovieDetails_releases_results_inner_release_dates_inner(
                                    certification = 'PG-13', 
                                    iso_639_1 = '', 
                                    note = 'Blu ray', 
                                    release_date = '2017-07-12T00:00:00.000Z', 
                                    type = 1, )
                                ], )
                        ], ),
                revenue = 1.337,
                runtime = 1.337,
                spoken_languages = [
                    overseerr_api.models.spoken_language.SpokenLanguage(
                        english_name = 'English', 
                        iso_639_1 = 'en', 
                        name = 'English', )
                    ],
                status = '',
                tagline = '',
                title = '',
                video = True,
                vote_average = 1.337,
                vote_count = 1.337,
                watch_providers = [
                    [
                        overseerr_api.models.watch_providers_inner.WatchProviders_inner(
                            buy = [
                                overseerr_api.models.watch_provider_details.WatchProviderDetails(
                                    display_priority = 1.337, 
                                    id = 1.337, 
                                    logo_path = '', 
                                    name = '', )
                                ], 
                            flatrate = [
                                overseerr_api.models.watch_provider_details.WatchProviderDetails(
                                    display_priority = 1.337, 
                                    id = 1.337, 
                                    logo_path = '', 
                                    name = '', )
                                ], 
                            iso_3166_1 = '', 
                            link = '', )
                        ]
                    ]
            )
        else:
            return MovieDetails(
        )
        """

    def testMovieDetails(self):
        """Test MovieDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
