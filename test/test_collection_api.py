# coding: utf-8

"""
    Overseerr API

    This is the documentation for the Overseerr API backend.  Two primary authentication methods are supported:  - **Cookie Authentication**: A valid sign-in to the `/auth/plex` or `/auth/local` will generate a valid authentication cookie. - **API Key Authentication**: Sign-in is also possible by passing an `X-Api-Key` header along with a valid API Key generated by Overseerr. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from overseerr_api.api.collection_api import CollectionApi  # noqa: E501


class TestCollectionApi(unittest.TestCase):
    """CollectionApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CollectionApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_collection_collection_id_get(self) -> None:
        """Test case for collection_collection_id_get

        Get collection details  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
