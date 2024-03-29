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

from overseerr_api.models.user_user_id_settings_password_post_request import UserUserIdSettingsPasswordPostRequest  # noqa: E501

class TestUserUserIdSettingsPasswordPostRequest(unittest.TestCase):
    """UserUserIdSettingsPasswordPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserUserIdSettingsPasswordPostRequest:
        """Test UserUserIdSettingsPasswordPostRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserUserIdSettingsPasswordPostRequest`
        """
        model = UserUserIdSettingsPasswordPostRequest()  # noqa: E501
        if include_optional:
            return UserUserIdSettingsPasswordPostRequest(
                current_password = '',
                new_password = ''
            )
        else:
            return UserUserIdSettingsPasswordPostRequest(
                new_password = '',
        )
        """

    def testUserUserIdSettingsPasswordPostRequest(self):
        """Test UserUserIdSettingsPasswordPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
