# RequestGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_info** | [**PageInfo**](PageInfo.md) |  | [optional] 
**results** | [**List[MediaRequest]**](MediaRequest.md) |  | [optional] 

## Example

```python
from overseerr_api.models.request_get200_response import RequestGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RequestGet200Response from a JSON string
request_get200_response_instance = RequestGet200Response.from_json(json)
# print the JSON string representation of the object
print RequestGet200Response.to_json()

# convert the object into a dict
request_get200_response_dict = request_get200_response_instance.to_dict()
# create an instance of RequestGet200Response from a dict
request_get200_response_form_dict = request_get200_response.from_dict(request_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


