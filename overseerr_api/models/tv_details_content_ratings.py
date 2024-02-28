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
from overseerr_api.models.tv_details_content_ratings_results_inner import TvDetailsContentRatingsResultsInner

class TvDetailsContentRatings(BaseModel):
    """
    TvDetailsContentRatings
    """
    results: Optional[conlist(TvDetailsContentRatingsResultsInner)] = None
    __properties = ["results"]

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
    def from_json(cls, json_str: str) -> TvDetailsContentRatings:
        """Create an instance of TvDetailsContentRatings from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in results (list)
        _items = []
        if self.results:
            for _item in self.results:
                if _item:
                    _items.append(_item.to_dict())
            _dict['results'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TvDetailsContentRatings:
        """Create an instance of TvDetailsContentRatings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TvDetailsContentRatings.parse_obj(obj)

        _obj = TvDetailsContentRatings.parse_obj({
            "results": [TvDetailsContentRatingsResultsInner.from_dict(_item) for _item in obj.get("results")] if obj.get("results") is not None else None
        })
        return _obj


