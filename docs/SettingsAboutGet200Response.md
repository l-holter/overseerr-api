# SettingsAboutGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_data_path** | **str** |  | [optional] 
**total_media_items** | **float** |  | [optional] 
**total_requests** | **float** |  | [optional] 
**tz** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from overseerr_api.models.settings_about_get200_response import SettingsAboutGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SettingsAboutGet200Response from a JSON string
settings_about_get200_response_instance = SettingsAboutGet200Response.from_json(json)
# print the JSON string representation of the object
print SettingsAboutGet200Response.to_json()

# convert the object into a dict
settings_about_get200_response_dict = settings_about_get200_response_instance.to_dict()
# create an instance of SettingsAboutGet200Response from a dict
settings_about_get200_response_form_dict = settings_about_get200_response.from_dict(settings_about_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


