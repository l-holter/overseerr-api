# TvTvIdRatingsGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**critics_rating** | **str** |  | [optional] 
**critics_score** | **float** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**year** | **float** |  | [optional] 

## Example

```python
from overseerr_api.models.tv_tv_id_ratings_get200_response import TvTvIdRatingsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TvTvIdRatingsGet200Response from a JSON string
tv_tv_id_ratings_get200_response_instance = TvTvIdRatingsGet200Response.from_json(json)
# print the JSON string representation of the object
print TvTvIdRatingsGet200Response.to_json()

# convert the object into a dict
tv_tv_id_ratings_get200_response_dict = tv_tv_id_ratings_get200_response_instance.to_dict()
# create an instance of TvTvIdRatingsGet200Response from a dict
tv_tv_id_ratings_get200_response_form_dict = tv_tv_id_ratings_get200_response.from_dict(tv_tv_id_ratings_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


