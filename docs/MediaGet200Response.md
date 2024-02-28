# MediaGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_info** | [**PageInfo**](PageInfo.md) |  | [optional] 
**results** | [**List[MediaInfo]**](MediaInfo.md) |  | [optional] 

## Example

```python
from overseerr_api.models.media_get200_response import MediaGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MediaGet200Response from a JSON string
media_get200_response_instance = MediaGet200Response.from_json(json)
# print the JSON string representation of the object
print MediaGet200Response.to_json()

# convert the object into a dict
media_get200_response_dict = media_get200_response_instance.to_dict()
# create an instance of MediaGet200Response from a dict
media_get200_response_form_dict = media_get200_response.from_dict(media_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


