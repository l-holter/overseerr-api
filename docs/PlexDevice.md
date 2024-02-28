# PlexDevice


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | [optional] 
**client_identifier** | **str** |  | 
**connection** | [**List[PlexConnection]**](PlexConnection.md) |  | 
**created_at** | **str** |  | 
**device** | **str** |  | 
**dns_rebinding_protection** | **bool** |  | [optional] 
**home** | **bool** |  | [optional] 
**https_required** | **bool** |  | [optional] 
**last_seen_at** | **str** |  | 
**name** | **str** |  | 
**nat_loopback_supported** | **bool** |  | [optional] 
**owned** | **bool** |  | 
**owner_id** | **str** |  | [optional] 
**platform** | **str** |  | 
**platform_version** | **str** |  | [optional] 
**presence** | **bool** |  | [optional] 
**product** | **str** |  | 
**product_version** | **str** |  | 
**provides** | **List[str]** |  | 
**public_address** | **str** |  | [optional] 
**public_address_matches** | **bool** |  | [optional] 
**relay** | **bool** |  | [optional] 
**source_title** | **str** |  | [optional] 
**synced** | **bool** |  | [optional] 

## Example

```python
from overseerr_api.models.plex_device import PlexDevice

# TODO update the JSON string below
json = "{}"
# create an instance of PlexDevice from a JSON string
plex_device_instance = PlexDevice.from_json(json)
# print the JSON string representation of the object
print PlexDevice.to_json()

# convert the object into a dict
plex_device_dict = plex_device_instance.to_dict()
# create an instance of PlexDevice from a dict
plex_device_form_dict = plex_device.from_dict(plex_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


