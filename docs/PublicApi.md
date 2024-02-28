# overseerr_api.PublicApi

All URIs are relative to *http://localhost:5055/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**status_appdata_get**](PublicApi.md#status_appdata_get) | **GET** /status/appdata | Get application data volume status
[**status_get**](PublicApi.md#status_get) | **GET** /status | Get Overseerr status


# **status_appdata_get**
> StatusAppdataGet200Response status_appdata_get()

Get application data volume status

For Docker installs, returns whether or not the volume mount was configured properly. Always returns true for non-Docker installs.

### Example

```python
import time
import os
import overseerr_api
from overseerr_api.models.status_appdata_get200_response import StatusAppdataGet200Response
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
    api_instance = overseerr_api.PublicApi(api_client)

    try:
        # Get application data volume status
        api_response = api_instance.status_appdata_get()
        print("The response of PublicApi->status_appdata_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->status_appdata_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**StatusAppdataGet200Response**](StatusAppdataGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Application data volume status and path |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status_get**
> StatusGet200Response status_get()

Get Overseerr status

Returns the current Overseerr status in a JSON object.

### Example

```python
import time
import os
import overseerr_api
from overseerr_api.models.status_get200_response import StatusGet200Response
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
    api_instance = overseerr_api.PublicApi(api_client)

    try:
        # Get Overseerr status
        api_response = api_instance.status_get()
        print("The response of PublicApi->status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->status_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**StatusGet200Response**](StatusGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned status |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

