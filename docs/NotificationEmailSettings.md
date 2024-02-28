# NotificationEmailSettings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 
**options** | [**NotificationEmailSettingsOptions**](NotificationEmailSettingsOptions.md) |  | [optional] 
**types** | **float** |  | [optional] 

## Example

```python
from overseerr_api.models.notification_email_settings import NotificationEmailSettings

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationEmailSettings from a JSON string
notification_email_settings_instance = NotificationEmailSettings.from_json(json)
# print the JSON string representation of the object
print NotificationEmailSettings.to_json()

# convert the object into a dict
notification_email_settings_dict = notification_email_settings_instance.to_dict()
# create an instance of NotificationEmailSettings from a dict
notification_email_settings_form_dict = notification_email_settings.from_dict(notification_email_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


