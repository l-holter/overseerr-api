# RequestRequestIdPutRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is4k** | **bool** |  | [optional] 
**language_profile_id** | **float** |  | [optional] 
**media_type** | **str** |  | 
**profile_id** | **float** |  | [optional] 
**root_folder** | **str** |  | [optional] 
**seasons** | **List[float]** |  | [optional] 
**server_id** | **float** |  | [optional] 
**user_id** | **float** |  | [optional] 

## Example

```python
from overseerr_api.models.request_request_id_put_request import RequestRequestIdPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RequestRequestIdPutRequest from a JSON string
request_request_id_put_request_instance = RequestRequestIdPutRequest.from_json(json)
# print the JSON string representation of the object
print RequestRequestIdPutRequest.to_json()

# convert the object into a dict
request_request_id_put_request_dict = request_request_id_put_request_instance.to_dict()
# create an instance of RequestRequestIdPutRequest from a dict
request_request_id_put_request_form_dict = request_request_id_put_request.from_dict(request_request_id_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


