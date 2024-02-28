# SettingsDiscoverAddPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**type** | **float** |  | [optional] 

## Example

```python
from overseerr_api.models.settings_discover_add_post_request import SettingsDiscoverAddPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SettingsDiscoverAddPostRequest from a JSON string
settings_discover_add_post_request_instance = SettingsDiscoverAddPostRequest.from_json(json)
# print the JSON string representation of the object
print SettingsDiscoverAddPostRequest.to_json()

# convert the object into a dict
settings_discover_add_post_request_dict = settings_discover_add_post_request_instance.to_dict()
# create an instance of SettingsDiscoverAddPostRequest from a dict
settings_discover_add_post_request_form_dict = settings_discover_add_post_request.from_dict(settings_discover_add_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


