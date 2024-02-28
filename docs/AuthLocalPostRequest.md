# AuthLocalPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**password** | **str** |  | 

## Example

```python
from overseerr_api.models.auth_local_post_request import AuthLocalPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthLocalPostRequest from a JSON string
auth_local_post_request_instance = AuthLocalPostRequest.from_json(json)
# print the JSON string representation of the object
print AuthLocalPostRequest.to_json()

# convert the object into a dict
auth_local_post_request_dict = auth_local_post_request_instance.to_dict()
# create an instance of AuthLocalPostRequest from a dict
auth_local_post_request_form_dict = auth_local_post_request.from_dict(auth_local_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


