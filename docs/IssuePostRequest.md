# IssuePostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issue_type** | **float** |  | [optional] 
**media_id** | **float** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from overseerr_api.models.issue_post_request import IssuePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IssuePostRequest from a JSON string
issue_post_request_instance = IssuePostRequest.from_json(json)
# print the JSON string representation of the object
print IssuePostRequest.to_json()

# convert the object into a dict
issue_post_request_dict = issue_post_request_instance.to_dict()
# create an instance of IssuePostRequest from a dict
issue_post_request_form_dict = issue_post_request.from_dict(issue_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


