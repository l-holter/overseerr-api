# DiscoverSlider


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** |  | 
**enabled** | **bool** |  | 
**id** | **float** |  | [optional] 
**is_built_in** | **bool** |  | [optional] 
**title** | **str** |  | 
**type** | **float** |  | 

## Example

```python
from overseerr_api.models.discover_slider import DiscoverSlider

# TODO update the JSON string below
json = "{}"
# create an instance of DiscoverSlider from a JSON string
discover_slider_instance = DiscoverSlider.from_json(json)
# print the JSON string representation of the object
print DiscoverSlider.to_json()

# convert the object into a dict
discover_slider_dict = discover_slider_instance.to_dict()
# create an instance of DiscoverSlider from a dict
discover_slider_form_dict = discover_slider.from_dict(discover_slider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


