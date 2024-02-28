# RegionsGet200ResponseInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**english_name** | **str** |  | [optional] 
**iso_3166_1** | **str** |  | [optional] 

## Example

```python
from overseerr_api.models.regions_get200_response_inner import RegionsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RegionsGet200ResponseInner from a JSON string
regions_get200_response_inner_instance = RegionsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print RegionsGet200ResponseInner.to_json()

# convert the object into a dict
regions_get200_response_inner_dict = regions_get200_response_inner_instance.to_dict()
# create an instance of RegionsGet200ResponseInner from a dict
regions_get200_response_inner_form_dict = regions_get200_response_inner.from_dict(regions_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


