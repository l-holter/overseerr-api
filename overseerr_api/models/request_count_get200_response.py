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
from pydantic import BaseModel, StrictFloat, StrictInt

class RequestCountGet200Response(BaseModel):
    """
    RequestCountGet200Response
    """
    approved: Optional[Union[StrictFloat, StrictInt]] = None
    available: Optional[Union[StrictFloat, StrictInt]] = None
    declined: Optional[Union[StrictFloat, StrictInt]] = None
    movie: Optional[Union[StrictFloat, StrictInt]] = None
    pending: Optional[Union[StrictFloat, StrictInt]] = None
    processing: Optional[Union[StrictFloat, StrictInt]] = None
    total: Optional[Union[StrictFloat, StrictInt]] = None
    tv: Optional[Union[StrictFloat, StrictInt]] = None
    __properties = ["approved", "available", "declined", "movie", "pending", "processing", "total", "tv"]

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
    def from_json(cls, json_str: str) -> RequestCountGet200Response:
        """Create an instance of RequestCountGet200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RequestCountGet200Response:
        """Create an instance of RequestCountGet200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RequestCountGet200Response.parse_obj(obj)

        _obj = RequestCountGet200Response.parse_obj({
            "approved": obj.get("approved"),
            "available": obj.get("available"),
            "declined": obj.get("declined"),
            "movie": obj.get("movie"),
            "pending": obj.get("pending"),
            "processing": obj.get("processing"),
            "total": obj.get("total"),
            "tv": obj.get("tv")
        })
        return _obj

