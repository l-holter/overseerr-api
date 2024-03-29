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

from overseerr_api.models.request_count_get200_response import RequestCountGet200Response  # noqa: E501

class TestRequestCountGet200Response(unittest.TestCase):
    """RequestCountGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RequestCountGet200Response:
        """Test RequestCountGet200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RequestCountGet200Response`
        """
        model = RequestCountGet200Response()  # noqa: E501
        if include_optional:
            return RequestCountGet200Response(
                approved = 1.337,
                available = 1.337,
                declined = 1.337,
                movie = 1.337,
                pending = 1.337,
                processing = 1.337,
                total = 1.337,
                tv = 1.337
            )
        else:
            return RequestCountGet200Response(
        )
        """

    def testRequestCountGet200Response(self):
        """Test RequestCountGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
