# AuthResetPasswordGuidPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** |  | 

## Example

```python
from overseerr_api.models.auth_reset_password_guid_post_request import AuthResetPasswordGuidPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthResetPasswordGuidPostRequest from a JSON string
auth_reset_password_guid_post_request_instance = AuthResetPasswordGuidPostRequest.from_json(json)
# print the JSON string representation of the object
print AuthResetPasswordGuidPostRequest.to_json()

# convert the object into a dict
auth_reset_password_guid_post_request_dict = auth_reset_password_guid_post_request_instance.to_dict()
# create an instance of AuthResetPasswordGuidPostRequest from a dict
auth_reset_password_guid_post_request_form_dict = auth_reset_password_guid_post_request.from_dict(auth_reset_password_guid_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


