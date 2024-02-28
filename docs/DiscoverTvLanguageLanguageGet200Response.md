# DiscoverTvLanguageLanguageGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | [**SpokenLanguage**](SpokenLanguage.md) |  | [optional] 
**page** | **float** |  | [optional] 
**results** | [**List[TvResult]**](TvResult.md) |  | [optional] 
**total_pages** | **float** |  | [optional] 
**total_results** | **float** |  | [optional] 

## Example

```python
from overseerr_api.models.discover_tv_language_language_get200_response import DiscoverTvLanguageLanguageGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DiscoverTvLanguageLanguageGet200Response from a JSON string
discover_tv_language_language_get200_response_instance = DiscoverTvLanguageLanguageGet200Response.from_json(json)
# print the JSON string representation of the object
print DiscoverTvLanguageLanguageGet200Response.to_json()

# convert the object into a dict
discover_tv_language_language_get200_response_dict = discover_tv_language_language_get200_response_instance.to_dict()
# create an instance of DiscoverTvLanguageLanguageGet200Response from a dict
discover_tv_language_language_get200_response_form_dict = discover_tv_language_language_get200_response.from_dict(discover_tv_language_language_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


