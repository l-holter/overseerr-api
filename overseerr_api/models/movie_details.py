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
from overseerr_api.models.external_ids import ExternalIds
from overseerr_api.models.genre import Genre
from overseerr_api.models.media_info import MediaInfo
from overseerr_api.models.movie_details_collection import MovieDetailsCollection
from overseerr_api.models.movie_details_credits import MovieDetailsCredits
from overseerr_api.models.movie_details_production_countries_inner import MovieDetailsProductionCountriesInner
from overseerr_api.models.movie_details_releases import MovieDetailsReleases
from overseerr_api.models.production_company import ProductionCompany
from overseerr_api.models.related_video import RelatedVideo
from overseerr_api.models.spoken_language import SpokenLanguage
from overseerr_api.models.watch_providers_inner import WatchProvidersInner

class MovieDetails(BaseModel):
    """
    MovieDetails
    """
    adult: Optional[StrictBool] = None
    backdrop_path: Optional[StrictStr] = Field(None, alias="backdropPath")
    budget: Optional[Union[StrictFloat, StrictInt]] = None
    collection: Optional[MovieDetailsCollection] = None
    credits: Optional[MovieDetailsCredits] = None
    external_ids: Optional[ExternalIds] = Field(None, alias="externalIds")
    genres: Optional[conlist(Genre)] = None
    homepage: Optional[StrictStr] = None
    id: Optional[Union[StrictFloat, StrictInt]] = None
    imdb_id: Optional[StrictStr] = Field(None, alias="imdbId")
    media_info: Optional[MediaInfo] = Field(None, alias="mediaInfo")
    original_language: Optional[StrictStr] = Field(None, alias="originalLanguage")
    original_title: Optional[StrictStr] = Field(None, alias="originalTitle")
    overview: Optional[StrictStr] = None
    popularity: Optional[Union[StrictFloat, StrictInt]] = None
    poster_path: Optional[StrictStr] = Field(None, alias="posterPath")
    production_companies: Optional[conlist(ProductionCompany)] = Field(None, alias="productionCompanies")
    production_countries: Optional[conlist(MovieDetailsProductionCountriesInner)] = Field(None, alias="productionCountries")
    related_videos: Optional[conlist(RelatedVideo)] = Field(None, alias="relatedVideos")
    release_date: Optional[StrictStr] = Field(None, alias="releaseDate")
    releases: Optional[MovieDetailsReleases] = None
    revenue: Optional[Union[StrictFloat, StrictInt]] = None
    runtime: Optional[Union[StrictFloat, StrictInt]] = None
    spoken_languages: Optional[conlist(SpokenLanguage)] = Field(None, alias="spokenLanguages")
    status: Optional[StrictStr] = None
    tagline: Optional[StrictStr] = None
    title: Optional[StrictStr] = None
    video: Optional[StrictBool] = None
    vote_average: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="voteAverage")
    vote_count: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="voteCount")
    watch_providers: Optional[conlist(conlist(WatchProvidersInner))] = Field(None, alias="watchProviders")
    __properties = ["adult", "backdropPath", "budget", "collection", "credits", "externalIds", "genres", "homepage", "id", "imdbId", "mediaInfo", "originalLanguage", "originalTitle", "overview", "popularity", "posterPath", "productionCompanies", "productionCountries", "relatedVideos", "releaseDate", "releases", "revenue", "runtime", "spokenLanguages", "status", "tagline", "title", "video", "voteAverage", "voteCount", "watchProviders"]

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
    def from_json(cls, json_str: str) -> MovieDetails:
        """Create an instance of MovieDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "id",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of collection
        if self.collection:
            _dict['collection'] = self.collection.to_dict()
        # override the default output from pydantic by calling `to_dict()` of credits
        if self.credits:
            _dict['credits'] = self.credits.to_dict()
        # override the default output from pydantic by calling `to_dict()` of external_ids
        if self.external_ids:
            _dict['externalIds'] = self.external_ids.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in genres (list)
        _items = []
        if self.genres:
            for _item in self.genres:
                if _item:
                    _items.append(_item.to_dict())
            _dict['genres'] = _items
        # override the default output from pydantic by calling `to_dict()` of media_info
        if self.media_info:
            _dict['mediaInfo'] = self.media_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in production_companies (list)
        _items = []
        if self.production_companies:
            for _item in self.production_companies:
                if _item:
                    _items.append(_item.to_dict())
            _dict['productionCompanies'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in production_countries (list)
        _items = []
        if self.production_countries:
            for _item in self.production_countries:
                if _item:
                    _items.append(_item.to_dict())
            _dict['productionCountries'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in related_videos (list)
        _items = []
        if self.related_videos:
            for _item in self.related_videos:
                if _item:
                    _items.append(_item.to_dict())
            _dict['relatedVideos'] = _items
        # override the default output from pydantic by calling `to_dict()` of releases
        if self.releases:
            _dict['releases'] = self.releases.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in spoken_languages (list)
        _items = []
        if self.spoken_languages:
            for _item in self.spoken_languages:
                if _item:
                    _items.append(_item.to_dict())
            _dict['spokenLanguages'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in watch_providers (list of list)
        _items = []
        if self.watch_providers:
            for _item in self.watch_providers:
                if _item:
                    _items.append(
                         [_inner_item.to_dict() for _inner_item in _item if _inner_item is not None]
                    )
            _dict['watchProviders'] = _items
        # set to None if revenue (nullable) is None
        # and __fields_set__ contains the field
        if self.revenue is None and "revenue" in self.__fields_set__:
            _dict['revenue'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MovieDetails:
        """Create an instance of MovieDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MovieDetails.parse_obj(obj)

        _obj = MovieDetails.parse_obj({
            "adult": obj.get("adult"),
            "backdrop_path": obj.get("backdropPath"),
            "budget": obj.get("budget"),
            "collection": MovieDetailsCollection.from_dict(obj.get("collection")) if obj.get("collection") is not None else None,
            "credits": MovieDetailsCredits.from_dict(obj.get("credits")) if obj.get("credits") is not None else None,
            "external_ids": ExternalIds.from_dict(obj.get("externalIds")) if obj.get("externalIds") is not None else None,
            "genres": [Genre.from_dict(_item) for _item in obj.get("genres")] if obj.get("genres") is not None else None,
            "homepage": obj.get("homepage"),
            "id": obj.get("id"),
            "imdb_id": obj.get("imdbId"),
            "media_info": MediaInfo.from_dict(obj.get("mediaInfo")) if obj.get("mediaInfo") is not None else None,
            "original_language": obj.get("originalLanguage"),
            "original_title": obj.get("originalTitle"),
            "overview": obj.get("overview"),
            "popularity": obj.get("popularity"),
            "poster_path": obj.get("posterPath"),
            "production_companies": [ProductionCompany.from_dict(_item) for _item in obj.get("productionCompanies")] if obj.get("productionCompanies") is not None else None,
            "production_countries": [MovieDetailsProductionCountriesInner.from_dict(_item) for _item in obj.get("productionCountries")] if obj.get("productionCountries") is not None else None,
            "related_videos": [RelatedVideo.from_dict(_item) for _item in obj.get("relatedVideos")] if obj.get("relatedVideos") is not None else None,
            "release_date": obj.get("releaseDate"),
            "releases": MovieDetailsReleases.from_dict(obj.get("releases")) if obj.get("releases") is not None else None,
            "revenue": obj.get("revenue"),
            "runtime": obj.get("runtime"),
            "spoken_languages": [SpokenLanguage.from_dict(_item) for _item in obj.get("spokenLanguages")] if obj.get("spokenLanguages") is not None else None,
            "status": obj.get("status"),
            "tagline": obj.get("tagline"),
            "title": obj.get("title"),
            "video": obj.get("video"),
            "vote_average": obj.get("voteAverage"),
            "vote_count": obj.get("voteCount"),
            "watch_providers": [
                    [WatchProvidersInner.from_dict(_inner_item) for _inner_item in _item]
                    for _item in obj.get("watchProviders")
                ] if obj.get("watchProviders") is not None else None
        })
        return _obj


