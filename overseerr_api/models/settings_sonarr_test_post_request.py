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

class SettingsSonarrTestPostRequest(BaseModel):
    """
    SettingsSonarrTestPostRequest
    """
    api_key: StrictStr = Field(..., alias="apiKey")
    base_url: Optional[StrictStr] = Field(None, alias="baseUrl")
    hostname: StrictStr = Field(...)
    port: Union[StrictFloat, StrictInt] = Field(...)
    use_ssl: StrictBool = Field(..., alias="useSsl")
    __properties = ["apiKey", "baseUrl", "hostname", "port", "useSsl"]

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
    def from_json(cls, json_str: str) -> SettingsSonarrTestPostRequest:
        """Create an instance of SettingsSonarrTestPostRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SettingsSonarrTestPostRequest:
        """Create an instance of SettingsSonarrTestPostRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SettingsSonarrTestPostRequest.parse_obj(obj)

        _obj = SettingsSonarrTestPostRequest.parse_obj({
            "api_key": obj.get("apiKey"),
            "base_url": obj.get("baseUrl"),
            "hostname": obj.get("hostname"),
            "port": obj.get("port"),
            "use_ssl": obj.get("useSsl")
        })
        return _obj


