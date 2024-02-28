# SettingsPlexSyncGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_library** | [**PlexLibrary**](PlexLibrary.md) |  | [optional] 
**libraries** | [**List[PlexLibrary]**](PlexLibrary.md) |  | [optional] 
**progress** | **float** |  | [optional] 
**running** | **bool** |  | [optional] 
**total** | **float** |  | [optional] 

## Example

```python
from overseerr_api.models.settings_plex_sync_get200_response import SettingsPlexSyncGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SettingsPlexSyncGet200Response from a JSON string
settings_plex_sync_get200_response_instance = SettingsPlexSyncGet200Response.from_json(json)
# print the JSON string representation of the object
print SettingsPlexSyncGet200Response.to_json()

# convert the object into a dict
settings_plex_sync_get200_response_dict = settings_plex_sync_get200_response_instance.to_dict()
# create an instance of SettingsPlexSyncGet200Response from a dict
settings_plex_sync_get200_response_form_dict = settings_plex_sync_get200_response.from_dict(settings_plex_sync_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


