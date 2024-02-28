# UserUserIdSettingsPasswordPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_password** | **str** |  | [optional] 
**new_password** | **str** |  | 

## Example

```python
from overseerr_api.models.user_user_id_settings_password_post_request import UserUserIdSettingsPasswordPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserUserIdSettingsPasswordPostRequest from a JSON string
user_user_id_settings_password_post_request_instance = UserUserIdSettingsPasswordPostRequest.from_json(json)
# print the JSON string representation of the object
print UserUserIdSettingsPasswordPostRequest.to_json()

# convert the object into a dict
user_user_id_settings_password_post_request_dict = user_user_id_settings_password_post_request_instance.to_dict()
# create an instance of UserUserIdSettingsPasswordPostRequest from a dict
user_user_id_settings_password_post_request_form_dict = user_user_id_settings_password_post_request.from_dict(user_user_id_settings_password_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


