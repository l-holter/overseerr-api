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
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr

class Cast(BaseModel):
    """
    Cast
    """
    cast_id: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="castId")
    character: Optional[StrictStr] = None
    credit_id: Optional[StrictStr] = Field(None, alias="creditId")
    gender: Optional[Union[StrictFloat, StrictInt]] = None
    id: Optional[Union[StrictFloat, StrictInt]] = None
    name: Optional[StrictStr] = None
    order: Optional[Union[StrictFloat, StrictInt]] = None
    profile_path: Optional[StrictStr] = Field(None, alias="profilePath")
    __properties = ["castId", "character", "creditId", "gender", "id", "name", "order", "profilePath"]

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
    def from_json(cls, json_str: str) -> Cast:
        """Create an instance of Cast from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if profile_path (nullable) is None
        # and __fields_set__ contains the field
        if self.profile_path is None and "profile_path" in self.__fields_set__:
            _dict['profilePath'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Cast:
        """Create an instance of Cast from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Cast.parse_obj(obj)

        _obj = Cast.parse_obj({
            "cast_id": obj.get("castId"),
            "character": obj.get("character"),
            "credit_id": obj.get("creditId"),
            "gender": obj.get("gender"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "order": obj.get("order"),
            "profile_path": obj.get("profilePath")
        })
        return _obj

