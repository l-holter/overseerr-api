# SettingsRadarrTestPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** |  | 
**base_url** | **str** |  | [optional] 
**hostname** | **str** |  | 
**port** | **float** |  | 
**use_ssl** | **bool** |  | 

## Example

```python
from overseerr_api.models.settings_radarr_test_post_request import SettingsRadarrTestPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SettingsRadarrTestPostRequest from a JSON string
settings_radarr_test_post_request_instance = SettingsRadarrTestPostRequest.from_json(json)
# print the JSON string representation of the object
print SettingsRadarrTestPostRequest.to_json()

# convert the object into a dict
settings_radarr_test_post_request_dict = settings_radarr_test_post_request_instance.to_dict()
# create an instance of SettingsRadarrTestPostRequest from a dict
settings_radarr_test_post_request_form_dict = settings_radarr_test_post_request.from_dict(settings_radarr_test_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


