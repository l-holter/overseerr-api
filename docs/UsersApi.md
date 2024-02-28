# overseerr_api.UsersApi

All URIs are relative to *http://localhost:5055/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_me_get**](UsersApi.md#auth_me_get) | **GET** /auth/me | Get logged-in user
[**auth_reset_password_guid_post**](UsersApi.md#auth_reset_password_guid_post) | **POST** /auth/reset-password/{guid} | Reset the password for a user
[**auth_reset_password_post**](UsersApi.md#auth_reset_password_post) | **POST** /auth/reset-password | Send a reset password email
[**settings_plex_users_get**](UsersApi.md#settings_plex_users_get) | **GET** /settings/plex/users | Get Plex users
[**user_get**](UsersApi.md#user_get) | **GET** /user | Get all users
[**user_import_from_plex_post**](UsersApi.md#user_import_from_plex_post) | **POST** /user/import-from-plex | Import all users from Plex
[**user_post**](UsersApi.md#user_post) | **POST** /user | Create new user
[**user_put**](UsersApi.md#user_put) | **PUT** /user | Update batch of users
[**user_register_push_subscription_post**](UsersApi.md#user_register_push_subscription_post) | **POST** /user/registerPushSubscription | Register a web push /user/registerPushSubscription
[**user_user_id_delete**](UsersApi.md#user_user_id_delete) | **DELETE** /user/{userId} | Delete user by ID
[**user_user_id_get**](UsersApi.md#user_user_id_get) | **GET** /user/{userId} | Get user by ID
[**user_user_id_put**](UsersApi.md#user_user_id_put) | **PUT** /user/{userId} | Update a user by user ID
[**user_user_id_quota_get**](UsersApi.md#user_user_id_quota_get) | **GET** /user/{userId}/quota | Get quotas for a specific user
[**user_user_id_requests_get**](UsersApi.md#user_user_id_requests_get) | **GET** /user/{userId}/requests | Get requests for a specific user
[**user_user_id_settings_main_get**](UsersApi.md#user_user_id_settings_main_get) | **GET** /user/{userId}/settings/main | Get general settings for a user
[**user_user_id_settings_main_post**](UsersApi.md#user_user_id_settings_main_post) | **POST** /user/{userId}/settings/main | Update general settings for a user
[**user_user_id_settings_notifications_get**](UsersApi.md#user_user_id_settings_notifications_get) | **GET** /user/{userId}/settings/notifications | Get notification settings for a user
[**user_user_id_settings_notifications_post**](UsersApi.md#user_user_id_settings_notifications_post) | **POST** /user/{userId}/settings/notifications | Update notification settings for a user
[**user_user_id_settings_password_get**](UsersApi.md#user_user_id_settings_password_get) | **GET** /user/{userId}/settings/password | Get password page informatiom
[**user_user_id_settings_password_post**](UsersApi.md#user_user_id_settings_password_post) | **POST** /user/{userId}/settings/password | Update password for a user
[**user_user_id_settings_permissions_get**](UsersApi.md#user_user_id_settings_permissions_get) | **GET** /user/{userId}/settings/permissions | Get permission settings for a user
[**user_user_id_settings_permissions_post**](UsersApi.md#user_user_id_settings_permissions_post) | **POST** /user/{userId}/settings/permissions | Update permission settings for a user
[**user_user_id_watch_data_get**](UsersApi.md#user_user_id_watch_data_get) | **GET** /user/{userId}/watch_data | Get watch data
[**user_user_id_watchlist_get**](UsersApi.md#user_user_id_watchlist_get) | **GET** /user/{userId}/watchlist | Get the Plex watchlist for a specific user


# **auth_me_get**
> User auth_me_get()

Get logged-in user

Returns the currently logged-in user.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.user import User
from overseerr_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr_api.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr_api.UsersApi(api_client)

    try:
        # Get logged-in user
        api_response = api_instance.auth_me_get()
        print("The response of UsersApi->auth_me_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->auth_me_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Object containing the logged-in user in JSON |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_reset_password_guid_post**
> AuthLogoutPost200Response auth_reset_password_guid_post(guid, auth_reset_password_guid_post_request)

Reset the password for a user

Resets the password for a user if the given guid is connected to a user

### Example

```python
import time
import os
import overseerr_api
from overseerr_api.models.auth_logout_post200_response import AuthLogoutPost200Response
from overseerr_api.models.auth_reset_password_guid_post_request import AuthResetPasswordGuidPostRequest
from overseerr_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr_api.Configuration(
    host = "http://localhost:5055/api/v1"
)


# Enter a context with an instance of the API client
with overseerr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr_api.UsersApi(api_client)
    guid = '9afef5a7-ec89-4d5f-9397-261e96970b50' # str | 
    auth_reset_password_guid_post_request = overseerr_api.AuthResetPasswordGuidPostRequest() # AuthResetPasswordGuidPostRequest | 

    try:
        # Reset the password for a user
        api_response = api_instance.auth_reset_password_guid_post(guid, auth_reset_password_guid_post_request)
        print("The response of UsersApi->auth_reset_password_guid_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->auth_reset_password_guid_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**|  | 
 **auth_reset_password_guid_post_request** | [**AuthResetPasswordGuidPostRequest**](AuthResetPasswordGuidPostRequest.md)|  | 

### Return type

[**AuthLogoutPost200Response**](AuthLogoutPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_reset_password_post**
> AuthLogoutPost200Response auth_reset_password_post(auth_reset_password_post_request)

Send a reset password email

Sends a reset password email to the email if the user exists

### Example

```python
import time
import os
import overseerr_api
from overseerr_api.models.auth_logout_post200_response import AuthLogoutPost200Response
from overseerr_api.models.auth_reset_password_post_request import AuthResetPasswordPostRequest
from overseerr_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr_api.Configuration(
    host = "http://localhost:5055/api/v1"
)


# Enter a context with an instance of the API client
with overseerr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr_api.UsersApi(api_client)
    auth_reset_password_post_request = overseerr_api.AuthResetPasswordPostRequest() # AuthResetPasswordPostRequest | 

    try:
        # Send a reset password email
        api_response = api_instance.auth_reset_password_post(auth_reset_password_post_request)
        print("The response of UsersApi->auth_reset_password_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->auth_reset_password_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_reset_password_post_request** | [**AuthResetPasswordPostRequest**](AuthResetPasswordPostRequest.md)|  | 

### Return type

[**AuthLogoutPost200Response**](AuthLogoutPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_plex_users_get**
> List[SettingsPlexUsersGet200ResponseInner] settings_plex_users_get()

Get Plex users

Returns a list of Plex users in a JSON array.  Requires the `MANAGE_USERS` permission. 

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.settings_plex_users_get200_response_inner import SettingsPlexUsersGet200ResponseInner
from overseerr_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr_api.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr_api.UsersApi(api_client)

    try:
        # Get Plex users
        api_response = api_instance.settings_plex_users_get()
        print("The response of UsersApi->settings_plex_users_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->settings_plex_users_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[SettingsPlexUsersGet200ResponseInner]**](SettingsPlexUsersGet200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plex users |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_get**
> UserGet200Response user_get(take=take, skip=skip, sort=sort)

Get all users

Returns all users in a JSON object.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.user_get200_response import UserGet200Response
from overseerr_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr_api.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr_api.UsersApi(api_client)
    take = 20 # float |  (optional)
    skip = 0 # float |  (optional)
    sort = 'created' # str |  (optional) (default to 'created')

    try:
        # Get all users
        api_response = api_instance.user_get(take=take, skip=skip, sort=sort)
        print("The response of UsersApi->user_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->user_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **take** | **float**|  | [optional] 
 **skip** | **float**|  | [optional] 
 **sort** | **str**|  | [optional] [default to &#39;created&#39;]

### Return type

[**UserGet200Response**](UserGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON array of all users |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_import_from_plex_post**
> List[User] user_import_from_plex_post(user_import_from_plex_post_request=user_import_from_plex_post_request)

Import all users from Plex

Fetches and imports users from the Plex server. If a list of Plex IDs is provided in the request body, only the specified users will be imported. Otherwise, all users will be imported.  Requires the `MANAGE_USERS` permission. 

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.user import User
from overseerr_api.models.user_import_from_plex_post_request import UserImportFromPlexPostRequest
from overseerr_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr_api.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr_api.UsersApi(api_client)
    user_import_from_plex_post_request = overseerr_api.UserImportFromPlexPostRequest() # UserImportFromPlexPostRequest |  (optional)

    try:
        # Import all users from Plex
        api_response = api_instance.user_import_from_plex_post(user_import_from_plex_post_request=user_import_from_plex_post_request)
        print("The response of UsersApi->user_import_from_plex_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->user_import_from_plex_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_import_from_plex_post_request** | [**UserImportFromPlexPostRequest**](UserImportFromPlexPostRequest.md)|  | [optional] 

### Return type

[**List[User]**](User.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A list of the newly created users |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_post**
> User user_post(user_post_request)

Create new user

Creates a new user. Requires the `MANAGE_USERS` permission. 

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.user import User
from overseerr_api.models.user_post_request import UserPostRequest
from overseerr_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr_api.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr_api.UsersApi(api_client)
    user_post_request = overseerr_api.UserPostRequest() # UserPostRequest | 

    try:
        # Create new user
        api_response = api_instance.user_post(user_post_request)
        print("The response of UsersApi->user_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->user_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_post_request** | [**UserPostRequest**](UserPostRequest.md)|  | 

### Return type

[**User**](User.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_put**
> List[User] user_put(user_put_request)

Update batch of users

Update users with given IDs with provided values in request `body.settings`. You cannot update users' Plex tokens through this request.  Requires the `MANAGE_USERS` permission. 

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.user import User
from overseerr_api.models.user_put_request import UserPutRequest
from overseerr_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr_api.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr_api.UsersApi(api_client)
    user_put_request = overseerr_api.UserPutRequest() # UserPutRequest | 

    try:
        # Update batch of users
        api_response = api_instance.user_put(user_put_request)
        print("The response of UsersApi->user_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->user_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_put_request** | [**UserPutRequest**](UserPutRequest.md)|  | 

### Return type

[**List[User]**](User.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated user details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_register_push_subscription_post**
> user_register_push_subscription_post(user_register_push_subscription_post_request)

Register a web push /user/registerPushSubscription

Registers a web push subscription for the logged-in user

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.user_register_push_subscription_post_request import UserRegisterPushSubscriptionPostRequest
from overseerr_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr_api.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr_api.UsersApi(api_client)
    user_register_push_subscription_post_request = overseerr_api.UserRegisterPushSubscriptionPostRequest() # UserRegisterPushSubscriptionPostRequest | 

    try:
        # Register a web push /user/registerPushSubscription
        api_instance.user_register_push_subscription_post(user_register_push_subscription_post_request)
    except Exception as e:
        print("Exception when calling UsersApi->user_register_push_subscription_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_register_push_subscription_post_request** | [**UserRegisterPushSubscriptionPostRequest**](UserRegisterPushSubscriptionPostRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successfully registered push subscription |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_user_id_delete**
> User user_user_id_delete(user_id)

Delete user by ID

Deletes the user with the provided userId. Requires the `MANAGE_USERS` permission.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.user import User
from overseerr_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr_api.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr_api.UsersApi(api_client)
    user_id = 3.4 # float | 

    try:
        # Delete user by ID
        api_response = api_instance.user_user_id_delete(user_id)
        print("The response of UsersApi->user_user_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->user_user_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **float**|  | 

### Return type

[**User**](User.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User successfully deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_user_id_get**
> User user_user_id_get(user_id)

Get user by ID

Retrieves user details in a JSON object. Requires the `MANAGE_USERS` permission. 

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.user import User
from overseerr_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr_api.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr_api.UsersApi(api_client)
    user_id = 3.4 # float | 

    try:
        # Get user by ID
        api_response = api_instance.user_user_id_get(user_id)
        print("The response of UsersApi->user_user_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->user_user_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **float**|  | 

### Return type

[**User**](User.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Users details in JSON |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_user_id_put**
> User user_user_id_put(user_id, user)

Update a user by user ID

Update a user with the provided values. You cannot update a user's Plex token through this request.  Requires the `MANAGE_USERS` permission. 

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.user import User
from overseerr_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr_api.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr_api.UsersApi(api_client)
    user_id = 3.4 # float | 
    user = overseerr_api.User() # User | 

    try:
        # Update a user by user ID
        api_response = api_instance.user_user_id_put(user_id, user)
        print("The response of UsersApi->user_user_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->user_user_id_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **float**|  | 
 **user** | [**User**](User.md)|  | 

### Return type

[**User**](User.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated user details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_user_id_quota_get**
> UserUserIdQuotaGet200Response user_user_id_quota_get(user_id)

Get quotas for a specific user

Returns quota details for a user in a JSON object. Requires `MANAGE_USERS` permission if viewing other users. 

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.user_user_id_quota_get200_response import UserUserIdQuotaGet200Response
from overseerr_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr_api.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr_api.UsersApi(api_client)
    user_id = 3.4 # float | 

    try:
        # Get quotas for a specific user
        api_response = api_instance.user_user_id_quota_get(user_id)
        print("The response of UsersApi->user_user_id_quota_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->user_user_id_quota_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **float**|  | 

### Return type

[**UserUserIdQuotaGet200Response**](UserUserIdQuotaGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User quota details in JSON |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_user_id_requests_get**
> RequestGet200Response user_user_id_requests_get(user_id, take=take, skip=skip)

Get requests for a specific user

Retrieves a user's requests in a JSON object. 

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.request_get200_response import RequestGet200Response
from overseerr_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr_api.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr_api.UsersApi(api_client)
    user_id = 3.4 # float | 
    take = 20 # float |  (optional)
    skip = 0 # float |  (optional)

    try:
        # Get requests for a specific user
        api_response = api_instance.user_user_id_requests_get(user_id, take=take, skip=skip)
        print("The response of UsersApi->user_user_id_requests_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->user_user_id_requests_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **float**|  | 
 **take** | **float**|  | [optional] 
 **skip** | **float**|  | [optional] 

### Return type

[**RequestGet200Response**](RequestGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User&#39;s requests returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_user_id_settings_main_get**
> UserUserIdSettingsMainGet200Response user_user_id_settings_main_get(user_id)

Get general settings for a user

Returns general settings for a specific user. Requires `MANAGE_USERS` permission if viewing other users.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.user_user_id_settings_main_get200_response import UserUserIdSettingsMainGet200Response
from overseerr_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr_api.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr_api.UsersApi(api_client)
    user_id = 3.4 # float | 

    try:
        # Get general settings for a user
        api_response = api_instance.user_user_id_settings_main_get(user_id)
        print("The response of UsersApi->user_user_id_settings_main_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->user_user_id_settings_main_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **float**|  | 

### Return type

[**UserUserIdSettingsMainGet200Response**](UserUserIdSettingsMainGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User general settings returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_user_id_settings_main_post**
> UserUserIdSettingsMainGet200Response user_user_id_settings_main_post(user_id, user_user_id_settings_main_post_request)

Update general settings for a user

Updates and returns general settings for a specific user. Requires `MANAGE_USERS` permission if editing other users.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.user_user_id_settings_main_get200_response import UserUserIdSettingsMainGet200Response
from overseerr_api.models.user_user_id_settings_main_post_request import UserUserIdSettingsMainPostRequest
from overseerr_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr_api.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr_api.UsersApi(api_client)
    user_id = 3.4 # float | 
    user_user_id_settings_main_post_request = overseerr_api.UserUserIdSettingsMainPostRequest() # UserUserIdSettingsMainPostRequest | 

    try:
        # Update general settings for a user
        api_response = api_instance.user_user_id_settings_main_post(user_id, user_user_id_settings_main_post_request)
        print("The response of UsersApi->user_user_id_settings_main_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->user_user_id_settings_main_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **float**|  | 
 **user_user_id_settings_main_post_request** | [**UserUserIdSettingsMainPostRequest**](UserUserIdSettingsMainPostRequest.md)|  | 

### Return type

[**UserUserIdSettingsMainGet200Response**](UserUserIdSettingsMainGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated user general settings returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_user_id_settings_notifications_get**
> UserSettingsNotifications user_user_id_settings_notifications_get(user_id)

Get notification settings for a user

Returns notification settings for a specific user. Requires `MANAGE_USERS` permission if viewing other users.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.user_settings_notifications import UserSettingsNotifications
from overseerr_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr_api.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr_api.UsersApi(api_client)
    user_id = 3.4 # float | 

    try:
        # Get notification settings for a user
        api_response = api_instance.user_user_id_settings_notifications_get(user_id)
        print("The response of UsersApi->user_user_id_settings_notifications_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->user_user_id_settings_notifications_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **float**|  | 

### Return type

[**UserSettingsNotifications**](UserSettingsNotifications.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User notification settings returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_user_id_settings_notifications_post**
> UserSettingsNotifications user_user_id_settings_notifications_post(user_id, user_settings_notifications)

Update notification settings for a user

Updates and returns notification settings for a specific user. Requires `MANAGE_USERS` permission if editing other users.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.user_settings_notifications import UserSettingsNotifications
from overseerr_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr_api.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr_api.UsersApi(api_client)
    user_id = 3.4 # float | 
    user_settings_notifications = overseerr_api.UserSettingsNotifications() # UserSettingsNotifications | 

    try:
        # Update notification settings for a user
        api_response = api_instance.user_user_id_settings_notifications_post(user_id, user_settings_notifications)
        print("The response of UsersApi->user_user_id_settings_notifications_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->user_user_id_settings_notifications_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **float**|  | 
 **user_settings_notifications** | [**UserSettingsNotifications**](UserSettingsNotifications.md)|  | 

### Return type

[**UserSettingsNotifications**](UserSettingsNotifications.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated user notification settings returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_user_id_settings_password_get**
> UserUserIdSettingsPasswordGet200Response user_user_id_settings_password_get(user_id)

Get password page informatiom

Returns important data for the password page to function correctly. Requires `MANAGE_USERS` permission if viewing other users.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.user_user_id_settings_password_get200_response import UserUserIdSettingsPasswordGet200Response
from overseerr_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr_api.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr_api.UsersApi(api_client)
    user_id = 3.4 # float | 

    try:
        # Get password page informatiom
        api_response = api_instance.user_user_id_settings_password_get(user_id)
        print("The response of UsersApi->user_user_id_settings_password_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->user_user_id_settings_password_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **float**|  | 

### Return type

[**UserUserIdSettingsPasswordGet200Response**](UserUserIdSettingsPasswordGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User password page information returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_user_id_settings_password_post**
> user_user_id_settings_password_post(user_id, user_user_id_settings_password_post_request)

Update password for a user

Updates a user's password. Requires `MANAGE_USERS` permission if editing other users.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.user_user_id_settings_password_post_request import UserUserIdSettingsPasswordPostRequest
from overseerr_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr_api.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr_api.UsersApi(api_client)
    user_id = 3.4 # float | 
    user_user_id_settings_password_post_request = overseerr_api.UserUserIdSettingsPasswordPostRequest() # UserUserIdSettingsPasswordPostRequest | 

    try:
        # Update password for a user
        api_instance.user_user_id_settings_password_post(user_id, user_user_id_settings_password_post_request)
    except Exception as e:
        print("Exception when calling UsersApi->user_user_id_settings_password_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **float**|  | 
 **user_user_id_settings_password_post_request** | [**UserUserIdSettingsPasswordPostRequest**](UserUserIdSettingsPasswordPostRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | User password updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_user_id_settings_permissions_get**
> UserUserIdSettingsPermissionsGet200Response user_user_id_settings_permissions_get(user_id)

Get permission settings for a user

Returns permission settings for a specific user. Requires `MANAGE_USERS` permission if viewing other users.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.user_user_id_settings_permissions_get200_response import UserUserIdSettingsPermissionsGet200Response
from overseerr_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr_api.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr_api.UsersApi(api_client)
    user_id = 3.4 # float | 

    try:
        # Get permission settings for a user
        api_response = api_instance.user_user_id_settings_permissions_get(user_id)
        print("The response of UsersApi->user_user_id_settings_permissions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->user_user_id_settings_permissions_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **float**|  | 

### Return type

[**UserUserIdSettingsPermissionsGet200Response**](UserUserIdSettingsPermissionsGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User permission settings returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_user_id_settings_permissions_post**
> UserUserIdSettingsPermissionsGet200Response user_user_id_settings_permissions_post(user_id, user_user_id_settings_permissions_post_request)

Update permission settings for a user

Updates and returns permission settings for a specific user. Requires `MANAGE_USERS` permission if editing other users.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.user_user_id_settings_permissions_get200_response import UserUserIdSettingsPermissionsGet200Response
from overseerr_api.models.user_user_id_settings_permissions_post_request import UserUserIdSettingsPermissionsPostRequest
from overseerr_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr_api.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr_api.UsersApi(api_client)
    user_id = 3.4 # float | 
    user_user_id_settings_permissions_post_request = overseerr_api.UserUserIdSettingsPermissionsPostRequest() # UserUserIdSettingsPermissionsPostRequest | 

    try:
        # Update permission settings for a user
        api_response = api_instance.user_user_id_settings_permissions_post(user_id, user_user_id_settings_permissions_post_request)
        print("The response of UsersApi->user_user_id_settings_permissions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->user_user_id_settings_permissions_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **float**|  | 
 **user_user_id_settings_permissions_post_request** | [**UserUserIdSettingsPermissionsPostRequest**](UserUserIdSettingsPermissionsPostRequest.md)|  | 

### Return type

[**UserUserIdSettingsPermissionsGet200Response**](UserUserIdSettingsPermissionsGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated user general settings returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_user_id_watch_data_get**
> UserUserIdWatchDataGet200Response user_user_id_watch_data_get(user_id)

Get watch data

Returns play count, play duration, and recently watched media.  Requires the `ADMIN` permission to fetch results for other users. 

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.user_user_id_watch_data_get200_response import UserUserIdWatchDataGet200Response
from overseerr_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr_api.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr_api.UsersApi(api_client)
    user_id = 3.4 # float | 

    try:
        # Get watch data
        api_response = api_instance.user_user_id_watch_data_get(user_id)
        print("The response of UsersApi->user_user_id_watch_data_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->user_user_id_watch_data_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **float**|  | 

### Return type

[**UserUserIdWatchDataGet200Response**](UserUserIdWatchDataGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Users |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_user_id_watchlist_get**
> DiscoverWatchlistGet200Response user_user_id_watchlist_get(user_id, page=page)

Get the Plex watchlist for a specific user

Retrieves a user's Plex Watchlist in a JSON object. 

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.discover_watchlist_get200_response import DiscoverWatchlistGet200Response
from overseerr_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr_api.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr_api.UsersApi(api_client)
    user_id = 3.4 # float | 
    page = 1 # float |  (optional) (default to 1)

    try:
        # Get the Plex watchlist for a specific user
        api_response = api_instance.user_user_id_watchlist_get(user_id, page=page)
        print("The response of UsersApi->user_user_id_watchlist_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->user_user_id_watchlist_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **float**|  | 
 **page** | **float**|  | [optional] [default to 1]

### Return type

[**DiscoverWatchlistGet200Response**](DiscoverWatchlistGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Watchlist data returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

