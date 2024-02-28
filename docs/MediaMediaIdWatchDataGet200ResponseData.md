# MediaMediaIdWatchDataGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**play_count** | **float** |  | [optional] 
**play_count30_days** | **float** |  | [optional] 
**play_count7_days** | **float** |  | [optional] 
**users** | [**List[User]**](User.md) |  | [optional] 

## Example

```python
from overseerr_api.models.media_media_id_watch_data_get200_response_data import MediaMediaIdWatchDataGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of MediaMediaIdWatchDataGet200ResponseData from a JSON string
media_media_id_watch_data_get200_response_data_instance = MediaMediaIdWatchDataGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print MediaMediaIdWatchDataGet200ResponseData.to_json()

# convert the object into a dict
media_media_id_watch_data_get200_response_data_dict = media_media_id_watch_data_get200_response_data_instance.to_dict()
# create an instance of MediaMediaIdWatchDataGet200ResponseData from a dict
media_media_id_watch_data_get200_response_data_form_dict = media_media_id_watch_data_get200_response_data.from_dict(media_media_id_watch_data_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


