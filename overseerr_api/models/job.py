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
from pydantic import BaseModel, Field, StrictBool, StrictStr, validator

class Job(BaseModel):
    """
    Job
    """
    id: Optional[StrictStr] = None
    interval: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    next_execution_time: Optional[StrictStr] = Field(None, alias="nextExecutionTime")
    running: Optional[StrictBool] = None
    type: Optional[StrictStr] = None
    __properties = ["id", "interval", "name", "nextExecutionTime", "running", "type"]

    @validator('interval')
    def interval_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('short', 'long', 'fixed'):
            raise ValueError("must be one of enum values ('short', 'long', 'fixed')")
        return value

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('process', 'command'):
            raise ValueError("must be one of enum values ('process', 'command')")
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
    def from_json(cls, json_str: str) -> Job:
        """Create an instance of Job from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Job:
        """Create an instance of Job from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Job.parse_obj(obj)

        _obj = Job.parse_obj({
            "id": obj.get("id"),
            "interval": obj.get("interval"),
            "name": obj.get("name"),
            "next_execution_time": obj.get("nextExecutionTime"),
            "running": obj.get("running"),
            "type": obj.get("type")
        })
        return _obj


