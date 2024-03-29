# coding: utf-8

"""
    Overseerr API

    This is the documentation for the Overseerr API backend.  Two primary authentication methods are supported:  - **Cookie Authentication**: A valid sign-in to the `/auth/plex` or `/auth/local` will generate a valid authentication cookie. - **API Key Authentication**: Sign-in is also possible by passing an `X-Api-Key` header along with a valid API Key generated by Overseerr. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from overseerr_api.api.media_api import MediaApi  # noqa: E501


class TestMediaApi(unittest.TestCase):
    """MediaApi unit test stubs"""

    def setUp(self) -> None:
        self.api = MediaApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_media_get(self) -> None:
        """Test case for media_get

        Get media  # noqa: E501
        """
        pass

    def test_media_media_id_delete(self) -> None:
        """Test case for media_media_id_delete

        Delete media item  # noqa: E501
        """
        pass

    def test_media_media_id_status_post(self) -> None:
        """Test case for media_media_id_status_post

        Update media status  # noqa: E501
        """
        pass

    def test_media_media_id_watch_data_get(self) -> None:
        """Test case for media_media_id_watch_data_get

        Get watch data  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
