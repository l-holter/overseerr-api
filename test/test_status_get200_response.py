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

from overseerr_api.models.status_get200_response import StatusGet200Response  # noqa: E501

class TestStatusGet200Response(unittest.TestCase):
    """StatusGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StatusGet200Response:
        """Test StatusGet200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StatusGet200Response`
        """
        model = StatusGet200Response()  # noqa: E501
        if include_optional:
            return StatusGet200Response(
                commit_tag = '',
                commits_behind = 1.337,
                restart_required = True,
                update_available = True,
                version = '1.0.0'
            )
        else:
            return StatusGet200Response(
        )
        """

    def testStatusGet200Response(self):
        """Test StatusGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()