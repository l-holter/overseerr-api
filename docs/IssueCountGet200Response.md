# IssueCountGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audio** | **float** |  | [optional] 
**closed** | **float** |  | [optional] 
**open** | **float** |  | [optional] 
**others** | **float** |  | [optional] 
**subtitles** | **float** |  | [optional] 
**total** | **float** |  | [optional] 
**video** | **float** |  | [optional] 

## Example

```python
from overseerr_api.models.issue_count_get200_response import IssueCountGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of IssueCountGet200Response from a JSON string
issue_count_get200_response_instance = IssueCountGet200Response.from_json(json)
# print the JSON string representation of the object
print IssueCountGet200Response.to_json()

# convert the object into a dict
issue_count_get200_response_dict = issue_count_get200_response_instance.to_dict()
# create an instance of IssueCountGet200Response from a dict
issue_count_get200_response_form_dict = issue_count_get200_response.from_dict(issue_count_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


