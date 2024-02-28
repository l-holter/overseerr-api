# DiscoverTvGenreGenreIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**genre** | [**Genre**](Genre.md) |  | [optional] 
**page** | **float** |  | [optional] 
**results** | [**List[TvResult]**](TvResult.md) |  | [optional] 
**total_pages** | **float** |  | [optional] 
**total_results** | **float** |  | [optional] 

## Example

```python
from overseerr_api.models.discover_tv_genre_genre_id_get200_response import DiscoverTvGenreGenreIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DiscoverTvGenreGenreIdGet200Response from a JSON string
discover_tv_genre_genre_id_get200_response_instance = DiscoverTvGenreGenreIdGet200Response.from_json(json)
# print the JSON string representation of the object
print DiscoverTvGenreGenreIdGet200Response.to_json()

# convert the object into a dict
discover_tv_genre_genre_id_get200_response_dict = discover_tv_genre_genre_id_get200_response_instance.to_dict()
# create an instance of DiscoverTvGenreGenreIdGet200Response from a dict
discover_tv_genre_genre_id_get200_response_form_dict = discover_tv_genre_genre_id_get200_response.from_dict(discover_tv_genre_genre_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


