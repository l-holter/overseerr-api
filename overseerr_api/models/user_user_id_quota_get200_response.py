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


from typing import Optional
from pydantic import BaseModel
from overseerr_api.models.user_user_id_quota_get200_response_movie import UserUserIdQuotaGet200ResponseMovie

class UserUserIdQuotaGet200Response(BaseModel):
    """
    UserUserIdQuotaGet200Response
    """
    movie: Optional[UserUserIdQuotaGet200ResponseMovie] = None
    tv: Optional[UserUserIdQuotaGet200ResponseMovie] = None
    __properties = ["movie", "tv"]

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
    def from_json(cls, json_str: str) -> UserUserIdQuotaGet200Response:
        """Create an instance of UserUserIdQuotaGet200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of movie
        if self.movie:
            _dict['movie'] = self.movie.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tv
        if self.tv:
            _dict['tv'] = self.tv.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UserUserIdQuotaGet200Response:
        """Create an instance of UserUserIdQuotaGet200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UserUserIdQuotaGet200Response.parse_obj(obj)

        _obj = UserUserIdQuotaGet200Response.parse_obj({
            "movie": UserUserIdQuotaGet200ResponseMovie.from_dict(obj.get("movie")) if obj.get("movie") is not None else None,
            "tv": UserUserIdQuotaGet200ResponseMovie.from_dict(obj.get("tv")) if obj.get("tv") is not None else None
        })
        return _obj


