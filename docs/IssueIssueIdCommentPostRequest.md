# IssueIssueIdCommentPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 

## Example

```python
from overseerr_api.models.issue_issue_id_comment_post_request import IssueIssueIdCommentPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IssueIssueIdCommentPostRequest from a JSON string
issue_issue_id_comment_post_request_instance = IssueIssueIdCommentPostRequest.from_json(json)
# print the JSON string representation of the object
print IssueIssueIdCommentPostRequest.to_json()

# convert the object into a dict
issue_issue_id_comment_post_request_dict = issue_issue_id_comment_post_request_instance.to_dict()
# create an instance of IssueIssueIdCommentPostRequest from a dict
issue_issue_id_comment_post_request_form_dict = issue_issue_id_comment_post_request.from_dict(issue_issue_id_comment_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


