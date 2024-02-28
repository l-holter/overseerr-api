# overseerr_api.SettingsApi

All URIs are relative to *http://localhost:5055/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**settings_about_get**](SettingsApi.md#settings_about_get) | **GET** /settings/about | Get server stats
[**settings_cache_cache_id_flush_post**](SettingsApi.md#settings_cache_cache_id_flush_post) | **POST** /settings/cache/{cacheId}/flush | Flush a specific cache
[**settings_cache_get**](SettingsApi.md#settings_cache_get) | **GET** /settings/cache | Get a list of active caches
[**settings_discover_add_post**](SettingsApi.md#settings_discover_add_post) | **POST** /settings/discover/add | Add a new slider
[**settings_discover_get**](SettingsApi.md#settings_discover_get) | **GET** /settings/discover | Get all discover sliders
[**settings_discover_post**](SettingsApi.md#settings_discover_post) | **POST** /settings/discover | Batch update all sliders.
[**settings_discover_reset_get**](SettingsApi.md#settings_discover_reset_get) | **GET** /settings/discover/reset | Reset all discover sliders
[**settings_discover_slider_id_delete**](SettingsApi.md#settings_discover_slider_id_delete) | **DELETE** /settings/discover/{sliderId} | Delete slider by ID
[**settings_discover_slider_id_put**](SettingsApi.md#settings_discover_slider_id_put) | **PUT** /settings/discover/{sliderId} | Update a single slider
[**settings_initialize_post**](SettingsApi.md#settings_initialize_post) | **POST** /settings/initialize | Initialize application
[**settings_jobs_get**](SettingsApi.md#settings_jobs_get) | **GET** /settings/jobs | Get scheduled jobs
[**settings_jobs_job_id_cancel_post**](SettingsApi.md#settings_jobs_job_id_cancel_post) | **POST** /settings/jobs/{jobId}/cancel | Cancel a specific job
[**settings_jobs_job_id_run_post**](SettingsApi.md#settings_jobs_job_id_run_post) | **POST** /settings/jobs/{jobId}/run | Invoke a specific job
[**settings_jobs_job_id_schedule_post**](SettingsApi.md#settings_jobs_job_id_schedule_post) | **POST** /settings/jobs/{jobId}/schedule | Modify job schedule
[**settings_logs_get**](SettingsApi.md#settings_logs_get) | **GET** /settings/logs | Returns logs
[**settings_main_get**](SettingsApi.md#settings_main_get) | **GET** /settings/main | Get main settings
[**settings_main_post**](SettingsApi.md#settings_main_post) | **POST** /settings/main | Update main settings
[**settings_main_regenerate_post**](SettingsApi.md#settings_main_regenerate_post) | **POST** /settings/main/regenerate | Get main settings with newly-generated API key
[**settings_notifications_discord_get**](SettingsApi.md#settings_notifications_discord_get) | **GET** /settings/notifications/discord | Get Discord notification settings
[**settings_notifications_discord_post**](SettingsApi.md#settings_notifications_discord_post) | **POST** /settings/notifications/discord | Update Discord notification settings
[**settings_notifications_discord_test_post**](SettingsApi.md#settings_notifications_discord_test_post) | **POST** /settings/notifications/discord/test | Test Discord settings
[**settings_notifications_email_get**](SettingsApi.md#settings_notifications_email_get) | **GET** /settings/notifications/email | Get email notification settings
[**settings_notifications_email_post**](SettingsApi.md#settings_notifications_email_post) | **POST** /settings/notifications/email | Update email notification settings
[**settings_notifications_email_test_post**](SettingsApi.md#settings_notifications_email_test_post) | **POST** /settings/notifications/email/test | Test email settings
[**settings_notifications_gotify_get**](SettingsApi.md#settings_notifications_gotify_get) | **GET** /settings/notifications/gotify | Get Gotify notification settings
[**settings_notifications_gotify_post**](SettingsApi.md#settings_notifications_gotify_post) | **POST** /settings/notifications/gotify | Update Gotify notification settings
[**settings_notifications_gotify_test_post**](SettingsApi.md#settings_notifications_gotify_test_post) | **POST** /settings/notifications/gotify/test | Test Gotify settings
[**settings_notifications_lunasea_get**](SettingsApi.md#settings_notifications_lunasea_get) | **GET** /settings/notifications/lunasea | Get LunaSea notification settings
[**settings_notifications_lunasea_post**](SettingsApi.md#settings_notifications_lunasea_post) | **POST** /settings/notifications/lunasea | Update LunaSea notification settings
[**settings_notifications_lunasea_test_post**](SettingsApi.md#settings_notifications_lunasea_test_post) | **POST** /settings/notifications/lunasea/test | Test LunaSea settings
[**settings_notifications_pushbullet_get**](SettingsApi.md#settings_notifications_pushbullet_get) | **GET** /settings/notifications/pushbullet | Get Pushbullet notification settings
[**settings_notifications_pushbullet_post**](SettingsApi.md#settings_notifications_pushbullet_post) | **POST** /settings/notifications/pushbullet | Update Pushbullet notification settings
[**settings_notifications_pushbullet_test_post**](SettingsApi.md#settings_notifications_pushbullet_test_post) | **POST** /settings/notifications/pushbullet/test | Test Pushbullet settings
[**settings_notifications_pushover_get**](SettingsApi.md#settings_notifications_pushover_get) | **GET** /settings/notifications/pushover | Get Pushover notification settings
[**settings_notifications_pushover_post**](SettingsApi.md#settings_notifications_pushover_post) | **POST** /settings/notifications/pushover | Update Pushover notification settings
[**settings_notifications_pushover_sounds_get**](SettingsApi.md#settings_notifications_pushover_sounds_get) | **GET** /settings/notifications/pushover/sounds | Get Pushover sounds
[**settings_notifications_pushover_test_post**](SettingsApi.md#settings_notifications_pushover_test_post) | **POST** /settings/notifications/pushover/test | Test Pushover settings
[**settings_notifications_slack_get**](SettingsApi.md#settings_notifications_slack_get) | **GET** /settings/notifications/slack | Get Slack notification settings
[**settings_notifications_slack_post**](SettingsApi.md#settings_notifications_slack_post) | **POST** /settings/notifications/slack | Update Slack notification settings
[**settings_notifications_slack_test_post**](SettingsApi.md#settings_notifications_slack_test_post) | **POST** /settings/notifications/slack/test | Test Slack settings
[**settings_notifications_telegram_get**](SettingsApi.md#settings_notifications_telegram_get) | **GET** /settings/notifications/telegram | Get Telegram notification settings
[**settings_notifications_telegram_post**](SettingsApi.md#settings_notifications_telegram_post) | **POST** /settings/notifications/telegram | Update Telegram notification settings
[**settings_notifications_telegram_test_post**](SettingsApi.md#settings_notifications_telegram_test_post) | **POST** /settings/notifications/telegram/test | Test Telegram settings
[**settings_notifications_webhook_get**](SettingsApi.md#settings_notifications_webhook_get) | **GET** /settings/notifications/webhook | Get webhook notification settings
[**settings_notifications_webhook_post**](SettingsApi.md#settings_notifications_webhook_post) | **POST** /settings/notifications/webhook | Update webhook notification settings
[**settings_notifications_webhook_test_post**](SettingsApi.md#settings_notifications_webhook_test_post) | **POST** /settings/notifications/webhook/test | Test webhook settings
[**settings_notifications_webpush_get**](SettingsApi.md#settings_notifications_webpush_get) | **GET** /settings/notifications/webpush | Get Web Push notification settings
[**settings_notifications_webpush_post**](SettingsApi.md#settings_notifications_webpush_post) | **POST** /settings/notifications/webpush | Update Web Push notification settings
[**settings_notifications_webpush_test_post**](SettingsApi.md#settings_notifications_webpush_test_post) | **POST** /settings/notifications/webpush/test | Test Web Push settings
[**settings_plex_devices_servers_get**](SettingsApi.md#settings_plex_devices_servers_get) | **GET** /settings/plex/devices/servers | Gets the user&#39;s available Plex servers
[**settings_plex_get**](SettingsApi.md#settings_plex_get) | **GET** /settings/plex | Get Plex settings
[**settings_plex_library_get**](SettingsApi.md#settings_plex_library_get) | **GET** /settings/plex/library | Get Plex libraries
[**settings_plex_post**](SettingsApi.md#settings_plex_post) | **POST** /settings/plex | Update Plex settings
[**settings_plex_sync_get**](SettingsApi.md#settings_plex_sync_get) | **GET** /settings/plex/sync | Get status of full Plex library scan
[**settings_plex_sync_post**](SettingsApi.md#settings_plex_sync_post) | **POST** /settings/plex/sync | Start full Plex library scan
[**settings_plex_users_get**](SettingsApi.md#settings_plex_users_get) | **GET** /settings/plex/users | Get Plex users
[**settings_public_get**](SettingsApi.md#settings_public_get) | **GET** /settings/public | Get public settings
[**settings_radarr_get**](SettingsApi.md#settings_radarr_get) | **GET** /settings/radarr | Get Radarr settings
[**settings_radarr_post**](SettingsApi.md#settings_radarr_post) | **POST** /settings/radarr | Create Radarr instance
[**settings_radarr_radarr_id_delete**](SettingsApi.md#settings_radarr_radarr_id_delete) | **DELETE** /settings/radarr/{radarrId} | Delete Radarr instance
[**settings_radarr_radarr_id_profiles_get**](SettingsApi.md#settings_radarr_radarr_id_profiles_get) | **GET** /settings/radarr/{radarrId}/profiles | Get available Radarr profiles
[**settings_radarr_radarr_id_put**](SettingsApi.md#settings_radarr_radarr_id_put) | **PUT** /settings/radarr/{radarrId} | Update Radarr instance
[**settings_radarr_test_post**](SettingsApi.md#settings_radarr_test_post) | **POST** /settings/radarr/test | Test Radarr configuration
[**settings_sonarr_get**](SettingsApi.md#settings_sonarr_get) | **GET** /settings/sonarr | Get Sonarr settings
[**settings_sonarr_post**](SettingsApi.md#settings_sonarr_post) | **POST** /settings/sonarr | Create Sonarr instance
[**settings_sonarr_sonarr_id_delete**](SettingsApi.md#settings_sonarr_sonarr_id_delete) | **DELETE** /settings/sonarr/{sonarrId} | Delete Sonarr instance
[**settings_sonarr_sonarr_id_put**](SettingsApi.md#settings_sonarr_sonarr_id_put) | **PUT** /settings/sonarr/{sonarrId} | Update Sonarr instance
[**settings_sonarr_test_post**](SettingsApi.md#settings_sonarr_test_post) | **POST** /settings/sonarr/test | Test Sonarr configuration
[**settings_tautulli_get**](SettingsApi.md#settings_tautulli_get) | **GET** /settings/tautulli | Get Tautulli settings
[**settings_tautulli_post**](SettingsApi.md#settings_tautulli_post) | **POST** /settings/tautulli | Update Tautulli settings


# **settings_about_get**
> SettingsAboutGet200Response settings_about_get()

Get server stats

Returns current server stats in a JSON object.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.settings_about_get200_response import SettingsAboutGet200Response
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
    api_instance = overseerr_api.SettingsApi(api_client)

    try:
        # Get server stats
        api_response = api_instance.settings_about_get()
        print("The response of SettingsApi->settings_about_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_about_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**SettingsAboutGet200Response**](SettingsAboutGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned about settings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_cache_cache_id_flush_post**
> settings_cache_cache_id_flush_post(cache_id)

Flush a specific cache

Flushes all data from the cache ID provided

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
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
    api_instance = overseerr_api.SettingsApi(api_client)
    cache_id = 'cache_id_example' # str | 

    try:
        # Flush a specific cache
        api_instance.settings_cache_cache_id_flush_post(cache_id)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_cache_cache_id_flush_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cache_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Flushed cache |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_cache_get**
> SettingsCacheGet200Response settings_cache_get()

Get a list of active caches

Retrieves a list of all active caches and their current stats.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.settings_cache_get200_response import SettingsCacheGet200Response
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
    api_instance = overseerr_api.SettingsApi(api_client)

    try:
        # Get a list of active caches
        api_response = api_instance.settings_cache_get()
        print("The response of SettingsApi->settings_cache_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_cache_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**SettingsCacheGet200Response**](SettingsCacheGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Caches returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_discover_add_post**
> DiscoverSlider settings_discover_add_post(settings_discover_add_post_request)

Add a new slider

Add a single slider and return the newly created slider. Requires the `ADMIN` permission. 

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.discover_slider import DiscoverSlider
from overseerr_api.models.settings_discover_add_post_request import SettingsDiscoverAddPostRequest
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
    api_instance = overseerr_api.SettingsApi(api_client)
    settings_discover_add_post_request = overseerr_api.SettingsDiscoverAddPostRequest() # SettingsDiscoverAddPostRequest | 

    try:
        # Add a new slider
        api_response = api_instance.settings_discover_add_post(settings_discover_add_post_request)
        print("The response of SettingsApi->settings_discover_add_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_discover_add_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_discover_add_post_request** | [**SettingsDiscoverAddPostRequest**](SettingsDiscoverAddPostRequest.md)|  | 

### Return type

[**DiscoverSlider**](DiscoverSlider.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns newly added discovery slider |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_discover_get**
> List[DiscoverSlider] settings_discover_get()

Get all discover sliders

Returns all discovery sliders. Built-in and custom made.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.discover_slider import DiscoverSlider
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
    api_instance = overseerr_api.SettingsApi(api_client)

    try:
        # Get all discover sliders
        api_response = api_instance.settings_discover_get()
        print("The response of SettingsApi->settings_discover_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_discover_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[DiscoverSlider]**](DiscoverSlider.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned all discovery sliders |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_discover_post**
> List[DiscoverSlider] settings_discover_post(discover_slider)

Batch update all sliders.

Batch update all sliders at once. Should also be used for creation. Will only update sliders provided and will not delete any sliders not present in the request. If a slider is missing a required field, it will be ignored. Requires the `ADMIN` permission. 

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.discover_slider import DiscoverSlider
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
    api_instance = overseerr_api.SettingsApi(api_client)
    discover_slider = [overseerr_api.DiscoverSlider()] # List[DiscoverSlider] | 

    try:
        # Batch update all sliders.
        api_response = api_instance.settings_discover_post(discover_slider)
        print("The response of SettingsApi->settings_discover_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_discover_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **discover_slider** | [**List[DiscoverSlider]**](DiscoverSlider.md)|  | 

### Return type

[**List[DiscoverSlider]**](DiscoverSlider.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned all newly updated discovery sliders |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_discover_reset_get**
> settings_discover_reset_get()

Reset all discover sliders

Resets all discovery sliders to the default values. Requires the `ADMIN` permission.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
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
    api_instance = overseerr_api.SettingsApi(api_client)

    try:
        # Reset all discover sliders
        api_instance.settings_discover_reset_get()
    except Exception as e:
        print("Exception when calling SettingsApi->settings_discover_reset_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | All sliders reset to defaults |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_discover_slider_id_delete**
> DiscoverSlider settings_discover_slider_id_delete(slider_id)

Delete slider by ID

Deletes the slider with the provided sliderId. Requires the `ADMIN` permission.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.discover_slider import DiscoverSlider
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
    api_instance = overseerr_api.SettingsApi(api_client)
    slider_id = 3.4 # float | 

    try:
        # Delete slider by ID
        api_response = api_instance.settings_discover_slider_id_delete(slider_id)
        print("The response of SettingsApi->settings_discover_slider_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_discover_slider_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slider_id** | **float**|  | 

### Return type

[**DiscoverSlider**](DiscoverSlider.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Slider successfully deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_discover_slider_id_put**
> DiscoverSlider settings_discover_slider_id_put(slider_id, settings_discover_slider_id_put_request)

Update a single slider

Updates a single slider and return the newly updated slider. Requires the `ADMIN` permission. 

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.discover_slider import DiscoverSlider
from overseerr_api.models.settings_discover_slider_id_put_request import SettingsDiscoverSliderIdPutRequest
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
    api_instance = overseerr_api.SettingsApi(api_client)
    slider_id = 'slider_id_example' # str | The ID of the slider
    settings_discover_slider_id_put_request = overseerr_api.SettingsDiscoverSliderIdPutRequest() # SettingsDiscoverSliderIdPutRequest | 

    try:
        # Update a single slider
        api_response = api_instance.settings_discover_slider_id_put(slider_id, settings_discover_slider_id_put_request)
        print("The response of SettingsApi->settings_discover_slider_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_discover_slider_id_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slider_id** | **str**| The ID of the slider | 
 **settings_discover_slider_id_put_request** | [**SettingsDiscoverSliderIdPutRequest**](SettingsDiscoverSliderIdPutRequest.md)|  | 

### Return type

[**DiscoverSlider**](DiscoverSlider.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns newly added discovery slider |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_initialize_post**
> PublicSettings settings_initialize_post()

Initialize application

Sets the app as initialized, allowing the user to navigate to pages other than the setup page.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.public_settings import PublicSettings
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
    api_instance = overseerr_api.SettingsApi(api_client)

    try:
        # Initialize application
        api_response = api_instance.settings_initialize_post()
        print("The response of SettingsApi->settings_initialize_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_initialize_post: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**PublicSettings**](PublicSettings.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Public settings returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_jobs_get**
> List[Job] settings_jobs_get()

Get scheduled jobs

Returns list of all scheduled jobs and details about their next execution time in a JSON array.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.job import Job
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
    api_instance = overseerr_api.SettingsApi(api_client)

    try:
        # Get scheduled jobs
        api_response = api_instance.settings_jobs_get()
        print("The response of SettingsApi->settings_jobs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_jobs_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[Job]**](Job.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Scheduled jobs returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_jobs_job_id_cancel_post**
> Job settings_jobs_job_id_cancel_post(job_id)

Cancel a specific job

Cancels a specific job. Will return the new job status in JSON format.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.job import Job
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
    api_instance = overseerr_api.SettingsApi(api_client)
    job_id = 'job_id_example' # str | 

    try:
        # Cancel a specific job
        api_response = api_instance.settings_jobs_job_id_cancel_post(job_id)
        print("The response of SettingsApi->settings_jobs_job_id_cancel_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_jobs_job_id_cancel_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 

### Return type

[**Job**](Job.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Canceled job returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_jobs_job_id_run_post**
> Job settings_jobs_job_id_run_post(job_id)

Invoke a specific job

Invokes a specific job to run. Will return the new job status in JSON format.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.job import Job
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
    api_instance = overseerr_api.SettingsApi(api_client)
    job_id = 'job_id_example' # str | 

    try:
        # Invoke a specific job
        api_response = api_instance.settings_jobs_job_id_run_post(job_id)
        print("The response of SettingsApi->settings_jobs_job_id_run_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_jobs_job_id_run_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 

### Return type

[**Job**](Job.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Invoked job returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_jobs_job_id_schedule_post**
> Job settings_jobs_job_id_schedule_post(job_id, settings_jobs_job_id_schedule_post_request)

Modify job schedule

Re-registers the job with the schedule specified. Will return the job in JSON format.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.job import Job
from overseerr_api.models.settings_jobs_job_id_schedule_post_request import SettingsJobsJobIdSchedulePostRequest
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
    api_instance = overseerr_api.SettingsApi(api_client)
    job_id = 'job_id_example' # str | 
    settings_jobs_job_id_schedule_post_request = overseerr_api.SettingsJobsJobIdSchedulePostRequest() # SettingsJobsJobIdSchedulePostRequest | 

    try:
        # Modify job schedule
        api_response = api_instance.settings_jobs_job_id_schedule_post(job_id, settings_jobs_job_id_schedule_post_request)
        print("The response of SettingsApi->settings_jobs_job_id_schedule_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_jobs_job_id_schedule_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 
 **settings_jobs_job_id_schedule_post_request** | [**SettingsJobsJobIdSchedulePostRequest**](SettingsJobsJobIdSchedulePostRequest.md)|  | 

### Return type

[**Job**](Job.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Rescheduled job |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_logs_get**
> List[SettingsLogsGet200ResponseInner] settings_logs_get(take=take, skip=skip, filter=filter, search=search)

Returns logs

Returns list of all log items and details

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.settings_logs_get200_response_inner import SettingsLogsGet200ResponseInner
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
    api_instance = overseerr_api.SettingsApi(api_client)
    take = 25 # float |  (optional)
    skip = 0 # float |  (optional)
    filter = 'debug' # str |  (optional) (default to 'debug')
    search = 'plex' # str |  (optional)

    try:
        # Returns logs
        api_response = api_instance.settings_logs_get(take=take, skip=skip, filter=filter, search=search)
        print("The response of SettingsApi->settings_logs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_logs_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **take** | **float**|  | [optional] 
 **skip** | **float**|  | [optional] 
 **filter** | **str**|  | [optional] [default to &#39;debug&#39;]
 **search** | **str**|  | [optional] 

### Return type

[**List[SettingsLogsGet200ResponseInner]**](SettingsLogsGet200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Server log returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_main_get**
> MainSettings settings_main_get()

Get main settings

Retrieves all main settings in a JSON object.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.main_settings import MainSettings
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
    api_instance = overseerr_api.SettingsApi(api_client)

    try:
        # Get main settings
        api_response = api_instance.settings_main_get()
        print("The response of SettingsApi->settings_main_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_main_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**MainSettings**](MainSettings.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_main_post**
> MainSettings settings_main_post(main_settings)

Update main settings

Updates main settings with the provided values.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.main_settings import MainSettings
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
    api_instance = overseerr_api.SettingsApi(api_client)
    main_settings = overseerr_api.MainSettings() # MainSettings | 

    try:
        # Update main settings
        api_response = api_instance.settings_main_post(main_settings)
        print("The response of SettingsApi->settings_main_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_main_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **main_settings** | [**MainSettings**](MainSettings.md)|  | 

### Return type

[**MainSettings**](MainSettings.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Values were sucessfully updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_main_regenerate_post**
> MainSettings settings_main_regenerate_post()

Get main settings with newly-generated API key

Returns main settings in a JSON object, using the new API key.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.main_settings import MainSettings
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
    api_instance = overseerr_api.SettingsApi(api_client)

    try:
        # Get main settings with newly-generated API key
        api_response = api_instance.settings_main_regenerate_post()
        print("The response of SettingsApi->settings_main_regenerate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_main_regenerate_post: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**MainSettings**](MainSettings.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_notifications_discord_get**
> DiscordSettings settings_notifications_discord_get()

Get Discord notification settings

Returns current Discord notification settings in a JSON object.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.discord_settings import DiscordSettings
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
    api_instance = overseerr_api.SettingsApi(api_client)

    try:
        # Get Discord notification settings
        api_response = api_instance.settings_notifications_discord_get()
        print("The response of SettingsApi->settings_notifications_discord_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_notifications_discord_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**DiscordSettings**](DiscordSettings.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned Discord settings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_notifications_discord_post**
> DiscordSettings settings_notifications_discord_post(discord_settings)

Update Discord notification settings

Updates Discord notification settings with the provided values.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.discord_settings import DiscordSettings
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
    api_instance = overseerr_api.SettingsApi(api_client)
    discord_settings = overseerr_api.DiscordSettings() # DiscordSettings | 

    try:
        # Update Discord notification settings
        api_response = api_instance.settings_notifications_discord_post(discord_settings)
        print("The response of SettingsApi->settings_notifications_discord_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_notifications_discord_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **discord_settings** | [**DiscordSettings**](DiscordSettings.md)|  | 

### Return type

[**DiscordSettings**](DiscordSettings.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Values were sucessfully updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_notifications_discord_test_post**
> settings_notifications_discord_test_post(discord_settings)

Test Discord settings

Sends a test notification to the Discord agent.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.discord_settings import DiscordSettings
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
    api_instance = overseerr_api.SettingsApi(api_client)
    discord_settings = overseerr_api.DiscordSettings() # DiscordSettings | 

    try:
        # Test Discord settings
        api_instance.settings_notifications_discord_test_post(discord_settings)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_notifications_discord_test_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **discord_settings** | [**DiscordSettings**](DiscordSettings.md)|  | 

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
**204** | Test notification attempted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_notifications_email_get**
> NotificationEmailSettings settings_notifications_email_get()

Get email notification settings

Returns current email notification settings in a JSON object.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.notification_email_settings import NotificationEmailSettings
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
    api_instance = overseerr_api.SettingsApi(api_client)

    try:
        # Get email notification settings
        api_response = api_instance.settings_notifications_email_get()
        print("The response of SettingsApi->settings_notifications_email_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_notifications_email_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**NotificationEmailSettings**](NotificationEmailSettings.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned email settings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_notifications_email_post**
> NotificationEmailSettings settings_notifications_email_post(notification_email_settings)

Update email notification settings

Updates email notification settings with provided values

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.notification_email_settings import NotificationEmailSettings
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
    api_instance = overseerr_api.SettingsApi(api_client)
    notification_email_settings = overseerr_api.NotificationEmailSettings() # NotificationEmailSettings | 

    try:
        # Update email notification settings
        api_response = api_instance.settings_notifications_email_post(notification_email_settings)
        print("The response of SettingsApi->settings_notifications_email_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_notifications_email_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_email_settings** | [**NotificationEmailSettings**](NotificationEmailSettings.md)|  | 

### Return type

[**NotificationEmailSettings**](NotificationEmailSettings.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Values were sucessfully updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_notifications_email_test_post**
> settings_notifications_email_test_post(notification_email_settings)

Test email settings

Sends a test notification to the email agent.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.notification_email_settings import NotificationEmailSettings
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
    api_instance = overseerr_api.SettingsApi(api_client)
    notification_email_settings = overseerr_api.NotificationEmailSettings() # NotificationEmailSettings | 

    try:
        # Test email settings
        api_instance.settings_notifications_email_test_post(notification_email_settings)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_notifications_email_test_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_email_settings** | [**NotificationEmailSettings**](NotificationEmailSettings.md)|  | 

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
**204** | Test notification attempted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_notifications_gotify_get**
> GotifySettings settings_notifications_gotify_get()

Get Gotify notification settings

Returns current Gotify notification settings in a JSON object.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.gotify_settings import GotifySettings
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
    api_instance = overseerr_api.SettingsApi(api_client)

    try:
        # Get Gotify notification settings
        api_response = api_instance.settings_notifications_gotify_get()
        print("The response of SettingsApi->settings_notifications_gotify_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_notifications_gotify_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**GotifySettings**](GotifySettings.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned Gotify settings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_notifications_gotify_post**
> GotifySettings settings_notifications_gotify_post(gotify_settings)

Update Gotify notification settings

Update Gotify notification settings with the provided values.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.gotify_settings import GotifySettings
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
    api_instance = overseerr_api.SettingsApi(api_client)
    gotify_settings = overseerr_api.GotifySettings() # GotifySettings | 

    try:
        # Update Gotify notification settings
        api_response = api_instance.settings_notifications_gotify_post(gotify_settings)
        print("The response of SettingsApi->settings_notifications_gotify_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_notifications_gotify_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gotify_settings** | [**GotifySettings**](GotifySettings.md)|  | 

### Return type

[**GotifySettings**](GotifySettings.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Values were sucessfully updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_notifications_gotify_test_post**
> settings_notifications_gotify_test_post(gotify_settings)

Test Gotify settings

Sends a test notification to the Gotify agent.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.gotify_settings import GotifySettings
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
    api_instance = overseerr_api.SettingsApi(api_client)
    gotify_settings = overseerr_api.GotifySettings() # GotifySettings | 

    try:
        # Test Gotify settings
        api_instance.settings_notifications_gotify_test_post(gotify_settings)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_notifications_gotify_test_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gotify_settings** | [**GotifySettings**](GotifySettings.md)|  | 

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
**204** | Test notification attempted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_notifications_lunasea_get**
> LunaSeaSettings settings_notifications_lunasea_get()

Get LunaSea notification settings

Returns current LunaSea notification settings in a JSON object.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.luna_sea_settings import LunaSeaSettings
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
    api_instance = overseerr_api.SettingsApi(api_client)

    try:
        # Get LunaSea notification settings
        api_response = api_instance.settings_notifications_lunasea_get()
        print("The response of SettingsApi->settings_notifications_lunasea_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_notifications_lunasea_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**LunaSeaSettings**](LunaSeaSettings.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned LunaSea settings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_notifications_lunasea_post**
> LunaSeaSettings settings_notifications_lunasea_post(luna_sea_settings)

Update LunaSea notification settings

Updates LunaSea notification settings with the provided values.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.luna_sea_settings import LunaSeaSettings
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
    api_instance = overseerr_api.SettingsApi(api_client)
    luna_sea_settings = overseerr_api.LunaSeaSettings() # LunaSeaSettings | 

    try:
        # Update LunaSea notification settings
        api_response = api_instance.settings_notifications_lunasea_post(luna_sea_settings)
        print("The response of SettingsApi->settings_notifications_lunasea_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_notifications_lunasea_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **luna_sea_settings** | [**LunaSeaSettings**](LunaSeaSettings.md)|  | 

### Return type

[**LunaSeaSettings**](LunaSeaSettings.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Values were sucessfully updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_notifications_lunasea_test_post**
> settings_notifications_lunasea_test_post(luna_sea_settings)

Test LunaSea settings

Sends a test notification to the LunaSea agent.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.luna_sea_settings import LunaSeaSettings
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
    api_instance = overseerr_api.SettingsApi(api_client)
    luna_sea_settings = overseerr_api.LunaSeaSettings() # LunaSeaSettings | 

    try:
        # Test LunaSea settings
        api_instance.settings_notifications_lunasea_test_post(luna_sea_settings)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_notifications_lunasea_test_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **luna_sea_settings** | [**LunaSeaSettings**](LunaSeaSettings.md)|  | 

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
**204** | Test notification attempted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_notifications_pushbullet_get**
> PushbulletSettings settings_notifications_pushbullet_get()

Get Pushbullet notification settings

Returns current Pushbullet notification settings in a JSON object.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.pushbullet_settings import PushbulletSettings
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
    api_instance = overseerr_api.SettingsApi(api_client)

    try:
        # Get Pushbullet notification settings
        api_response = api_instance.settings_notifications_pushbullet_get()
        print("The response of SettingsApi->settings_notifications_pushbullet_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_notifications_pushbullet_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**PushbulletSettings**](PushbulletSettings.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned Pushbullet settings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_notifications_pushbullet_post**
> PushbulletSettings settings_notifications_pushbullet_post(pushbullet_settings)

Update Pushbullet notification settings

Update Pushbullet notification settings with the provided values.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.pushbullet_settings import PushbulletSettings
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
    api_instance = overseerr_api.SettingsApi(api_client)
    pushbullet_settings = overseerr_api.PushbulletSettings() # PushbulletSettings | 

    try:
        # Update Pushbullet notification settings
        api_response = api_instance.settings_notifications_pushbullet_post(pushbullet_settings)
        print("The response of SettingsApi->settings_notifications_pushbullet_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_notifications_pushbullet_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pushbullet_settings** | [**PushbulletSettings**](PushbulletSettings.md)|  | 

### Return type

[**PushbulletSettings**](PushbulletSettings.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Values were sucessfully updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_notifications_pushbullet_test_post**
> settings_notifications_pushbullet_test_post(pushbullet_settings)

Test Pushbullet settings

Sends a test notification to the Pushbullet agent.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.pushbullet_settings import PushbulletSettings
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
    api_instance = overseerr_api.SettingsApi(api_client)
    pushbullet_settings = overseerr_api.PushbulletSettings() # PushbulletSettings | 

    try:
        # Test Pushbullet settings
        api_instance.settings_notifications_pushbullet_test_post(pushbullet_settings)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_notifications_pushbullet_test_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pushbullet_settings** | [**PushbulletSettings**](PushbulletSettings.md)|  | 

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
**204** | Test notification attempted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_notifications_pushover_get**
> PushoverSettings settings_notifications_pushover_get()

Get Pushover notification settings

Returns current Pushover notification settings in a JSON object.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.pushover_settings import PushoverSettings
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
    api_instance = overseerr_api.SettingsApi(api_client)

    try:
        # Get Pushover notification settings
        api_response = api_instance.settings_notifications_pushover_get()
        print("The response of SettingsApi->settings_notifications_pushover_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_notifications_pushover_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**PushoverSettings**](PushoverSettings.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned Pushover settings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_notifications_pushover_post**
> PushoverSettings settings_notifications_pushover_post(pushover_settings)

Update Pushover notification settings

Update Pushover notification settings with the provided values.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.pushover_settings import PushoverSettings
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
    api_instance = overseerr_api.SettingsApi(api_client)
    pushover_settings = overseerr_api.PushoverSettings() # PushoverSettings | 

    try:
        # Update Pushover notification settings
        api_response = api_instance.settings_notifications_pushover_post(pushover_settings)
        print("The response of SettingsApi->settings_notifications_pushover_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_notifications_pushover_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pushover_settings** | [**PushoverSettings**](PushoverSettings.md)|  | 

### Return type

[**PushoverSettings**](PushoverSettings.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Values were sucessfully updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_notifications_pushover_sounds_get**
> List[SettingsNotificationsPushoverSoundsGet200ResponseInner] settings_notifications_pushover_sounds_get(token)

Get Pushover sounds

Returns valid Pushover sound options in a JSON array.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.settings_notifications_pushover_sounds_get200_response_inner import SettingsNotificationsPushoverSoundsGet200ResponseInner
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
    api_instance = overseerr_api.SettingsApi(api_client)
    token = 'token_example' # str | 

    try:
        # Get Pushover sounds
        api_response = api_instance.settings_notifications_pushover_sounds_get(token)
        print("The response of SettingsApi->settings_notifications_pushover_sounds_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_notifications_pushover_sounds_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

### Return type

[**List[SettingsNotificationsPushoverSoundsGet200ResponseInner]**](SettingsNotificationsPushoverSoundsGet200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned Pushover settings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_notifications_pushover_test_post**
> settings_notifications_pushover_test_post(pushover_settings)

Test Pushover settings

Sends a test notification to the Pushover agent.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.pushover_settings import PushoverSettings
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
    api_instance = overseerr_api.SettingsApi(api_client)
    pushover_settings = overseerr_api.PushoverSettings() # PushoverSettings | 

    try:
        # Test Pushover settings
        api_instance.settings_notifications_pushover_test_post(pushover_settings)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_notifications_pushover_test_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pushover_settings** | [**PushoverSettings**](PushoverSettings.md)|  | 

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
**204** | Test notification attempted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_notifications_slack_get**
> SlackSettings settings_notifications_slack_get()

Get Slack notification settings

Returns current Slack notification settings in a JSON object.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.slack_settings import SlackSettings
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
    api_instance = overseerr_api.SettingsApi(api_client)

    try:
        # Get Slack notification settings
        api_response = api_instance.settings_notifications_slack_get()
        print("The response of SettingsApi->settings_notifications_slack_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_notifications_slack_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**SlackSettings**](SlackSettings.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned slack settings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_notifications_slack_post**
> SlackSettings settings_notifications_slack_post(slack_settings)

Update Slack notification settings

Updates Slack notification settings with the provided values.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.slack_settings import SlackSettings
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
    api_instance = overseerr_api.SettingsApi(api_client)
    slack_settings = overseerr_api.SlackSettings() # SlackSettings | 

    try:
        # Update Slack notification settings
        api_response = api_instance.settings_notifications_slack_post(slack_settings)
        print("The response of SettingsApi->settings_notifications_slack_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_notifications_slack_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slack_settings** | [**SlackSettings**](SlackSettings.md)|  | 

### Return type

[**SlackSettings**](SlackSettings.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Values were sucessfully updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_notifications_slack_test_post**
> settings_notifications_slack_test_post(slack_settings)

Test Slack settings

Sends a test notification to the Slack agent.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.slack_settings import SlackSettings
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
    api_instance = overseerr_api.SettingsApi(api_client)
    slack_settings = overseerr_api.SlackSettings() # SlackSettings | 

    try:
        # Test Slack settings
        api_instance.settings_notifications_slack_test_post(slack_settings)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_notifications_slack_test_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slack_settings** | [**SlackSettings**](SlackSettings.md)|  | 

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
**204** | Test notification attempted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_notifications_telegram_get**
> TelegramSettings settings_notifications_telegram_get()

Get Telegram notification settings

Returns current Telegram notification settings in a JSON object.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.telegram_settings import TelegramSettings
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
    api_instance = overseerr_api.SettingsApi(api_client)

    try:
        # Get Telegram notification settings
        api_response = api_instance.settings_notifications_telegram_get()
        print("The response of SettingsApi->settings_notifications_telegram_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_notifications_telegram_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**TelegramSettings**](TelegramSettings.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned Telegram settings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_notifications_telegram_post**
> TelegramSettings settings_notifications_telegram_post(telegram_settings)

Update Telegram notification settings

Update Telegram notification settings with the provided values.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.telegram_settings import TelegramSettings
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
    api_instance = overseerr_api.SettingsApi(api_client)
    telegram_settings = overseerr_api.TelegramSettings() # TelegramSettings | 

    try:
        # Update Telegram notification settings
        api_response = api_instance.settings_notifications_telegram_post(telegram_settings)
        print("The response of SettingsApi->settings_notifications_telegram_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_notifications_telegram_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **telegram_settings** | [**TelegramSettings**](TelegramSettings.md)|  | 

### Return type

[**TelegramSettings**](TelegramSettings.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Values were sucessfully updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_notifications_telegram_test_post**
> settings_notifications_telegram_test_post(telegram_settings)

Test Telegram settings

Sends a test notification to the Telegram agent.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.telegram_settings import TelegramSettings
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
    api_instance = overseerr_api.SettingsApi(api_client)
    telegram_settings = overseerr_api.TelegramSettings() # TelegramSettings | 

    try:
        # Test Telegram settings
        api_instance.settings_notifications_telegram_test_post(telegram_settings)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_notifications_telegram_test_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **telegram_settings** | [**TelegramSettings**](TelegramSettings.md)|  | 

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
**204** | Test notification attempted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_notifications_webhook_get**
> WebhookSettings settings_notifications_webhook_get()

Get webhook notification settings

Returns current webhook notification settings in a JSON object.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.webhook_settings import WebhookSettings
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
    api_instance = overseerr_api.SettingsApi(api_client)

    try:
        # Get webhook notification settings
        api_response = api_instance.settings_notifications_webhook_get()
        print("The response of SettingsApi->settings_notifications_webhook_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_notifications_webhook_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**WebhookSettings**](WebhookSettings.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned webhook settings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_notifications_webhook_post**
> WebhookSettings settings_notifications_webhook_post(webhook_settings)

Update webhook notification settings

Updates webhook notification settings with the provided values.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.webhook_settings import WebhookSettings
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
    api_instance = overseerr_api.SettingsApi(api_client)
    webhook_settings = overseerr_api.WebhookSettings() # WebhookSettings | 

    try:
        # Update webhook notification settings
        api_response = api_instance.settings_notifications_webhook_post(webhook_settings)
        print("The response of SettingsApi->settings_notifications_webhook_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_notifications_webhook_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_settings** | [**WebhookSettings**](WebhookSettings.md)|  | 

### Return type

[**WebhookSettings**](WebhookSettings.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Values were sucessfully updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_notifications_webhook_test_post**
> settings_notifications_webhook_test_post(webhook_settings)

Test webhook settings

Sends a test notification to the webhook agent.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.webhook_settings import WebhookSettings
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
    api_instance = overseerr_api.SettingsApi(api_client)
    webhook_settings = overseerr_api.WebhookSettings() # WebhookSettings | 

    try:
        # Test webhook settings
        api_instance.settings_notifications_webhook_test_post(webhook_settings)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_notifications_webhook_test_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_settings** | [**WebhookSettings**](WebhookSettings.md)|  | 

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
**204** | Test notification attempted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_notifications_webpush_get**
> WebPushSettings settings_notifications_webpush_get()

Get Web Push notification settings

Returns current Web Push notification settings in a JSON object.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.web_push_settings import WebPushSettings
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
    api_instance = overseerr_api.SettingsApi(api_client)

    try:
        # Get Web Push notification settings
        api_response = api_instance.settings_notifications_webpush_get()
        print("The response of SettingsApi->settings_notifications_webpush_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_notifications_webpush_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**WebPushSettings**](WebPushSettings.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned web push settings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_notifications_webpush_post**
> WebPushSettings settings_notifications_webpush_post(web_push_settings)

Update Web Push notification settings

Updates Web Push notification settings with the provided values.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.web_push_settings import WebPushSettings
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
    api_instance = overseerr_api.SettingsApi(api_client)
    web_push_settings = overseerr_api.WebPushSettings() # WebPushSettings | 

    try:
        # Update Web Push notification settings
        api_response = api_instance.settings_notifications_webpush_post(web_push_settings)
        print("The response of SettingsApi->settings_notifications_webpush_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_notifications_webpush_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_push_settings** | [**WebPushSettings**](WebPushSettings.md)|  | 

### Return type

[**WebPushSettings**](WebPushSettings.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Values were sucessfully updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_notifications_webpush_test_post**
> settings_notifications_webpush_test_post(web_push_settings)

Test Web Push settings

Sends a test notification to the Web Push agent.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.web_push_settings import WebPushSettings
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
    api_instance = overseerr_api.SettingsApi(api_client)
    web_push_settings = overseerr_api.WebPushSettings() # WebPushSettings | 

    try:
        # Test Web Push settings
        api_instance.settings_notifications_webpush_test_post(web_push_settings)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_notifications_webpush_test_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_push_settings** | [**WebPushSettings**](WebPushSettings.md)|  | 

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
**204** | Test notification attempted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_plex_devices_servers_get**
> List[PlexDevice] settings_plex_devices_servers_get()

Gets the user's available Plex servers

Returns a list of available Plex servers and their connectivity state

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.plex_device import PlexDevice
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
    api_instance = overseerr_api.SettingsApi(api_client)

    try:
        # Gets the user's available Plex servers
        api_response = api_instance.settings_plex_devices_servers_get()
        print("The response of SettingsApi->settings_plex_devices_servers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_plex_devices_servers_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[PlexDevice]**](PlexDevice.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_plex_get**
> PlexSettings settings_plex_get()

Get Plex settings

Retrieves current Plex settings.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.plex_settings import PlexSettings
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
    api_instance = overseerr_api.SettingsApi(api_client)

    try:
        # Get Plex settings
        api_response = api_instance.settings_plex_get()
        print("The response of SettingsApi->settings_plex_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_plex_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**PlexSettings**](PlexSettings.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_plex_library_get**
> List[PlexLibrary] settings_plex_library_get(sync=sync, enable=enable)

Get Plex libraries

Returns a list of Plex libraries in a JSON array.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.plex_library import PlexLibrary
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
    api_instance = overseerr_api.SettingsApi(api_client)
    sync = 'sync_example' # str | Syncs the current libraries with the current Plex server (optional)
    enable = 'enable_example' # str | Comma separated list of libraries to enable. Any libraries not passed will be disabled! (optional)

    try:
        # Get Plex libraries
        api_response = api_instance.settings_plex_library_get(sync=sync, enable=enable)
        print("The response of SettingsApi->settings_plex_library_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_plex_library_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sync** | **str**| Syncs the current libraries with the current Plex server | [optional] 
 **enable** | **str**| Comma separated list of libraries to enable. Any libraries not passed will be disabled! | [optional] 

### Return type

[**List[PlexLibrary]**](PlexLibrary.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plex libraries returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_plex_post**
> PlexSettings settings_plex_post(plex_settings)

Update Plex settings

Updates Plex settings with the provided values.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.plex_settings import PlexSettings
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
    api_instance = overseerr_api.SettingsApi(api_client)
    plex_settings = overseerr_api.PlexSettings() # PlexSettings | 

    try:
        # Update Plex settings
        api_response = api_instance.settings_plex_post(plex_settings)
        print("The response of SettingsApi->settings_plex_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_plex_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plex_settings** | [**PlexSettings**](PlexSettings.md)|  | 

### Return type

[**PlexSettings**](PlexSettings.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Values were successfully updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_plex_sync_get**
> SettingsPlexSyncGet200Response settings_plex_sync_get()

Get status of full Plex library scan

Returns scan progress in a JSON array.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.settings_plex_sync_get200_response import SettingsPlexSyncGet200Response
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
    api_instance = overseerr_api.SettingsApi(api_client)

    try:
        # Get status of full Plex library scan
        api_response = api_instance.settings_plex_sync_get()
        print("The response of SettingsApi->settings_plex_sync_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_plex_sync_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**SettingsPlexSyncGet200Response**](SettingsPlexSyncGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status of Plex scan |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_plex_sync_post**
> SettingsPlexSyncGet200Response settings_plex_sync_post(settings_plex_sync_post_request=settings_plex_sync_post_request)

Start full Plex library scan

Runs a full Plex library scan and returns the progress in a JSON array.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.settings_plex_sync_get200_response import SettingsPlexSyncGet200Response
from overseerr_api.models.settings_plex_sync_post_request import SettingsPlexSyncPostRequest
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
    api_instance = overseerr_api.SettingsApi(api_client)
    settings_plex_sync_post_request = overseerr_api.SettingsPlexSyncPostRequest() # SettingsPlexSyncPostRequest |  (optional)

    try:
        # Start full Plex library scan
        api_response = api_instance.settings_plex_sync_post(settings_plex_sync_post_request=settings_plex_sync_post_request)
        print("The response of SettingsApi->settings_plex_sync_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_plex_sync_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_plex_sync_post_request** | [**SettingsPlexSyncPostRequest**](SettingsPlexSyncPostRequest.md)|  | [optional] 

### Return type

[**SettingsPlexSyncGet200Response**](SettingsPlexSyncGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status of Plex scan |  -  |

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
    api_instance = overseerr_api.SettingsApi(api_client)

    try:
        # Get Plex users
        api_response = api_instance.settings_plex_users_get()
        print("The response of SettingsApi->settings_plex_users_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_plex_users_get: %s\n" % e)
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

# **settings_public_get**
> PublicSettings settings_public_get()

Get public settings

Returns settings that are not protected or sensitive. Mainly used to determine if the application has been configured for the first time.

### Example

```python
import time
import os
import overseerr_api
from overseerr_api.models.public_settings import PublicSettings
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
    api_instance = overseerr_api.SettingsApi(api_client)

    try:
        # Get public settings
        api_response = api_instance.settings_public_get()
        print("The response of SettingsApi->settings_public_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_public_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**PublicSettings**](PublicSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Public settings returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_radarr_get**
> List[RadarrSettings] settings_radarr_get()

Get Radarr settings

Returns all Radarr settings in a JSON array.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.radarr_settings import RadarrSettings
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
    api_instance = overseerr_api.SettingsApi(api_client)

    try:
        # Get Radarr settings
        api_response = api_instance.settings_radarr_get()
        print("The response of SettingsApi->settings_radarr_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_radarr_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[RadarrSettings]**](RadarrSettings.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Values were returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_radarr_post**
> RadarrSettings settings_radarr_post(radarr_settings)

Create Radarr instance

Creates a new Radarr instance from the request body.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.radarr_settings import RadarrSettings
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
    api_instance = overseerr_api.SettingsApi(api_client)
    radarr_settings = overseerr_api.RadarrSettings() # RadarrSettings | 

    try:
        # Create Radarr instance
        api_response = api_instance.settings_radarr_post(radarr_settings)
        print("The response of SettingsApi->settings_radarr_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_radarr_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **radarr_settings** | [**RadarrSettings**](RadarrSettings.md)|  | 

### Return type

[**RadarrSettings**](RadarrSettings.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | New Radarr instance created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_radarr_radarr_id_delete**
> RadarrSettings settings_radarr_radarr_id_delete(radarr_id)

Delete Radarr instance

Deletes an existing Radarr instance based on the radarrId parameter.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.radarr_settings import RadarrSettings
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
    api_instance = overseerr_api.SettingsApi(api_client)
    radarr_id = 56 # int | Radarr instance ID

    try:
        # Delete Radarr instance
        api_response = api_instance.settings_radarr_radarr_id_delete(radarr_id)
        print("The response of SettingsApi->settings_radarr_radarr_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_radarr_radarr_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **radarr_id** | **int**| Radarr instance ID | 

### Return type

[**RadarrSettings**](RadarrSettings.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Radarr instance updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_radarr_radarr_id_profiles_get**
> List[ServiceProfile] settings_radarr_radarr_id_profiles_get(radarr_id)

Get available Radarr profiles

Returns a list of profiles available on the Radarr server instance in a JSON array.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.service_profile import ServiceProfile
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
    api_instance = overseerr_api.SettingsApi(api_client)
    radarr_id = 56 # int | Radarr instance ID

    try:
        # Get available Radarr profiles
        api_response = api_instance.settings_radarr_radarr_id_profiles_get(radarr_id)
        print("The response of SettingsApi->settings_radarr_radarr_id_profiles_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_radarr_radarr_id_profiles_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **radarr_id** | **int**| Radarr instance ID | 

### Return type

[**List[ServiceProfile]**](ServiceProfile.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned list of profiles |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_radarr_radarr_id_put**
> RadarrSettings settings_radarr_radarr_id_put(radarr_id, radarr_settings)

Update Radarr instance

Updates an existing Radarr instance with the provided values.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.radarr_settings import RadarrSettings
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
    api_instance = overseerr_api.SettingsApi(api_client)
    radarr_id = 56 # int | Radarr instance ID
    radarr_settings = overseerr_api.RadarrSettings() # RadarrSettings | 

    try:
        # Update Radarr instance
        api_response = api_instance.settings_radarr_radarr_id_put(radarr_id, radarr_settings)
        print("The response of SettingsApi->settings_radarr_radarr_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_radarr_radarr_id_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **radarr_id** | **int**| Radarr instance ID | 
 **radarr_settings** | [**RadarrSettings**](RadarrSettings.md)|  | 

### Return type

[**RadarrSettings**](RadarrSettings.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Radarr instance updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_radarr_test_post**
> SettingsRadarrTestPost200Response settings_radarr_test_post(settings_radarr_test_post_request)

Test Radarr configuration

Tests if the Radarr configuration is valid. Returns profiles and root folders on success.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.settings_radarr_test_post200_response import SettingsRadarrTestPost200Response
from overseerr_api.models.settings_radarr_test_post_request import SettingsRadarrTestPostRequest
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
    api_instance = overseerr_api.SettingsApi(api_client)
    settings_radarr_test_post_request = overseerr_api.SettingsRadarrTestPostRequest() # SettingsRadarrTestPostRequest | 

    try:
        # Test Radarr configuration
        api_response = api_instance.settings_radarr_test_post(settings_radarr_test_post_request)
        print("The response of SettingsApi->settings_radarr_test_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_radarr_test_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_radarr_test_post_request** | [**SettingsRadarrTestPostRequest**](SettingsRadarrTestPostRequest.md)|  | 

### Return type

[**SettingsRadarrTestPost200Response**](SettingsRadarrTestPost200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succesfully connected to Radarr instance |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_sonarr_get**
> List[SonarrSettings] settings_sonarr_get()

Get Sonarr settings

Returns all Sonarr settings in a JSON array.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.sonarr_settings import SonarrSettings
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
    api_instance = overseerr_api.SettingsApi(api_client)

    try:
        # Get Sonarr settings
        api_response = api_instance.settings_sonarr_get()
        print("The response of SettingsApi->settings_sonarr_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_sonarr_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[SonarrSettings]**](SonarrSettings.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Values were returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_sonarr_post**
> SonarrSettings settings_sonarr_post(sonarr_settings)

Create Sonarr instance

Creates a new Sonarr instance from the request body.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.sonarr_settings import SonarrSettings
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
    api_instance = overseerr_api.SettingsApi(api_client)
    sonarr_settings = overseerr_api.SonarrSettings() # SonarrSettings | 

    try:
        # Create Sonarr instance
        api_response = api_instance.settings_sonarr_post(sonarr_settings)
        print("The response of SettingsApi->settings_sonarr_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_sonarr_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sonarr_settings** | [**SonarrSettings**](SonarrSettings.md)|  | 

### Return type

[**SonarrSettings**](SonarrSettings.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | New Sonarr instance created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_sonarr_sonarr_id_delete**
> SonarrSettings settings_sonarr_sonarr_id_delete(sonarr_id)

Delete Sonarr instance

Deletes an existing Sonarr instance based on the sonarrId parameter.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.sonarr_settings import SonarrSettings
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
    api_instance = overseerr_api.SettingsApi(api_client)
    sonarr_id = 56 # int | Sonarr instance ID

    try:
        # Delete Sonarr instance
        api_response = api_instance.settings_sonarr_sonarr_id_delete(sonarr_id)
        print("The response of SettingsApi->settings_sonarr_sonarr_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_sonarr_sonarr_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sonarr_id** | **int**| Sonarr instance ID | 

### Return type

[**SonarrSettings**](SonarrSettings.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sonarr instance updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_sonarr_sonarr_id_put**
> SonarrSettings settings_sonarr_sonarr_id_put(sonarr_id, sonarr_settings)

Update Sonarr instance

Updates an existing Sonarr instance with the provided values.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.sonarr_settings import SonarrSettings
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
    api_instance = overseerr_api.SettingsApi(api_client)
    sonarr_id = 56 # int | Sonarr instance ID
    sonarr_settings = overseerr_api.SonarrSettings() # SonarrSettings | 

    try:
        # Update Sonarr instance
        api_response = api_instance.settings_sonarr_sonarr_id_put(sonarr_id, sonarr_settings)
        print("The response of SettingsApi->settings_sonarr_sonarr_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_sonarr_sonarr_id_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sonarr_id** | **int**| Sonarr instance ID | 
 **sonarr_settings** | [**SonarrSettings**](SonarrSettings.md)|  | 

### Return type

[**SonarrSettings**](SonarrSettings.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sonarr instance updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_sonarr_test_post**
> SettingsRadarrTestPost200Response settings_sonarr_test_post(settings_sonarr_test_post_request)

Test Sonarr configuration

Tests if the Sonarr configuration is valid. Returns profiles and root folders on success.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.settings_radarr_test_post200_response import SettingsRadarrTestPost200Response
from overseerr_api.models.settings_sonarr_test_post_request import SettingsSonarrTestPostRequest
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
    api_instance = overseerr_api.SettingsApi(api_client)
    settings_sonarr_test_post_request = overseerr_api.SettingsSonarrTestPostRequest() # SettingsSonarrTestPostRequest | 

    try:
        # Test Sonarr configuration
        api_response = api_instance.settings_sonarr_test_post(settings_sonarr_test_post_request)
        print("The response of SettingsApi->settings_sonarr_test_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_sonarr_test_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_sonarr_test_post_request** | [**SettingsSonarrTestPostRequest**](SettingsSonarrTestPostRequest.md)|  | 

### Return type

[**SettingsRadarrTestPost200Response**](SettingsRadarrTestPost200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succesfully connected to Sonarr instance |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_tautulli_get**
> TautulliSettings settings_tautulli_get()

Get Tautulli settings

Retrieves current Tautulli settings.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.tautulli_settings import TautulliSettings
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
    api_instance = overseerr_api.SettingsApi(api_client)

    try:
        # Get Tautulli settings
        api_response = api_instance.settings_tautulli_get()
        print("The response of SettingsApi->settings_tautulli_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_tautulli_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**TautulliSettings**](TautulliSettings.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_tautulli_post**
> TautulliSettings settings_tautulli_post(tautulli_settings)

Update Tautulli settings

Updates Tautulli settings with the provided values.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.tautulli_settings import TautulliSettings
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
    api_instance = overseerr_api.SettingsApi(api_client)
    tautulli_settings = overseerr_api.TautulliSettings() # TautulliSettings | 

    try:
        # Update Tautulli settings
        api_response = api_instance.settings_tautulli_post(tautulli_settings)
        print("The response of SettingsApi->settings_tautulli_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_tautulli_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tautulli_settings** | [**TautulliSettings**](TautulliSettings.md)|  | 

### Return type

[**TautulliSettings**](TautulliSettings.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Values were successfully updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

