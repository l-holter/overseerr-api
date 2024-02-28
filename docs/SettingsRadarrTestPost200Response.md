# SettingsRadarrTestPost200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profiles** | [**List[ServiceProfile]**](ServiceProfile.md) |  | [optional] 

## Example

```python
from overseerr_api.models.settings_radarr_test_post200_response import SettingsRadarrTestPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SettingsRadarrTestPost200Response from a JSON string
settings_radarr_test_post200_response_instance = SettingsRadarrTestPost200Response.from_json(json)
# print the JSON string representation of the object
print SettingsRadarrTestPost200Response.to_json()

# convert the object into a dict
settings_radarr_test_post200_response_dict = settings_radarr_test_post200_response_instance.to_dict()
# create an instance of SettingsRadarrTestPost200Response from a dict
settings_radarr_test_post200_response_form_dict = settings_radarr_test_post200_response.from_dict(settings_radarr_test_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


