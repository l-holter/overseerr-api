# StatusGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commit_tag** | **str** |  | [optional] 
**commits_behind** | **float** |  | [optional] 
**restart_required** | **bool** |  | [optional] 
**update_available** | **bool** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from overseerr_api.models.status_get200_response import StatusGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of StatusGet200Response from a JSON string
status_get200_response_instance = StatusGet200Response.from_json(json)
# print the JSON string representation of the object
print StatusGet200Response.to_json()

# convert the object into a dict
status_get200_response_dict = status_get200_response_instance.to_dict()
# create an instance of StatusGet200Response from a dict
status_get200_response_form_dict = status_get200_response.from_dict(status_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


