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

from overseerr_api.models.settings_notifications_pushover_sounds_get200_response_inner import SettingsNotificationsPushoverSoundsGet200ResponseInner  # noqa: E501

class TestSettingsNotificationsPushoverSoundsGet200ResponseInner(unittest.TestCase):
    """SettingsNotificationsPushoverSoundsGet200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SettingsNotificationsPushoverSoundsGet200ResponseInner:
        """Test SettingsNotificationsPushoverSoundsGet200ResponseInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SettingsNotificationsPushoverSoundsGet200ResponseInner`
        """
        model = SettingsNotificationsPushoverSoundsGet200ResponseInner()  # noqa: E501
        if include_optional:
            return SettingsNotificationsPushoverSoundsGet200ResponseInner(
                description = '',
                name = ''
            )
        else:
            return SettingsNotificationsPushoverSoundsGet200ResponseInner(
        )
        """

    def testSettingsNotificationsPushoverSoundsGet200ResponseInner(self):
        """Test SettingsNotificationsPushoverSoundsGet200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
