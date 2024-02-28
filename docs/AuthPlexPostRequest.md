# AuthPlexPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_token** | **str** |  | 

## Example

```python
from overseerr_api.models.auth_plex_post_request import AuthPlexPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthPlexPostRequest from a JSON string
auth_plex_post_request_instance = AuthPlexPostRequest.from_json(json)
# print the JSON string representation of the object
print AuthPlexPostRequest.to_json()

# convert the object into a dict
auth_plex_post_request_dict = auth_plex_post_request_instance.to_dict()
# create an instance of AuthPlexPostRequest from a dict
auth_plex_post_request_form_dict = auth_plex_post_request.from_dict(auth_plex_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


