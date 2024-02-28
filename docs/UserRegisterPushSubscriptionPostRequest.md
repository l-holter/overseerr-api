# UserRegisterPushSubscriptionPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth** | **str** |  | 
**endpoint** | **str** |  | 
**p256dh** | **str** |  | 

## Example

```python
from overseerr_api.models.user_register_push_subscription_post_request import UserRegisterPushSubscriptionPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserRegisterPushSubscriptionPostRequest from a JSON string
user_register_push_subscription_post_request_instance = UserRegisterPushSubscriptionPostRequest.from_json(json)
# print the JSON string representation of the object
print UserRegisterPushSubscriptionPostRequest.to_json()

# convert the object into a dict
user_register_push_subscription_post_request_dict = user_register_push_subscription_post_request_instance.to_dict()
# create an instance of UserRegisterPushSubscriptionPostRequest from a dict
user_register_push_subscription_post_request_form_dict = user_register_push_subscription_post_request.from_dict(user_register_push_subscription_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


