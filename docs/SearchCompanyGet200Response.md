# SearchCompanyGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **float** |  | [optional] 
**results** | [**List[Company]**](Company.md) |  | [optional] 
**total_pages** | **float** |  | [optional] 
**total_results** | **float** |  | [optional] 

## Example

```python
from overseerr_api.models.search_company_get200_response import SearchCompanyGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SearchCompanyGet200Response from a JSON string
search_company_get200_response_instance = SearchCompanyGet200Response.from_json(json)
# print the JSON string representation of the object
print SearchCompanyGet200Response.to_json()

# convert the object into a dict
search_company_get200_response_dict = search_company_get200_response_instance.to_dict()
# create an instance of SearchCompanyGet200Response from a dict
search_company_get200_response_form_dict = search_company_get200_response.from_dict(search_company_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


