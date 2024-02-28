# MovieResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adult** | **bool** |  | [optional] 
**backdrop_path** | **str** |  | [optional] 
**genre_ids** | **List[float]** |  | [optional] 
**id** | **float** |  | 
**media_info** | [**MediaInfo**](MediaInfo.md) |  | [optional] 
**media_type** | **str** |  | 
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

## Example

```python
from overseerr_api.models.movie_result import MovieResult

# TODO update the JSON string below
json = "{}"
# create an instance of MovieResult from a JSON string
movie_result_instance = MovieResult.from_json(json)
# print the JSON string representation of the object
print MovieResult.to_json()

# convert the object into a dict
movie_result_dict = movie_result_instance.to_dict()
# create an instance of MovieResult from a dict
movie_result_form_dict = movie_result.from_dict(movie_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


