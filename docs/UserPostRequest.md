# UserPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**permissions** | **float** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from overseerr_api.models.user_post_request import UserPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserPostRequest from a JSON string
user_post_request_instance = UserPostRequest.from_json(json)
# print the JSON string representation of the object
print UserPostRequest.to_json()

# convert the object into a dict
user_post_request_dict = user_post_request_instance.to_dict()
# create an instance of UserPostRequest from a dict
user_post_request_form_dict = user_post_request.from_dict(user_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


