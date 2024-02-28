# UserImportFromPlexPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plex_ids** | **List[str]** |  | [optional] 

## Example

```python
from overseerr_api.models.user_import_from_plex_post_request import UserImportFromPlexPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserImportFromPlexPostRequest from a JSON string
user_import_from_plex_post_request_instance = UserImportFromPlexPostRequest.from_json(json)
# print the JSON string representation of the object
print UserImportFromPlexPostRequest.to_json()

# convert the object into a dict
user_import_from_plex_post_request_dict = user_import_from_plex_post_request_instance.to_dict()
# create an instance of UserImportFromPlexPostRequest from a dict
user_import_from_plex_post_request_form_dict = user_import_from_plex_post_request.from_dict(user_import_from_plex_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


