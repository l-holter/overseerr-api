# PersonResultKnownForInner


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
**first_air_date** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**origin_country** | **List[str]** |  | [optional] 
**original_name** | **str** |  | [optional] 

## Example

```python
from overseerr_api.models.person_result_known_for_inner import PersonResultKnownForInner

# TODO update the JSON string below
json = "{}"
# create an instance of PersonResultKnownForInner from a JSON string
person_result_known_for_inner_instance = PersonResultKnownForInner.from_json(json)
# print the JSON string representation of the object
print PersonResultKnownForInner.to_json()

# convert the object into a dict
person_result_known_for_inner_dict = person_result_known_for_inner_instance.to_dict()
# create an instance of PersonResultKnownForInner from a dict
person_result_known_for_inner_form_dict = person_result_known_for_inner.from_dict(person_result_known_for_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


