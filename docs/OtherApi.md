# overseerr_api.OtherApi

All URIs are relative to *http://localhost:5055/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**keyword_keyword_id_get**](OtherApi.md#keyword_keyword_id_get) | **GET** /keyword/{keywordId} | Get keyword
[**watchproviders_movies_get**](OtherApi.md#watchproviders_movies_get) | **GET** /watchproviders/movies | Get watch provider movies
[**watchproviders_regions_get**](OtherApi.md#watchproviders_regions_get) | **GET** /watchproviders/regions | Get watch provider regions
[**watchproviders_tv_get**](OtherApi.md#watchproviders_tv_get) | **GET** /watchproviders/tv | Get watch provider series


# **keyword_keyword_id_get**
> Keyword keyword_keyword_id_get(keyword_id)

Get keyword

Returns a single keyword in JSON format. 

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.keyword import Keyword
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
    api_instance = overseerr_api.OtherApi(api_client)
    keyword_id = 1 # float | 

    try:
        # Get keyword
        api_response = api_instance.keyword_keyword_id_get(keyword_id)
        print("The response of OtherApi->keyword_keyword_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OtherApi->keyword_keyword_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyword_id** | **float**|  | 

### Return type

[**Keyword**](Keyword.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Keyword returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watchproviders_movies_get**
> List[WatchProviderDetails] watchproviders_movies_get(watch_region)

Get watch provider movies

Returns a list of all available watch providers for movies. 

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.watch_provider_details import WatchProviderDetails
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
    api_instance = overseerr_api.OtherApi(api_client)
    watch_region = 'US' # str | 

    try:
        # Get watch provider movies
        api_response = api_instance.watchproviders_movies_get(watch_region)
        print("The response of OtherApi->watchproviders_movies_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OtherApi->watchproviders_movies_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watch_region** | **str**|  | 

### Return type

[**List[WatchProviderDetails]**](WatchProviderDetails.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Watch providers for movies returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watchproviders_regions_get**
> List[WatchProviderRegion] watchproviders_regions_get()

Get watch provider regions

Returns a list of all available watch provider regions. 

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.watch_provider_region import WatchProviderRegion
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
    api_instance = overseerr_api.OtherApi(api_client)

    try:
        # Get watch provider regions
        api_response = api_instance.watchproviders_regions_get()
        print("The response of OtherApi->watchproviders_regions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OtherApi->watchproviders_regions_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[WatchProviderRegion]**](WatchProviderRegion.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Watch provider regions returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watchproviders_tv_get**
> List[WatchProviderDetails] watchproviders_tv_get(watch_region)

Get watch provider series

Returns a list of all available watch providers for series. 

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.watch_provider_details import WatchProviderDetails
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
    api_instance = overseerr_api.OtherApi(api_client)
    watch_region = 'US' # str | 

    try:
        # Get watch provider series
        api_response = api_instance.watchproviders_tv_get(watch_region)
        print("The response of OtherApi->watchproviders_tv_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OtherApi->watchproviders_tv_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watch_region** | **str**|  | 

### Return type

[**List[WatchProviderDetails]**](WatchProviderDetails.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Watch providers for series returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

