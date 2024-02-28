# coding: utf-8

"""
    Overseerr API

    This is the documentation for the Overseerr API backend.  Two primary authentication methods are supported:  - **Cookie Authentication**: A valid sign-in to the `/auth/plex` or `/auth/local` will generate a valid authentication cookie. - **API Key Authentication**: Sign-in is also possible by passing an `X-Api-Key` header along with a valid API Key generated by Overseerr. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, conlist
from overseerr_api.models.settings_cache_get200_response_api_caches_inner import SettingsCacheGet200ResponseApiCachesInner
from overseerr_api.models.settings_cache_get200_response_image_cache import SettingsCacheGet200ResponseImageCache

class SettingsCacheGet200Response(BaseModel):
    """
    SettingsCacheGet200Response
    """
    api_caches: Optional[conlist(SettingsCacheGet200ResponseApiCachesInner)] = Field(None, alias="apiCaches")
    image_cache: Optional[SettingsCacheGet200ResponseImageCache] = Field(None, alias="imageCache")
    __properties = ["apiCaches", "imageCache"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> SettingsCacheGet200Response:
        """Create an instance of SettingsCacheGet200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in api_caches (list)
        _items = []
        if self.api_caches:
            for _item in self.api_caches:
                if _item:
                    _items.append(_item.to_dict())
            _dict['apiCaches'] = _items
        # override the default output from pydantic by calling `to_dict()` of image_cache
        if self.image_cache:
            _dict['imageCache'] = self.image_cache.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SettingsCacheGet200Response:
        """Create an instance of SettingsCacheGet200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SettingsCacheGet200Response.parse_obj(obj)

        _obj = SettingsCacheGet200Response.parse_obj({
            "api_caches": [SettingsCacheGet200ResponseApiCachesInner.from_dict(_item) for _item in obj.get("apiCaches")] if obj.get("apiCaches") is not None else None,
            "image_cache": SettingsCacheGet200ResponseImageCache.from_dict(obj.get("imageCache")) if obj.get("imageCache") is not None else None
        })
        return _obj


