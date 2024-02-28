# PersonDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adult** | **bool** |  | [optional] 
**also_known_as** | **List[str]** |  | [optional] 
**biography** | **str** |  | [optional] 
**deathday** | **str** |  | [optional] 
**gender** | **str** |  | [optional] 
**homepage** | **str** |  | [optional] 
**id** | **float** |  | [optional] 
**imdb_id** | **str** |  | [optional] 
**known_for_department** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**place_of_birth** | **str** |  | [optional] 
**popularity** | **str** |  | [optional] 
**profile_path** | **str** |  | [optional] 

## Example

```python
from overseerr_api.models.person_details import PersonDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PersonDetails from a JSON string
person_details_instance = PersonDetails.from_json(json)
# print the JSON string representation of the object
print PersonDetails.to_json()

# convert the object into a dict
person_details_dict = person_details_instance.to_dict()
# create an instance of PersonDetails from a dict
person_details_form_dict = person_details.from_dict(person_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


