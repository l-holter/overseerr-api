# TvResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backdrop_path** | **str** |  | [optional] 
**first_air_date** | **str** |  | [optional] 
**genre_ids** | **List[float]** |  | [optional] 
**id** | **float** |  | [optional] 
**media_info** | [**MediaInfo**](MediaInfo.md) |  | [optional] 
**media_type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**origin_country** | **List[str]** |  | [optional] 
**original_language** | **str** |  | [optional] 
**original_name** | **str** |  | [optional] 
**overview** | **str** |  | [optional] 
**popularity** | **float** |  | [optional] 
**poster_path** | **str** |  | [optional] 
**vote_average** | **float** |  | [optional] 
**vote_count** | **float** |  | [optional] 

## Example

```python
from overseerr_api.models.tv_result import TvResult

# TODO update the JSON string below
json = "{}"
# create an instance of TvResult from a JSON string
tv_result_instance = TvResult.from_json(json)
# print the JSON string representation of the object
print TvResult.to_json()

# convert the object into a dict
tv_result_dict = tv_result_instance.to_dict()
# create an instance of TvResult from a dict
tv_result_form_dict = tv_result.from_dict(tv_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


