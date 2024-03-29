# coding: utf-8

"""
    Overseerr API

    This is the documentation for the Overseerr API backend.  Two primary authentication methods are supported:  - **Cookie Authentication**: A valid sign-in to the `/auth/plex` or `/auth/local` will generate a valid authentication cookie. - **API Key Authentication**: Sign-in is also possible by passing an `X-Api-Key` header along with a valid API Key generated by Overseerr. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, validator
from overseerr_api.models.movie_result import MovieResult
from overseerr_api.models.tv_result import TvResult
from typing import Union, Any, List, TYPE_CHECKING
from pydantic import StrictStr, Field

PERSONRESULTKNOWNFORINNER_ONE_OF_SCHEMAS = ["MovieResult", "TvResult"]

class PersonResultKnownForInner(BaseModel):
    """
    PersonResultKnownForInner
    """
    # data type: MovieResult
    oneof_schema_1_validator: Optional[MovieResult] = None
    # data type: TvResult
    oneof_schema_2_validator: Optional[TvResult] = None
    if TYPE_CHECKING:
        actual_instance: Union[MovieResult, TvResult]
    else:
        actual_instance: Any
    one_of_schemas: List[str] = Field(PERSONRESULTKNOWNFORINNER_ONE_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = PersonResultKnownForInner.construct()
        error_messages = []
        match = 0
        # validate data type: MovieResult
        if not isinstance(v, MovieResult):
            error_messages.append(f"Error! Input type `{type(v)}` is not `MovieResult`")
        else:
            match += 1
        # validate data type: TvResult
        if not isinstance(v, TvResult):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TvResult`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in PersonResultKnownForInner with oneOf schemas: MovieResult, TvResult. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in PersonResultKnownForInner with oneOf schemas: MovieResult, TvResult. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> PersonResultKnownForInner:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> PersonResultKnownForInner:
        """Returns the object represented by the json string"""
        instance = PersonResultKnownForInner.construct()
        error_messages = []
        match = 0

        # deserialize data into MovieResult
        try:
            instance.actual_instance = MovieResult.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TvResult
        try:
            instance.actual_instance = TvResult.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into PersonResultKnownForInner with oneOf schemas: MovieResult, TvResult. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into PersonResultKnownForInner with oneOf schemas: MovieResult, TvResult. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        to_dict = getattr(self.actual_instance, "to_dict", None)
        if callable(to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.dict())


