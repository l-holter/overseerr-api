# RequestPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is4k** | **bool** |  | [optional] 
**language_profile_id** | **float** |  | [optional] 
**media_id** | **float** |  | 
**media_type** | **str** |  | 
**profile_id** | **float** |  | [optional] 
**root_folder** | **str** |  | [optional] 
**seasons** | [**RequestPostRequestSeasons**](RequestPostRequestSeasons.md) |  | [optional] 
**server_id** | **float** |  | [optional] 
**tvdb_id** | **float** |  | [optional] 
**user_id** | **float** |  | [optional] 

## Example

```python
from overseerr_api.models.request_post_request import RequestPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RequestPostRequest from a JSON string
request_post_request_instance = RequestPostRequest.from_json(json)
# print the JSON string representation of the object
print RequestPostRequest.to_json()

# convert the object into a dict
request_post_request_dict = request_post_request_instance.to_dict()
# create an instance of RequestPostRequest from a dict
request_post_request_form_dict = request_post_request.from_dict(request_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


