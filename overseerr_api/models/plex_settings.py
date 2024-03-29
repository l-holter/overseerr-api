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


from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, conlist
from overseerr_api.models.plex_library import PlexLibrary

class PlexSettings(BaseModel):
    """
    PlexSettings
    """
    ip: StrictStr = Field(...)
    libraries: Optional[conlist(PlexLibrary)] = None
    machine_id: StrictStr = Field(..., alias="machineId")
    name: StrictStr = Field(...)
    port: Union[StrictFloat, StrictInt] = Field(...)
    use_ssl: Optional[StrictBool] = Field(None, alias="useSsl")
    web_app_url: Optional[StrictStr] = Field(None, alias="webAppUrl")
    __properties = ["ip", "libraries", "machineId", "name", "port", "useSsl", "webAppUrl"]

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
    def from_json(cls, json_str: str) -> PlexSettings:
        """Create an instance of PlexSettings from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "libraries",
                            "machine_id",
                            "name",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in libraries (list)
        _items = []
        if self.libraries:
            for _item in self.libraries:
                if _item:
                    _items.append(_item.to_dict())
            _dict['libraries'] = _items
        # set to None if use_ssl (nullable) is None
        # and __fields_set__ contains the field
        if self.use_ssl is None and "use_ssl" in self.__fields_set__:
            _dict['useSsl'] = None

        # set to None if web_app_url (nullable) is None
        # and __fields_set__ contains the field
        if self.web_app_url is None and "web_app_url" in self.__fields_set__:
            _dict['webAppUrl'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PlexSettings:
        """Create an instance of PlexSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PlexSettings.parse_obj(obj)

        _obj = PlexSettings.parse_obj({
            "ip": obj.get("ip"),
            "libraries": [PlexLibrary.from_dict(_item) for _item in obj.get("libraries")] if obj.get("libraries") is not None else None,
            "machine_id": obj.get("machineId"),
            "name": obj.get("name"),
            "port": obj.get("port"),
            "use_ssl": obj.get("useSsl"),
            "web_app_url": obj.get("webAppUrl")
        })
        return _obj


