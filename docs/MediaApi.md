# overseerr_api.MediaApi

All URIs are relative to *http://localhost:5055/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**media_get**](MediaApi.md#media_get) | **GET** /media | Get media
[**media_media_id_delete**](MediaApi.md#media_media_id_delete) | **DELETE** /media/{mediaId} | Delete media item
[**media_media_id_status_post**](MediaApi.md#media_media_id_status_post) | **POST** /media/{mediaId}/{status} | Update media status
[**media_media_id_watch_data_get**](MediaApi.md#media_media_id_watch_data_get) | **GET** /media/{mediaId}/watch_data | Get watch data


# **media_get**
> MediaGet200Response media_get(take=take, skip=skip, filter=filter, sort=sort)

Get media

Returns all media (can be filtered and limited) in a JSON object.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.media_get200_response import MediaGet200Response
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
    api_instance = overseerr_api.MediaApi(api_client)
    take = 20 # float |  (optional)
    skip = 0 # float |  (optional)
    filter = 'filter_example' # str |  (optional)
    sort = 'added' # str |  (optional) (default to 'added')

    try:
        # Get media
        api_response = api_instance.media_get(take=take, skip=skip, filter=filter, sort=sort)
        print("The response of MediaApi->media_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaApi->media_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **take** | **float**|  | [optional] 
 **skip** | **float**|  | [optional] 
 **filter** | **str**|  | [optional] 
 **sort** | **str**|  | [optional] [default to &#39;added&#39;]

### Return type

[**MediaGet200Response**](MediaGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned media |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **media_media_id_delete**
> media_media_id_delete(media_id)

Delete media item

Removes a media item. The `MANAGE_REQUESTS` permission is required to perform this action.

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
    api_instance = overseerr_api.MediaApi(api_client)
    media_id = '1' # str | Media ID

    try:
        # Delete media item
        api_instance.media_media_id_delete(media_id)
    except Exception as e:
        print("Exception when calling MediaApi->media_media_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **media_id** | **str**| Media ID | 

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
**204** | Succesfully removed media item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **media_media_id_status_post**
> MediaInfo media_media_id_status_post(media_id, status, media_media_id_status_post_request=media_media_id_status_post_request)

Update media status

Updates a media item's status and returns the media in JSON format

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.media_info import MediaInfo
from overseerr_api.models.media_media_id_status_post_request import MediaMediaIdStatusPostRequest
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
    api_instance = overseerr_api.MediaApi(api_client)
    media_id = '1' # str | Media ID
    status = 'available' # str | New status
    media_media_id_status_post_request = overseerr_api.MediaMediaIdStatusPostRequest() # MediaMediaIdStatusPostRequest |  (optional)

    try:
        # Update media status
        api_response = api_instance.media_media_id_status_post(media_id, status, media_media_id_status_post_request=media_media_id_status_post_request)
        print("The response of MediaApi->media_media_id_status_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaApi->media_media_id_status_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **media_id** | **str**| Media ID | 
 **status** | **str**| New status | 
 **media_media_id_status_post_request** | [**MediaMediaIdStatusPostRequest**](MediaMediaIdStatusPostRequest.md)|  | [optional] 

### Return type

[**MediaInfo**](MediaInfo.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned media |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **media_media_id_watch_data_get**
> MediaMediaIdWatchDataGet200Response media_media_id_watch_data_get(media_id)

Get watch data

Returns play count, play duration, and users who have watched the media.  Requires the `ADMIN` permission. 

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.media_media_id_watch_data_get200_response import MediaMediaIdWatchDataGet200Response
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
    api_instance = overseerr_api.MediaApi(api_client)
    media_id = '1' # str | Media ID

    try:
        # Get watch data
        api_response = api_instance.media_media_id_watch_data_get(media_id)
        print("The response of MediaApi->media_media_id_watch_data_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaApi->media_media_id_watch_data_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **media_id** | **str**| Media ID | 

### Return type

[**MediaMediaIdWatchDataGet200Response**](MediaMediaIdWatchDataGet200Response.md)

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

