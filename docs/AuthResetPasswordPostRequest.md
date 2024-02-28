# AuthResetPasswordPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 

## Example

```python
from overseerr_api.models.auth_reset_password_post_request import AuthResetPasswordPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthResetPasswordPostRequest from a JSON string
auth_reset_password_post_request_instance = AuthResetPasswordPostRequest.from_json(json)
# print the JSON string representation of the object
print AuthResetPasswordPostRequest.to_json()

# convert the object into a dict
auth_reset_password_post_request_dict = auth_reset_password_post_request_instance.to_dict()
# create an instance of AuthResetPasswordPostRequest from a dict
auth_reset_password_post_request_form_dict = auth_reset_password_post_request.from_dict(auth_reset_password_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


