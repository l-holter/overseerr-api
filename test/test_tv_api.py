# coding: utf-8

"""
    Overseerr API

    This is the documentation for the Overseerr API backend.  Two primary authentication methods are supported:  - **Cookie Authentication**: A valid sign-in to the `/auth/plex` or `/auth/local` will generate a valid authentication cookie. - **API Key Authentication**: Sign-in is also possible by passing an `X-Api-Key` header along with a valid API Key generated by Overseerr. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from overseerr_api.api.tv_api import TvApi  # noqa: E501


class TestTvApi(unittest.TestCase):
    """TvApi unit test stubs"""

    def setUp(self) -> None:
        self.api = TvApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_tv_tv_id_get(self) -> None:
        """Test case for tv_tv_id_get

        Get TV details  # noqa: E501
        """
        pass

    def test_tv_tv_id_ratings_get(self) -> None:
        """Test case for tv_tv_id_ratings_get

        Get TV ratings  # noqa: E501
        """
        pass

    def test_tv_tv_id_recommendations_get(self) -> None:
        """Test case for tv_tv_id_recommendations_get

        Get recommended TV series  # noqa: E501
        """
        pass

    def test_tv_tv_id_season_season_id_get(self) -> None:
        """Test case for tv_tv_id_season_season_id_get

        Get season details and episode list  # noqa: E501
        """
        pass

    def test_tv_tv_id_similar_get(self) -> None:
        """Test case for tv_tv_id_similar_get

        Get similar TV series  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
