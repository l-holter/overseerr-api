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


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr

class MainSettings(BaseModel):
    """
    MainSettings
    """
    api_key: Optional[StrictStr] = Field(None, alias="apiKey")
    app_language: Optional[StrictStr] = Field(None, alias="appLanguage")
    application_title: Optional[StrictStr] = Field(None, alias="applicationTitle")
    application_url: Optional[StrictStr] = Field(None, alias="applicationUrl")
    csrf_protection: Optional[StrictBool] = Field(None, alias="csrfProtection")
    default_permissions: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="defaultPermissions")
    hide_available: Optional[StrictBool] = Field(None, alias="hideAvailable")
    local_login: Optional[StrictBool] = Field(None, alias="localLogin")
    new_plex_login: Optional[StrictBool] = Field(None, alias="newPlexLogin")
    partial_requests_enabled: Optional[StrictBool] = Field(None, alias="partialRequestsEnabled")
    trust_proxy: Optional[StrictBool] = Field(None, alias="trustProxy")
    __properties = ["apiKey", "appLanguage", "applicationTitle", "applicationUrl", "csrfProtection", "defaultPermissions", "hideAvailable", "localLogin", "newPlexLogin", "partialRequestsEnabled", "trustProxy"]

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
    def from_json(cls, json_str: str) -> MainSettings:
        """Create an instance of MainSettings from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "api_key",
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MainSettings:
        """Create an instance of MainSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MainSettings.parse_obj(obj)

        _obj = MainSettings.parse_obj({
            "api_key": obj.get("apiKey"),
            "app_language": obj.get("appLanguage"),
            "application_title": obj.get("applicationTitle"),
            "application_url": obj.get("applicationUrl"),
            "csrf_protection": obj.get("csrfProtection"),
            "default_permissions": obj.get("defaultPermissions"),
            "hide_available": obj.get("hideAvailable"),
            "local_login": obj.get("localLogin"),
            "new_plex_login": obj.get("newPlexLogin"),
            "partial_requests_enabled": obj.get("partialRequestsEnabled"),
            "trust_proxy": obj.get("trustProxy")
        })
        return _obj

