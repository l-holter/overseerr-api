# NotificationEmailSettingsOptions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_self_signed** | **bool** |  | [optional] 
**auth_pass** | **str** |  | [optional] 
**auth_user** | **str** |  | [optional] 
**email_from** | **str** |  | [optional] 
**ignore_tls** | **bool** |  | [optional] 
**require_tls** | **bool** |  | [optional] 
**secure** | **bool** |  | [optional] 
**sender_name** | **str** |  | [optional] 
**smtp_host** | **str** |  | [optional] 
**smtp_port** | **float** |  | [optional] 

## Example

```python
from overseerr_api.models.notification_email_settings_options import NotificationEmailSettingsOptions

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationEmailSettingsOptions from a JSON string
notification_email_settings_options_instance = NotificationEmailSettingsOptions.from_json(json)
# print the JSON string representation of the object
print NotificationEmailSettingsOptions.to_json()

# convert the object into a dict
notification_email_settings_options_dict = notification_email_settings_options_instance.to_dict()
# create an instance of NotificationEmailSettingsOptions from a dict
notification_email_settings_options_form_dict = notification_email_settings_options.from_dict(notification_email_settings_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


