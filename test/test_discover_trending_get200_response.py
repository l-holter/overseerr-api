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

from overseerr_api.models.discover_trending_get200_response import DiscoverTrendingGet200Response  # noqa: E501

class TestDiscoverTrendingGet200Response(unittest.TestCase):
    """DiscoverTrendingGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DiscoverTrendingGet200Response:
        """Test DiscoverTrendingGet200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DiscoverTrendingGet200Response`
        """
        model = DiscoverTrendingGet200Response()  # noqa: E501
        if include_optional:
            return DiscoverTrendingGet200Response(
                page = 1,
                results = [
                    null
                    ],
                total_pages = 20,
                total_results = 200
            )
        else:
            return DiscoverTrendingGet200Response(
        )
        """

    def testDiscoverTrendingGet200Response(self):
        """Test DiscoverTrendingGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
