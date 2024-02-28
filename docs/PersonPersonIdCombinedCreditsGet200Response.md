# PersonPersonIdCombinedCreditsGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cast** | [**List[CreditCast]**](CreditCast.md) |  | [optional] 
**crew** | [**List[CreditCrew]**](CreditCrew.md) |  | [optional] 
**id** | **float** |  | [optional] 

## Example

```python
from overseerr_api.models.person_person_id_combined_credits_get200_response import PersonPersonIdCombinedCreditsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PersonPersonIdCombinedCreditsGet200Response from a JSON string
person_person_id_combined_credits_get200_response_instance = PersonPersonIdCombinedCreditsGet200Response.from_json(json)
# print the JSON string representation of the object
print PersonPersonIdCombinedCreditsGet200Response.to_json()

# convert the object into a dict
person_person_id_combined_credits_get200_response_dict = person_person_id_combined_credits_get200_response_instance.to_dict()
# create an instance of PersonPersonIdCombinedCreditsGet200Response from a dict
person_person_id_combined_credits_get200_response_form_dict = person_person_id_combined_credits_get200_response.from_dict(person_person_id_combined_credits_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


