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
from pydantic import BaseModel, conlist
from overseerr_api.models.cast import Cast
from overseerr_api.models.crew import Crew

class MovieDetailsCredits(BaseModel):
    """
    MovieDetailsCredits
    """
    cast: Optional[conlist(Cast)] = None
    crew: Optional[conlist(Crew)] = None
    __properties = ["cast", "crew"]

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
    def from_json(cls, json_str: str) -> MovieDetailsCredits:
        """Create an instance of MovieDetailsCredits from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in cast (list)
        _items = []
        if self.cast:
            for _item in self.cast:
                if _item:
                    _items.append(_item.to_dict())
            _dict['cast'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in crew (list)
        _items = []
        if self.crew:
            for _item in self.crew:
                if _item:
                    _items.append(_item.to_dict())
            _dict['crew'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MovieDetailsCredits:
        """Create an instance of MovieDetailsCredits from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MovieDetailsCredits.parse_obj(obj)

        _obj = MovieDetailsCredits.parse_obj({
            "cast": [Cast.from_dict(_item) for _item in obj.get("cast")] if obj.get("cast") is not None else None,
            "crew": [Crew.from_dict(_item) for _item in obj.get("crew")] if obj.get("crew") is not None else None
        })
        return _obj


