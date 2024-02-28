# ServiceSonarrSonarrIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profiles** | [**ServiceProfile**](ServiceProfile.md) |  | [optional] 
**server** | [**SonarrSettings**](SonarrSettings.md) |  | [optional] 

## Example

```python
from overseerr_api.models.service_sonarr_sonarr_id_get200_response import ServiceSonarrSonarrIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceSonarrSonarrIdGet200Response from a JSON string
service_sonarr_sonarr_id_get200_response_instance = ServiceSonarrSonarrIdGet200Response.from_json(json)
# print the JSON string representation of the object
print ServiceSonarrSonarrIdGet200Response.to_json()

# convert the object into a dict
service_sonarr_sonarr_id_get200_response_dict = service_sonarr_sonarr_id_get200_response_instance.to_dict()
# create an instance of ServiceSonarrSonarrIdGet200Response from a dict
service_sonarr_sonarr_id_get200_response_form_dict = service_sonarr_sonarr_id_get200_response.from_dict(service_sonarr_sonarr_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


