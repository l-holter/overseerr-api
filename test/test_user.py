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

from overseerr_api.models.user import User  # noqa: E501

class TestUser(unittest.TestCase):
    """User unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> User:
        """Test User
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `User`
        """
        model = User()  # noqa: E501
        if include_optional:
            return User(
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
                username = ''
            )
        else:
            return User(
                created_at = '2020-09-02T05:02:23.000Z',
                email = 'hey@itsme.com',
                id = 1,
                updated_at = '2020-09-02T05:02:23.000Z',
        )
        """

    def testUser(self):
        """Test User"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
