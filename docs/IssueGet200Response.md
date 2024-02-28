# IssueGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_info** | [**PageInfo**](PageInfo.md) |  | [optional] 
**results** | [**List[Issue]**](Issue.md) |  | [optional] 

## Example

```python
from overseerr_api.models.issue_get200_response import IssueGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of IssueGet200Response from a JSON string
issue_get200_response_instance = IssueGet200Response.from_json(json)
# print the JSON string representation of the object
print IssueGet200Response.to_json()

# convert the object into a dict
issue_get200_response_dict = issue_get200_response_instance.to_dict()
# create an instance of IssueGet200Response from a dict
issue_get200_response_form_dict = issue_get200_response.from_dict(issue_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


