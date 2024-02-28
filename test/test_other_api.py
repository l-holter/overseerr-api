# coding: utf-8

"""
    Overseerr API

    This is the documentation for the Overseerr API backend.  Two primary authentication methods are supported:  - **Cookie Authentication**: A valid sign-in to the `/auth/plex` or `/auth/local` will generate a valid authentication cookie. - **API Key Authentication**: Sign-in is also possible by passing an `X-Api-Key` header along with a valid API Key generated by Overseerr. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from overseerr_api.api.other_api import OtherApi  # noqa: E501


class TestOtherApi(unittest.TestCase):
    """OtherApi unit test stubs"""

    def setUp(self) -> None:
        self.api = OtherApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_keyword_keyword_id_get(self) -> None:
        """Test case for keyword_keyword_id_get

        Get keyword  # noqa: E501
        """
        pass

    def test_watchproviders_movies_get(self) -> None:
        """Test case for watchproviders_movies_get

        Get watch provider movies  # noqa: E501
        """
        pass

    def test_watchproviders_regions_get(self) -> None:
        """Test case for watchproviders_regions_get

        Get watch provider regions  # noqa: E501
        """
        pass

    def test_watchproviders_tv_get(self) -> None:
        """Test case for watchproviders_tv_get

        Get watch provider series  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
