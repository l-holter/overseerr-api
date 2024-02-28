# SettingsCacheGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_caches** | [**List[SettingsCacheGet200ResponseApiCachesInner]**](SettingsCacheGet200ResponseApiCachesInner.md) |  | [optional] 
**image_cache** | [**SettingsCacheGet200ResponseImageCache**](SettingsCacheGet200ResponseImageCache.md) |  | [optional] 

## Example

```python
from overseerr_api.models.settings_cache_get200_response import SettingsCacheGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SettingsCacheGet200Response from a JSON string
settings_cache_get200_response_instance = SettingsCacheGet200Response.from_json(json)
# print the JSON string representation of the object
print SettingsCacheGet200Response.to_json()

# convert the object into a dict
settings_cache_get200_response_dict = settings_cache_get200_response_instance.to_dict()
# create an instance of SettingsCacheGet200Response from a dict
settings_cache_get200_response_form_dict = settings_cache_get200_response.from_dict(settings_cache_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


