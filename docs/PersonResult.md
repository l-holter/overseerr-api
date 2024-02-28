# PersonResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adult** | **bool** |  | [optional] 
**id** | **float** |  | [optional] 
**known_for** | [**List[PersonResultKnownForInner]**](PersonResultKnownForInner.md) |  | [optional] 
**media_type** | **str** |  | [optional] [default to 'person']
**profile_path** | **str** |  | [optional] 

## Example

```python
from overseerr_api.models.person_result import PersonResult

# TODO update the JSON string below
json = "{}"
# create an instance of PersonResult from a JSON string
person_result_instance = PersonResult.from_json(json)
# print the JSON string representation of the object
print PersonResult.to_json()

# convert the object into a dict
person_result_dict = person_result_instance.to_dict()
# create an instance of PersonResult from a dict
person_result_form_dict = person_result.from_dict(person_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


