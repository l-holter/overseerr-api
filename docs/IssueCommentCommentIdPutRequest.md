# IssueCommentCommentIdPutRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 

## Example

```python
from overseerr_api.models.issue_comment_comment_id_put_request import IssueCommentCommentIdPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IssueCommentCommentIdPutRequest from a JSON string
issue_comment_comment_id_put_request_instance = IssueCommentCommentIdPutRequest.from_json(json)
# print the JSON string representation of the object
print IssueCommentCommentIdPutRequest.to_json()

# convert the object into a dict
issue_comment_comment_id_put_request_dict = issue_comment_comment_id_put_request_instance.to_dict()
# create an instance of IssueCommentCommentIdPutRequest from a dict
issue_comment_comment_id_put_request_form_dict = issue_comment_comment_id_put_request.from_dict(issue_comment_comment_id_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


