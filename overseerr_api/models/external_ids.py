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

class ExternalIds(BaseModel):
    """
    ExternalIds
    """
    facebook_id: Optional[StrictStr] = Field(None, alias="facebookId")
    freebase_id: Optional[StrictStr] = Field(None, alias="freebaseId")
    freebase_mid: Optional[StrictStr] = Field(None, alias="freebaseMid")
    imdb_id: Optional[StrictStr] = Field(None, alias="imdbId")
    instagram_id: Optional[StrictStr] = Field(None, alias="instagramId")
    tvdb_id: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="tvdbId")
    tvrage_id: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="tvrageId")
    twitter_id: Optional[StrictStr] = Field(None, alias="twitterId")
    __properties = ["facebookId", "freebaseId", "freebaseMid", "imdbId", "instagramId", "tvdbId", "tvrageId", "twitterId"]

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
    def from_json(cls, json_str: str) -> ExternalIds:
        """Create an instance of ExternalIds from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if facebook_id (nullable) is None
        # and __fields_set__ contains the field
        if self.facebook_id is None and "facebook_id" in self.__fields_set__:
            _dict['facebookId'] = None

        # set to None if freebase_id (nullable) is None
        # and __fields_set__ contains the field
        if self.freebase_id is None and "freebase_id" in self.__fields_set__:
            _dict['freebaseId'] = None

        # set to None if freebase_mid (nullable) is None
        # and __fields_set__ contains the field
        if self.freebase_mid is None and "freebase_mid" in self.__fields_set__:
            _dict['freebaseMid'] = None

        # set to None if imdb_id (nullable) is None
        # and __fields_set__ contains the field
        if self.imdb_id is None and "imdb_id" in self.__fields_set__:
            _dict['imdbId'] = None

        # set to None if instagram_id (nullable) is None
        # and __fields_set__ contains the field
        if self.instagram_id is None and "instagram_id" in self.__fields_set__:
            _dict['instagramId'] = None

        # set to None if tvdb_id (nullable) is None
        # and __fields_set__ contains the field
        if self.tvdb_id is None and "tvdb_id" in self.__fields_set__:
            _dict['tvdbId'] = None

        # set to None if tvrage_id (nullable) is None
        # and __fields_set__ contains the field
        if self.tvrage_id is None and "tvrage_id" in self.__fields_set__:
            _dict['tvrageId'] = None

        # set to None if twitter_id (nullable) is None
        # and __fields_set__ contains the field
        if self.twitter_id is None and "twitter_id" in self.__fields_set__:
            _dict['twitterId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ExternalIds:
        """Create an instance of ExternalIds from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ExternalIds.parse_obj(obj)

        _obj = ExternalIds.parse_obj({
            "facebook_id": obj.get("facebookId"),
            "freebase_id": obj.get("freebaseId"),
            "freebase_mid": obj.get("freebaseMid"),
            "imdb_id": obj.get("imdbId"),
            "instagram_id": obj.get("instagramId"),
            "tvdb_id": obj.get("tvdbId"),
            "tvrage_id": obj.get("tvrageId"),
            "twitter_id": obj.get("twitterId")
        })
        return _obj

