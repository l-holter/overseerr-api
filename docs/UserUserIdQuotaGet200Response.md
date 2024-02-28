# UserUserIdQuotaGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**movie** | [**UserUserIdQuotaGet200ResponseMovie**](UserUserIdQuotaGet200ResponseMovie.md) |  | [optional] 
**tv** | [**UserUserIdQuotaGet200ResponseMovie**](UserUserIdQuotaGet200ResponseMovie.md) |  | [optional] 

## Example

```python
from overseerr_api.models.user_user_id_quota_get200_response import UserUserIdQuotaGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UserUserIdQuotaGet200Response from a JSON string
user_user_id_quota_get200_response_instance = UserUserIdQuotaGet200Response.from_json(json)
# print the JSON string representation of the object
print UserUserIdQuotaGet200Response.to_json()

# convert the object into a dict
user_user_id_quota_get200_response_dict = user_user_id_quota_get200_response_instance.to_dict()
# create an instance of UserUserIdQuotaGet200Response from a dict
user_user_id_quota_get200_response_form_dict = user_user_id_quota_get200_response.from_dict(user_user_id_quota_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


