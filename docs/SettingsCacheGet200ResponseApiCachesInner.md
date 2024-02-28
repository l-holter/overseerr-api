# SettingsCacheGet200ResponseApiCachesInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**stats** | [**SettingsCacheGet200ResponseApiCachesInnerStats**](SettingsCacheGet200ResponseApiCachesInnerStats.md) |  | [optional] 

## Example

```python
from overseerr_api.models.settings_cache_get200_response_api_caches_inner import SettingsCacheGet200ResponseApiCachesInner

# TODO update the JSON string below
json = "{}"
# create an instance of SettingsCacheGet200ResponseApiCachesInner from a JSON string
settings_cache_get200_response_api_caches_inner_instance = SettingsCacheGet200ResponseApiCachesInner.from_json(json)
# print the JSON string representation of the object
print SettingsCacheGet200ResponseApiCachesInner.to_json()

# convert the object into a dict
settings_cache_get200_response_api_caches_inner_dict = settings_cache_get200_response_api_caches_inner_instance.to_dict()
# create an instance of SettingsCacheGet200ResponseApiCachesInner from a dict
settings_cache_get200_response_api_caches_inner_form_dict = settings_cache_get200_response_api_caches_inner.from_dict(settings_cache_get200_response_api_caches_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


