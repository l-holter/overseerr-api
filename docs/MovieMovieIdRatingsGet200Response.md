# MovieMovieIdRatingsGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audience_rating** | **str** |  | [optional] 
**audience_score** | **float** |  | [optional] 
**critics_rating** | **str** |  | [optional] 
**critics_score** | **float** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**year** | **float** |  | [optional] 

## Example

```python
from overseerr_api.models.movie_movie_id_ratings_get200_response import MovieMovieIdRatingsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MovieMovieIdRatingsGet200Response from a JSON string
movie_movie_id_ratings_get200_response_instance = MovieMovieIdRatingsGet200Response.from_json(json)
# print the JSON string representation of the object
print MovieMovieIdRatingsGet200Response.to_json()

# convert the object into a dict
movie_movie_id_ratings_get200_response_dict = movie_movie_id_ratings_get200_response_instance.to_dict()
# create an instance of MovieMovieIdRatingsGet200Response from a dict
movie_movie_id_ratings_get200_response_form_dict = movie_movie_id_ratings_get200_response.from_dict(movie_movie_id_ratings_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


