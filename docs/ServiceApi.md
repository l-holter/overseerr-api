# overseerr_api.ServiceApi

All URIs are relative to *http://localhost:5055/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**service_radarr_get**](ServiceApi.md#service_radarr_get) | **GET** /service/radarr | Get non-sensitive Radarr server list
[**service_radarr_radarr_id_get**](ServiceApi.md#service_radarr_radarr_id_get) | **GET** /service/radarr/{radarrId} | Get Radarr server quality profiles and root folders
[**service_sonarr_get**](ServiceApi.md#service_sonarr_get) | **GET** /service/sonarr | Get non-sensitive Sonarr server list
[**service_sonarr_lookup_tmdb_id_get**](ServiceApi.md#service_sonarr_lookup_tmdb_id_get) | **GET** /service/sonarr/lookup/{tmdbId} | Get series from Sonarr
[**service_sonarr_sonarr_id_get**](ServiceApi.md#service_sonarr_sonarr_id_get) | **GET** /service/sonarr/{sonarrId} | Get Sonarr server quality profiles and root folders


# **service_radarr_get**
> List[RadarrSettings] service_radarr_get()

Get non-sensitive Radarr server list

Returns a list of Radarr server IDs and names in a JSON object.

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
    api_instance = overseerr_api.ServiceApi(api_client)

    try:
        # Get non-sensitive Radarr server list
        api_response = api_instance.service_radarr_get()
        print("The response of ServiceApi->service_radarr_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->service_radarr_get: %s\n" % e)
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
**200** | Request successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_radarr_radarr_id_get**
> ServiceRadarrRadarrIdGet200Response service_radarr_radarr_id_get(radarr_id)

Get Radarr server quality profiles and root folders

Returns a Radarr server's quality profile and root folder details in a JSON object.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.service_radarr_radarr_id_get200_response import ServiceRadarrRadarrIdGet200Response
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
    api_instance = overseerr_api.ServiceApi(api_client)
    radarr_id = 0 # float | 

    try:
        # Get Radarr server quality profiles and root folders
        api_response = api_instance.service_radarr_radarr_id_get(radarr_id)
        print("The response of ServiceApi->service_radarr_radarr_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->service_radarr_radarr_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **radarr_id** | **float**|  | 

### Return type

[**ServiceRadarrRadarrIdGet200Response**](ServiceRadarrRadarrIdGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_sonarr_get**
> List[SonarrSettings] service_sonarr_get()

Get non-sensitive Sonarr server list

Returns a list of Sonarr server IDs and names in a JSON object.

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
    api_instance = overseerr_api.ServiceApi(api_client)

    try:
        # Get non-sensitive Sonarr server list
        api_response = api_instance.service_sonarr_get()
        print("The response of ServiceApi->service_sonarr_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->service_sonarr_get: %s\n" % e)
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
**200** | Request successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_sonarr_lookup_tmdb_id_get**
> List[SonarrSeries] service_sonarr_lookup_tmdb_id_get(tmdb_id)

Get series from Sonarr

Returns a list of series returned by searching for the name in Sonarr.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.sonarr_series import SonarrSeries
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
    api_instance = overseerr_api.ServiceApi(api_client)
    tmdb_id = 0 # float | 

    try:
        # Get series from Sonarr
        api_response = api_instance.service_sonarr_lookup_tmdb_id_get(tmdb_id)
        print("The response of ServiceApi->service_sonarr_lookup_tmdb_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->service_sonarr_lookup_tmdb_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tmdb_id** | **float**|  | 

### Return type

[**List[SonarrSeries]**](SonarrSeries.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_sonarr_sonarr_id_get**
> ServiceSonarrSonarrIdGet200Response service_sonarr_sonarr_id_get(sonarr_id)

Get Sonarr server quality profiles and root folders

Returns a Sonarr server's quality profile and root folder details in a JSON object.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.service_sonarr_sonarr_id_get200_response import ServiceSonarrSonarrIdGet200Response
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
    api_instance = overseerr_api.ServiceApi(api_client)
    sonarr_id = 0 # float | 

    try:
        # Get Sonarr server quality profiles and root folders
        api_response = api_instance.service_sonarr_sonarr_id_get(sonarr_id)
        print("The response of ServiceApi->service_sonarr_sonarr_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->service_sonarr_sonarr_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sonarr_id** | **float**|  | 

### Return type

[**ServiceSonarrSonarrIdGet200Response**](ServiceSonarrSonarrIdGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

