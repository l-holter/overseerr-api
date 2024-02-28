# overseerr_api.TvApi

All URIs are relative to *http://localhost:5055/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tv_tv_id_get**](TvApi.md#tv_tv_id_get) | **GET** /tv/{tvId} | Get TV details
[**tv_tv_id_ratings_get**](TvApi.md#tv_tv_id_ratings_get) | **GET** /tv/{tvId}/ratings | Get TV ratings
[**tv_tv_id_recommendations_get**](TvApi.md#tv_tv_id_recommendations_get) | **GET** /tv/{tvId}/recommendations | Get recommended TV series
[**tv_tv_id_season_season_id_get**](TvApi.md#tv_tv_id_season_season_id_get) | **GET** /tv/{tvId}/season/{seasonId} | Get season details and episode list
[**tv_tv_id_similar_get**](TvApi.md#tv_tv_id_similar_get) | **GET** /tv/{tvId}/similar | Get similar TV series


# **tv_tv_id_get**
> TvDetails tv_tv_id_get(tv_id, language=language)

Get TV details

Returns full TV details in a JSON object.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.tv_details import TvDetails
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
    api_instance = overseerr_api.TvApi(api_client)
    tv_id = 76479 # float | 
    language = 'en' # str |  (optional)

    try:
        # Get TV details
        api_response = api_instance.tv_tv_id_get(tv_id, language=language)
        print("The response of TvApi->tv_tv_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TvApi->tv_tv_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tv_id** | **float**|  | 
 **language** | **str**|  | [optional] 

### Return type

[**TvDetails**](TvDetails.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TV details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_tv_id_ratings_get**
> TvTvIdRatingsGet200Response tv_tv_id_ratings_get(tv_id)

Get TV ratings

Returns ratings based on provided tvId in a JSON object.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.tv_tv_id_ratings_get200_response import TvTvIdRatingsGet200Response
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
    api_instance = overseerr_api.TvApi(api_client)
    tv_id = 76479 # float | 

    try:
        # Get TV ratings
        api_response = api_instance.tv_tv_id_ratings_get(tv_id)
        print("The response of TvApi->tv_tv_id_ratings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TvApi->tv_tv_id_ratings_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tv_id** | **float**|  | 

### Return type

[**TvTvIdRatingsGet200Response**](TvTvIdRatingsGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ratings returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_tv_id_recommendations_get**
> DiscoverTvGet200Response tv_tv_id_recommendations_get(tv_id, page=page, language=language)

Get recommended TV series

Returns list of recommended TV series based on the provided tvId in a JSON object.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.discover_tv_get200_response import DiscoverTvGet200Response
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
    api_instance = overseerr_api.TvApi(api_client)
    tv_id = 76479 # float | 
    page = 1 # float |  (optional) (default to 1)
    language = 'en' # str |  (optional)

    try:
        # Get recommended TV series
        api_response = api_instance.tv_tv_id_recommendations_get(tv_id, page=page, language=language)
        print("The response of TvApi->tv_tv_id_recommendations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TvApi->tv_tv_id_recommendations_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tv_id** | **float**|  | 
 **page** | **float**|  | [optional] [default to 1]
 **language** | **str**|  | [optional] 

### Return type

[**DiscoverTvGet200Response**](DiscoverTvGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of TV series |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_tv_id_season_season_id_get**
> Season tv_tv_id_season_season_id_get(tv_id, season_id, language=language)

Get season details and episode list

Returns season details with a list of episodes in a JSON object.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.season import Season
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
    api_instance = overseerr_api.TvApi(api_client)
    tv_id = 76479 # float | 
    season_id = 1 # float | 
    language = 'en' # str |  (optional)

    try:
        # Get season details and episode list
        api_response = api_instance.tv_tv_id_season_season_id_get(tv_id, season_id, language=language)
        print("The response of TvApi->tv_tv_id_season_season_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TvApi->tv_tv_id_season_season_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tv_id** | **float**|  | 
 **season_id** | **float**|  | 
 **language** | **str**|  | [optional] 

### Return type

[**Season**](Season.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TV details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_tv_id_similar_get**
> DiscoverTvGet200Response tv_tv_id_similar_get(tv_id, page=page, language=language)

Get similar TV series

Returns list of similar TV series based on the provided tvId in a JSON object.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.discover_tv_get200_response import DiscoverTvGet200Response
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
    api_instance = overseerr_api.TvApi(api_client)
    tv_id = 76479 # float | 
    page = 1 # float |  (optional) (default to 1)
    language = 'en' # str |  (optional)

    try:
        # Get similar TV series
        api_response = api_instance.tv_tv_id_similar_get(tv_id, page=page, language=language)
        print("The response of TvApi->tv_tv_id_similar_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TvApi->tv_tv_id_similar_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tv_id** | **float**|  | 
 **page** | **float**|  | [optional] [default to 1]
 **language** | **str**|  | [optional] 

### Return type

[**DiscoverTvGet200Response**](DiscoverTvGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of TV series |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

