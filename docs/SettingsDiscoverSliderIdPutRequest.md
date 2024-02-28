# SettingsDiscoverSliderIdPutRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**type** | **float** |  | [optional] 

## Example

```python
from overseerr_api.models.settings_discover_slider_id_put_request import SettingsDiscoverSliderIdPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SettingsDiscoverSliderIdPutRequest from a JSON string
settings_discover_slider_id_put_request_instance = SettingsDiscoverSliderIdPutRequest.from_json(json)
# print the JSON string representation of the object
print SettingsDiscoverSliderIdPutRequest.to_json()

# convert the object into a dict
settings_discover_slider_id_put_request_dict = settings_discover_slider_id_put_request_instance.to_dict()
# create an instance of SettingsDiscoverSliderIdPutRequest from a dict
settings_discover_slider_id_put_request_form_dict = settings_discover_slider_id_put_request.from_dict(settings_discover_slider_id_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


