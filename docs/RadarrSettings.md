# RadarrSettings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_directory** | **str** |  | 
**active_profile_id** | **float** |  | 
**active_profile_name** | **str** |  | 
**api_key** | **str** |  | 
**base_url** | **str** |  | [optional] 
**external_url** | **str** |  | [optional] 
**hostname** | **str** |  | 
**id** | **float** |  | [optional] [readonly] 
**is4k** | **bool** |  | 
**is_default** | **bool** |  | 
**minimum_availability** | **str** |  | 
**name** | **str** |  | 
**port** | **float** |  | 
**prevent_search** | **bool** |  | [optional] 
**sync_enabled** | **bool** |  | [optional] 
**use_ssl** | **bool** |  | 

## Example

```python
from overseerr_api.models.radarr_settings import RadarrSettings

# TODO update the JSON string below
json = "{}"
# create an instance of RadarrSettings from a JSON string
radarr_settings_instance = RadarrSettings.from_json(json)
# print the JSON string representation of the object
print RadarrSettings.to_json()

# convert the object into a dict
radarr_settings_dict = radarr_settings_instance.to_dict()
# create an instance of RadarrSettings from a dict
radarr_settings_form_dict = radarr_settings.from_dict(radarr_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


