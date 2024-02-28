# LunaSeaSettings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 
**options** | [**LunaSeaSettingsOptions**](LunaSeaSettingsOptions.md) |  | [optional] 
**types** | **float** |  | [optional] 

## Example

```python
from overseerr_api.models.luna_sea_settings import LunaSeaSettings

# TODO update the JSON string below
json = "{}"
# create an instance of LunaSeaSettings from a JSON string
luna_sea_settings_instance = LunaSeaSettings.from_json(json)
# print the JSON string representation of the object
print LunaSeaSettings.to_json()

# convert the object into a dict
luna_sea_settings_dict = luna_sea_settings_instance.to_dict()
# create an instance of LunaSeaSettings from a dict
luna_sea_settings_form_dict = luna_sea_settings.from_dict(luna_sea_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


