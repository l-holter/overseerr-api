# SettingsPlexSyncPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancel** | **bool** |  | [optional] 
**start** | **bool** |  | [optional] 

## Example

```python
from overseerr_api.models.settings_plex_sync_post_request import SettingsPlexSyncPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SettingsPlexSyncPostRequest from a JSON string
settings_plex_sync_post_request_instance = SettingsPlexSyncPostRequest.from_json(json)
# print the JSON string representation of the object
print SettingsPlexSyncPostRequest.to_json()

# convert the object into a dict
settings_plex_sync_post_request_dict = settings_plex_sync_post_request_instance.to_dict()
# create an instance of SettingsPlexSyncPostRequest from a dict
settings_plex_sync_post_request_form_dict = settings_plex_sync_post_request.from_dict(settings_plex_sync_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


