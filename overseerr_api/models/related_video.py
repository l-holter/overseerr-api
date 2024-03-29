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
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr, validator

class RelatedVideo(BaseModel):
    """
    RelatedVideo
    """
    key: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    site: Optional[StrictStr] = None
    size: Optional[Union[StrictFloat, StrictInt]] = None
    type: Optional[StrictStr] = None
    url: Optional[StrictStr] = None
    __properties = ["key", "name", "site", "size", "type", "url"]

    @validator('site')
    def site_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('YouTube'):
            raise ValueError("must be one of enum values ('YouTube')")
        return value

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Clip', 'Teaser', 'Trailer', 'Featurette', 'Opening Credits', 'Behind the Scenes', 'Bloopers'):
            raise ValueError("must be one of enum values ('Clip', 'Teaser', 'Trailer', 'Featurette', 'Opening Credits', 'Behind the Scenes', 'Bloopers')")
        return value

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
    def from_json(cls, json_str: str) -> RelatedVideo:
        """Create an instance of RelatedVideo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RelatedVideo:
        """Create an instance of RelatedVideo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RelatedVideo.parse_obj(obj)

        _obj = RelatedVideo.parse_obj({
            "key": obj.get("key"),
            "name": obj.get("name"),
            "site": obj.get("site"),
            "size": obj.get("size"),
            "type": obj.get("type"),
            "url": obj.get("url")
        })
        return _obj


