# DiscoverWatchlistGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **float** |  | [optional] 
**results** | [**List[DiscoverWatchlistGet200ResponseResultsInner]**](DiscoverWatchlistGet200ResponseResultsInner.md) |  | [optional] 
**total_pages** | **float** |  | [optional] 
**total_results** | **float** |  | [optional] 

## Example

```python
from overseerr_api.models.discover_watchlist_get200_response import DiscoverWatchlistGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DiscoverWatchlistGet200Response from a JSON string
discover_watchlist_get200_response_instance = DiscoverWatchlistGet200Response.from_json(json)
# print the JSON string representation of the object
print DiscoverWatchlistGet200Response.to_json()

# convert the object into a dict
discover_watchlist_get200_response_dict = discover_watchlist_get200_response_instance.to_dict()
# create an instance of DiscoverWatchlistGet200Response from a dict
discover_watchlist_get200_response_form_dict = discover_watchlist_get200_response.from_dict(discover_watchlist_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


