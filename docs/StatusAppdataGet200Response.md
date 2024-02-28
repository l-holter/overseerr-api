# StatusAppdataGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_data** | **bool** |  | [optional] 
**app_data_path** | **str** |  | [optional] 

## Example

```python
from overseerr_api.models.status_appdata_get200_response import StatusAppdataGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of StatusAppdataGet200Response from a JSON string
status_appdata_get200_response_instance = StatusAppdataGet200Response.from_json(json)
# print the JSON string representation of the object
print StatusAppdataGet200Response.to_json()

# convert the object into a dict
status_appdata_get200_response_dict = status_appdata_get200_response_instance.to_dict()
# create an instance of StatusAppdataGet200Response from a dict
status_appdata_get200_response_form_dict = status_appdata_get200_response.from_dict(status_appdata_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


