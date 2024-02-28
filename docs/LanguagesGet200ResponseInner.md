# LanguagesGet200ResponseInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**english_name** | **str** |  | [optional] 
**iso_639_1** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from overseerr_api.models.languages_get200_response_inner import LanguagesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of LanguagesGet200ResponseInner from a JSON string
languages_get200_response_inner_instance = LanguagesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print LanguagesGet200ResponseInner.to_json()

# convert the object into a dict
languages_get200_response_inner_dict = languages_get200_response_inner_instance.to_dict()
# create an instance of LanguagesGet200ResponseInner from a dict
languages_get200_response_inner_form_dict = languages_get200_response_inner.from_dict(languages_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


