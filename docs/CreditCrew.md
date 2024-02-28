# CreditCrew


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adult** | **bool** |  | [optional] 
**backdrop_path** | **str** |  | [optional] 
**credit_id** | **str** |  | [optional] 
**department** | **str** |  | [optional] 
**episode_count** | **float** |  | [optional] 
**first_air_date** | **str** |  | [optional] 
**genre_ids** | **List[float]** |  | [optional] 
**id** | **float** |  | [optional] 
**job** | **str** |  | [optional] 
**media_info** | [**MediaInfo**](MediaInfo.md) |  | [optional] 
**media_type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**origin_country** | **List[str]** |  | [optional] 
**original_language** | **str** |  | [optional] 
**original_name** | **str** |  | [optional] 
**original_title** | **str** |  | [optional] 
**overview** | **str** |  | [optional] 
**popularity** | **float** |  | [optional] 
**poster_path** | **str** |  | [optional] 
**release_date** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**video** | **bool** |  | [optional] 
**vote_average** | **float** |  | [optional] 
**vote_count** | **float** |  | [optional] 

## Example

```python
from overseerr_api.models.credit_crew import CreditCrew

# TODO update the JSON string below
json = "{}"
# create an instance of CreditCrew from a JSON string
credit_crew_instance = CreditCrew.from_json(json)
# print the JSON string representation of the object
print CreditCrew.to_json()

# convert the object into a dict
credit_crew_dict = credit_crew_instance.to_dict()
# create an instance of CreditCrew from a dict
credit_crew_form_dict = credit_crew.from_dict(credit_crew_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


