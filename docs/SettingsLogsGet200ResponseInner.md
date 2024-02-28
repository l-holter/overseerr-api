# SettingsLogsGet200ResponseInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**level** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**timestamp** | **str** |  | [optional] 

## Example

```python
from overseerr_api.models.settings_logs_get200_response_inner import SettingsLogsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of SettingsLogsGet200ResponseInner from a JSON string
settings_logs_get200_response_inner_instance = SettingsLogsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print SettingsLogsGet200ResponseInner.to_json()

# convert the object into a dict
settings_logs_get200_response_inner_dict = settings_logs_get200_response_inner_instance.to_dict()
# create an instance of SettingsLogsGet200ResponseInner from a dict
settings_logs_get200_response_inner_form_dict = settings_logs_get200_response_inner.from_dict(settings_logs_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


