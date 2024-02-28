# SearchKeywordGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **float** |  | [optional] 
**results** | [**List[Keyword]**](Keyword.md) |  | [optional] 
**total_pages** | **float** |  | [optional] 
**total_results** | **float** |  | [optional] 

## Example

```python
from overseerr_api.models.search_keyword_get200_response import SearchKeywordGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SearchKeywordGet200Response from a JSON string
search_keyword_get200_response_instance = SearchKeywordGet200Response.from_json(json)
# print the JSON string representation of the object
print SearchKeywordGet200Response.to_json()

# convert the object into a dict
search_keyword_get200_response_dict = search_keyword_get200_response_instance.to_dict()
# create an instance of SearchKeywordGet200Response from a dict
search_keyword_get200_response_form_dict = search_keyword_get200_response.from_dict(search_keyword_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


