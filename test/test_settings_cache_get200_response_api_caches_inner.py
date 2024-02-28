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

from overseerr_api.models.settings_cache_get200_response_api_caches_inner import SettingsCacheGet200ResponseApiCachesInner  # noqa: E501

class TestSettingsCacheGet200ResponseApiCachesInner(unittest.TestCase):
    """SettingsCacheGet200ResponseApiCachesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SettingsCacheGet200ResponseApiCachesInner:
        """Test SettingsCacheGet200ResponseApiCachesInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SettingsCacheGet200ResponseApiCachesInner`
        """
        model = SettingsCacheGet200ResponseApiCachesInner()  # noqa: E501
        if include_optional:
            return SettingsCacheGet200ResponseApiCachesInner(
                id = 'cache-id',
                name = 'cache name',
                stats = overseerr_api.models._settings_cache_get_200_response_api_caches_inner_stats._settings_cache_get_200_response_apiCaches_inner_stats(
                    hits = 1.337, 
                    keys = 1.337, 
                    ksize = 1.337, 
                    misses = 1.337, 
                    vsize = 1.337, )
            )
        else:
            return SettingsCacheGet200ResponseApiCachesInner(
        )
        """

    def testSettingsCacheGet200ResponseApiCachesInner(self):
        """Test SettingsCacheGet200ResponseApiCachesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()