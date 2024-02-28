# Season


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**air_date** | **str** |  | [optional] 
**episode_count** | **float** |  | [optional] 
**episodes** | [**List[Episode]**](Episode.md) |  | [optional] 
**id** | **float** |  | [optional] 
**name** | **str** |  | [optional] 
**overview** | **str** |  | [optional] 
**poster_path** | **str** |  | [optional] 
**season_number** | **float** |  | [optional] 

## Example

```python
from overseerr_api.models.season import Season

# TODO update the JSON string below
json = "{}"
# create an instance of Season from a JSON string
season_instance = Season.from_json(json)
# print the JSON string representation of the object
print Season.to_json()

# convert the object into a dict
season_dict = season_instance.to_dict()
# create an instance of Season from a dict
season_form_dict = season.from_dict(season_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


