# RequestCountGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approved** | **float** |  | [optional] 
**available** | **float** |  | [optional] 
**declined** | **float** |  | [optional] 
**movie** | **float** |  | [optional] 
**pending** | **float** |  | [optional] 
**processing** | **float** |  | [optional] 
**total** | **float** |  | [optional] 
**tv** | **float** |  | [optional] 

## Example

```python
from overseerr_api.models.request_count_get200_response import RequestCountGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RequestCountGet200Response from a JSON string
request_count_get200_response_instance = RequestCountGet200Response.from_json(json)
# print the JSON string representation of the object
print RequestCountGet200Response.to_json()

# convert the object into a dict
request_count_get200_response_dict = request_count_get200_response_instance.to_dict()
# create an instance of RequestCountGet200Response from a dict
request_count_get200_response_form_dict = request_count_get200_response.from_dict(request_count_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


