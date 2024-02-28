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

from overseerr_api.models.settings_cache_get200_response_image_cache import SettingsCacheGet200ResponseImageCache  # noqa: E501

class TestSettingsCacheGet200ResponseImageCache(unittest.TestCase):
    """SettingsCacheGet200ResponseImageCache unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SettingsCacheGet200ResponseImageCache:
        """Test SettingsCacheGet200ResponseImageCache
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SettingsCacheGet200ResponseImageCache`
        """
        model = SettingsCacheGet200ResponseImageCache()  # noqa: E501
        if include_optional:
            return SettingsCacheGet200ResponseImageCache(
                tmdb = overseerr_api.models._settings_cache_get_200_response_image_cache_tmdb._settings_cache_get_200_response_imageCache_tmdb(
                    image_count = 123, 
                    size = 123456, )
            )
        else:
            return SettingsCacheGet200ResponseImageCache(
        )
        """

    def testSettingsCacheGet200ResponseImageCache(self):
        """Test SettingsCacheGet200ResponseImageCache"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
