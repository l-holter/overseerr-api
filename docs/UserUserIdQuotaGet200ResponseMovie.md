# UserUserIdQuotaGet200ResponseMovie


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days** | **float** |  | [optional] 
**limit** | **float** |  | [optional] 
**remaining** | **float** |  | [optional] 
**restricted** | **bool** |  | [optional] 
**used** | **float** |  | [optional] 

## Example

```python
from overseerr_api.models.user_user_id_quota_get200_response_movie import UserUserIdQuotaGet200ResponseMovie

# TODO update the JSON string below
json = "{}"
# create an instance of UserUserIdQuotaGet200ResponseMovie from a JSON string
user_user_id_quota_get200_response_movie_instance = UserUserIdQuotaGet200ResponseMovie.from_json(json)
# print the JSON string representation of the object
print UserUserIdQuotaGet200ResponseMovie.to_json()

# convert the object into a dict
user_user_id_quota_get200_response_movie_dict = user_user_id_quota_get200_response_movie_instance.to_dict()
# create an instance of UserUserIdQuotaGet200ResponseMovie from a dict
user_user_id_quota_get200_response_movie_form_dict = user_user_id_quota_get200_response_movie.from_dict(user_user_id_quota_get200_response_movie_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


