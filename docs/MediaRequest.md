# MediaRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] [readonly] 
**id** | **float** |  | [readonly] 
**is4k** | **bool** |  | [optional] 
**media** | [**MediaInfo**](MediaInfo.md) |  | [optional] 
**modified_by** | [**MediaRequestModifiedBy**](MediaRequestModifiedBy.md) |  | [optional] 
**profile_id** | **float** |  | [optional] 
**requested_by** | [**User**](User.md) |  | [optional] 
**root_folder** | **str** |  | [optional] 
**server_id** | **float** |  | [optional] 
**status** | **float** | Status of the request. 1 &#x3D; PENDING APPROVAL, 2 &#x3D; APPROVED, 3 &#x3D; DECLINED | [readonly] 
**updated_at** | **str** |  | [optional] [readonly] 

## Example

```python
from overseerr_api.models.media_request import MediaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MediaRequest from a JSON string
media_request_instance = MediaRequest.from_json(json)
# print the JSON string representation of the object
print MediaRequest.to_json()

# convert the object into a dict
media_request_dict = media_request_instance.to_dict()
# create an instance of MediaRequest from a dict
media_request_form_dict = media_request.from_dict(media_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


