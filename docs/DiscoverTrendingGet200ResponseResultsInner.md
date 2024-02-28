# DiscoverTrendingGet200ResponseResultsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adult** | **bool** |  | [optional] 
**backdrop_path** | **str** |  | [optional] 
**genre_ids** | **List[float]** |  | [optional] 
**id** | **float** |  | 
**media_info** | [**MediaInfo**](MediaInfo.md) |  | [optional] 
**media_type** | **str** |  | [default to 'person']
**original_language** | **str** |  | [optional] 
**original_title** | **str** |  | [optional] 
**overview** | **str** |  | [optional] 
**popularity** | **float** |  | [optional] 
**poster_path** | **str** |  | [optional] 
**release_date** | **str** |  | [optional] 
**title** | **str** |  | 
**video** | **bool** |  | [optional] 
**vote_average** | **float** |  | [optional] 
**vote_count** | **float** |  | [optional] 
**first_air_date** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**origin_country** | **List[str]** |  | [optional] 
**original_name** | **str** |  | [optional] 
**known_for** | [**List[PersonResultKnownForInner]**](PersonResultKnownForInner.md) |  | [optional] 
**profile_path** | **str** |  | [optional] 

## Example

```python
from overseerr_api.models.discover_trending_get200_response_results_inner import DiscoverTrendingGet200ResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DiscoverTrendingGet200ResponseResultsInner from a JSON string
discover_trending_get200_response_results_inner_instance = DiscoverTrendingGet200ResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print DiscoverTrendingGet200ResponseResultsInner.to_json()

# convert the object into a dict
discover_trending_get200_response_results_inner_dict = discover_trending_get200_response_results_inner_instance.to_dict()
# create an instance of DiscoverTrendingGet200ResponseResultsInner from a dict
discover_trending_get200_response_results_inner_form_dict = discover_trending_get200_response_results_inner.from_dict(discover_trending_get200_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


