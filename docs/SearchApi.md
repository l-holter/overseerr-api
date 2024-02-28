# overseerr_api.SearchApi

All URIs are relative to *http://localhost:5055/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**discover_genreslider_movie_get**](SearchApi.md#discover_genreslider_movie_get) | **GET** /discover/genreslider/movie | Get genre slider data for movies
[**discover_genreslider_tv_get**](SearchApi.md#discover_genreslider_tv_get) | **GET** /discover/genreslider/tv | Get genre slider data for TV series
[**discover_keyword_keyword_id_movies_get**](SearchApi.md#discover_keyword_keyword_id_movies_get) | **GET** /discover/keyword/{keywordId}/movies | Get movies from keyword
[**discover_movies_genre_genre_id_get**](SearchApi.md#discover_movies_genre_genre_id_get) | **GET** /discover/movies/genre/{genreId} | Discover movies by genre
[**discover_movies_get**](SearchApi.md#discover_movies_get) | **GET** /discover/movies | Discover movies
[**discover_movies_language_language_get**](SearchApi.md#discover_movies_language_language_get) | **GET** /discover/movies/language/{language} | Discover movies by original language
[**discover_movies_studio_studio_id_get**](SearchApi.md#discover_movies_studio_studio_id_get) | **GET** /discover/movies/studio/{studioId} | Discover movies by studio
[**discover_movies_upcoming_get**](SearchApi.md#discover_movies_upcoming_get) | **GET** /discover/movies/upcoming | Upcoming movies
[**discover_trending_get**](SearchApi.md#discover_trending_get) | **GET** /discover/trending | Trending movies and TV
[**discover_tv_genre_genre_id_get**](SearchApi.md#discover_tv_genre_genre_id_get) | **GET** /discover/tv/genre/{genreId} | Discover TV shows by genre
[**discover_tv_get**](SearchApi.md#discover_tv_get) | **GET** /discover/tv | Discover TV shows
[**discover_tv_language_language_get**](SearchApi.md#discover_tv_language_language_get) | **GET** /discover/tv/language/{language} | Discover TV shows by original language
[**discover_tv_network_network_id_get**](SearchApi.md#discover_tv_network_network_id_get) | **GET** /discover/tv/network/{networkId} | Discover TV shows by network
[**discover_tv_upcoming_get**](SearchApi.md#discover_tv_upcoming_get) | **GET** /discover/tv/upcoming | Discover Upcoming TV shows
[**discover_watchlist_get**](SearchApi.md#discover_watchlist_get) | **GET** /discover/watchlist | Get the Plex watchlist.
[**search_company_get**](SearchApi.md#search_company_get) | **GET** /search/company | Search for companies
[**search_get**](SearchApi.md#search_get) | **GET** /search | Search for movies, TV shows, or people
[**search_keyword_get**](SearchApi.md#search_keyword_get) | **GET** /search/keyword | Search for keywords


# **discover_genreslider_movie_get**
> List[DiscoverGenresliderMovieGet200ResponseInner] discover_genreslider_movie_get(language=language)

Get genre slider data for movies

Returns a list of genres with backdrops attached

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.discover_genreslider_movie_get200_response_inner import DiscoverGenresliderMovieGet200ResponseInner
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
    api_instance = overseerr_api.SearchApi(api_client)
    language = 'en' # str |  (optional)

    try:
        # Get genre slider data for movies
        api_response = api_instance.discover_genreslider_movie_get(language=language)
        print("The response of SearchApi->discover_genreslider_movie_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->discover_genreslider_movie_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**|  | [optional] 

### Return type

[**List[DiscoverGenresliderMovieGet200ResponseInner]**](DiscoverGenresliderMovieGet200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Genre slider data returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discover_genreslider_tv_get**
> List[DiscoverGenresliderMovieGet200ResponseInner] discover_genreslider_tv_get(language=language)

Get genre slider data for TV series

Returns a list of genres with backdrops attached

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.discover_genreslider_movie_get200_response_inner import DiscoverGenresliderMovieGet200ResponseInner
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
    api_instance = overseerr_api.SearchApi(api_client)
    language = 'en' # str |  (optional)

    try:
        # Get genre slider data for TV series
        api_response = api_instance.discover_genreslider_tv_get(language=language)
        print("The response of SearchApi->discover_genreslider_tv_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->discover_genreslider_tv_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**|  | [optional] 

### Return type

[**List[DiscoverGenresliderMovieGet200ResponseInner]**](DiscoverGenresliderMovieGet200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Genre slider data returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discover_keyword_keyword_id_movies_get**
> DiscoverKeywordKeywordIdMoviesGet200Response discover_keyword_keyword_id_movies_get(keyword_id, page=page, language=language)

Get movies from keyword

Returns list of movies based on the provided keyword ID a JSON object.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.discover_keyword_keyword_id_movies_get200_response import DiscoverKeywordKeywordIdMoviesGet200Response
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
    api_instance = overseerr_api.SearchApi(api_client)
    keyword_id = 207317 # float | 
    page = 1 # float |  (optional) (default to 1)
    language = 'en' # str |  (optional)

    try:
        # Get movies from keyword
        api_response = api_instance.discover_keyword_keyword_id_movies_get(keyword_id, page=page, language=language)
        print("The response of SearchApi->discover_keyword_keyword_id_movies_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->discover_keyword_keyword_id_movies_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyword_id** | **float**|  | 
 **page** | **float**|  | [optional] [default to 1]
 **language** | **str**|  | [optional] 

### Return type

[**DiscoverKeywordKeywordIdMoviesGet200Response**](DiscoverKeywordKeywordIdMoviesGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of movies |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discover_movies_genre_genre_id_get**
> DiscoverMoviesGenreGenreIdGet200Response discover_movies_genre_genre_id_get(genre_id, page=page, language=language)

Discover movies by genre

Returns a list of movies based on the provided genre ID in a JSON object.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.discover_movies_genre_genre_id_get200_response import DiscoverMoviesGenreGenreIdGet200Response
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
    api_instance = overseerr_api.SearchApi(api_client)
    genre_id = '1' # str | 
    page = 1 # float |  (optional) (default to 1)
    language = 'en' # str |  (optional)

    try:
        # Discover movies by genre
        api_response = api_instance.discover_movies_genre_genre_id_get(genre_id, page=page, language=language)
        print("The response of SearchApi->discover_movies_genre_genre_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->discover_movies_genre_genre_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **genre_id** | **str**|  | 
 **page** | **float**|  | [optional] [default to 1]
 **language** | **str**|  | [optional] 

### Return type

[**DiscoverMoviesGenreGenreIdGet200Response**](DiscoverMoviesGenreGenreIdGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discover_movies_get**
> DiscoverKeywordKeywordIdMoviesGet200Response discover_movies_get(page=page, language=language, genre=genre, studio=studio, keywords=keywords, sort_by=sort_by, primary_release_date_gte=primary_release_date_gte, primary_release_date_lte=primary_release_date_lte, with_runtime_gte=with_runtime_gte, with_runtime_lte=with_runtime_lte, vote_average_gte=vote_average_gte, vote_average_lte=vote_average_lte, vote_count_gte=vote_count_gte, vote_count_lte=vote_count_lte, watch_region=watch_region, watch_providers=watch_providers)

Discover movies

Returns a list of movies in a JSON object.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.discover_keyword_keyword_id_movies_get200_response import DiscoverKeywordKeywordIdMoviesGet200Response
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
    api_instance = overseerr_api.SearchApi(api_client)
    page = 1 # float |  (optional) (default to 1)
    language = 'en' # str |  (optional)
    genre = '18' # str |  (optional)
    studio = 1 # float |  (optional)
    keywords = '1,2' # str |  (optional)
    sort_by = 'popularity.desc' # str |  (optional)
    primary_release_date_gte = '2022-01-01' # str |  (optional)
    primary_release_date_lte = '2023-01-01' # str |  (optional)
    with_runtime_gte = 60 # float |  (optional)
    with_runtime_lte = 120 # float |  (optional)
    vote_average_gte = 7 # float |  (optional)
    vote_average_lte = 10 # float |  (optional)
    vote_count_gte = 7 # float |  (optional)
    vote_count_lte = 10 # float |  (optional)
    watch_region = 'US' # str |  (optional)
    watch_providers = '8|9' # str |  (optional)

    try:
        # Discover movies
        api_response = api_instance.discover_movies_get(page=page, language=language, genre=genre, studio=studio, keywords=keywords, sort_by=sort_by, primary_release_date_gte=primary_release_date_gte, primary_release_date_lte=primary_release_date_lte, with_runtime_gte=with_runtime_gte, with_runtime_lte=with_runtime_lte, vote_average_gte=vote_average_gte, vote_average_lte=vote_average_lte, vote_count_gte=vote_count_gte, vote_count_lte=vote_count_lte, watch_region=watch_region, watch_providers=watch_providers)
        print("The response of SearchApi->discover_movies_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->discover_movies_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**|  | [optional] [default to 1]
 **language** | **str**|  | [optional] 
 **genre** | **str**|  | [optional] 
 **studio** | **float**|  | [optional] 
 **keywords** | **str**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **primary_release_date_gte** | **str**|  | [optional] 
 **primary_release_date_lte** | **str**|  | [optional] 
 **with_runtime_gte** | **float**|  | [optional] 
 **with_runtime_lte** | **float**|  | [optional] 
 **vote_average_gte** | **float**|  | [optional] 
 **vote_average_lte** | **float**|  | [optional] 
 **vote_count_gte** | **float**|  | [optional] 
 **vote_count_lte** | **float**|  | [optional] 
 **watch_region** | **str**|  | [optional] 
 **watch_providers** | **str**|  | [optional] 

### Return type

[**DiscoverKeywordKeywordIdMoviesGet200Response**](DiscoverKeywordKeywordIdMoviesGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discover_movies_language_language_get**
> DiscoverMoviesLanguageLanguageGet200Response discover_movies_language_language_get(language, page=page, language2=language2)

Discover movies by original language

Returns a list of movies based on the provided ISO 639-1 language code in a JSON object.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.discover_movies_language_language_get200_response import DiscoverMoviesLanguageLanguageGet200Response
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
    api_instance = overseerr_api.SearchApi(api_client)
    language = 'en' # str | 
    page = 1 # float |  (optional) (default to 1)
    language2 = 'en' # str |  (optional)

    try:
        # Discover movies by original language
        api_response = api_instance.discover_movies_language_language_get(language, page=page, language2=language2)
        print("The response of SearchApi->discover_movies_language_language_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->discover_movies_language_language_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**|  | 
 **page** | **float**|  | [optional] [default to 1]
 **language2** | **str**|  | [optional] 

### Return type

[**DiscoverMoviesLanguageLanguageGet200Response**](DiscoverMoviesLanguageLanguageGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discover_movies_studio_studio_id_get**
> DiscoverMoviesStudioStudioIdGet200Response discover_movies_studio_studio_id_get(studio_id, page=page, language=language)

Discover movies by studio

Returns a list of movies based on the provided studio ID in a JSON object.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.discover_movies_studio_studio_id_get200_response import DiscoverMoviesStudioStudioIdGet200Response
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
    api_instance = overseerr_api.SearchApi(api_client)
    studio_id = '1' # str | 
    page = 1 # float |  (optional) (default to 1)
    language = 'en' # str |  (optional)

    try:
        # Discover movies by studio
        api_response = api_instance.discover_movies_studio_studio_id_get(studio_id, page=page, language=language)
        print("The response of SearchApi->discover_movies_studio_studio_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->discover_movies_studio_studio_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **studio_id** | **str**|  | 
 **page** | **float**|  | [optional] [default to 1]
 **language** | **str**|  | [optional] 

### Return type

[**DiscoverMoviesStudioStudioIdGet200Response**](DiscoverMoviesStudioStudioIdGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discover_movies_upcoming_get**
> DiscoverKeywordKeywordIdMoviesGet200Response discover_movies_upcoming_get(page=page, language=language)

Upcoming movies

Returns a list of movies in a JSON object.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.discover_keyword_keyword_id_movies_get200_response import DiscoverKeywordKeywordIdMoviesGet200Response
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
    api_instance = overseerr_api.SearchApi(api_client)
    page = 1 # float |  (optional) (default to 1)
    language = 'en' # str |  (optional)

    try:
        # Upcoming movies
        api_response = api_instance.discover_movies_upcoming_get(page=page, language=language)
        print("The response of SearchApi->discover_movies_upcoming_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->discover_movies_upcoming_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**|  | [optional] [default to 1]
 **language** | **str**|  | [optional] 

### Return type

[**DiscoverKeywordKeywordIdMoviesGet200Response**](DiscoverKeywordKeywordIdMoviesGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discover_trending_get**
> DiscoverTrendingGet200Response discover_trending_get(page=page, language=language)

Trending movies and TV

Returns a list of movies and TV shows in a JSON object.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.discover_trending_get200_response import DiscoverTrendingGet200Response
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
    api_instance = overseerr_api.SearchApi(api_client)
    page = 1 # float |  (optional) (default to 1)
    language = 'en' # str |  (optional)

    try:
        # Trending movies and TV
        api_response = api_instance.discover_trending_get(page=page, language=language)
        print("The response of SearchApi->discover_trending_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->discover_trending_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**|  | [optional] [default to 1]
 **language** | **str**|  | [optional] 

### Return type

[**DiscoverTrendingGet200Response**](DiscoverTrendingGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discover_tv_genre_genre_id_get**
> DiscoverTvGenreGenreIdGet200Response discover_tv_genre_genre_id_get(genre_id, page=page, language=language)

Discover TV shows by genre

Returns a list of TV shows based on the provided genre ID in a JSON object.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.discover_tv_genre_genre_id_get200_response import DiscoverTvGenreGenreIdGet200Response
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
    api_instance = overseerr_api.SearchApi(api_client)
    genre_id = '1' # str | 
    page = 1 # float |  (optional) (default to 1)
    language = 'en' # str |  (optional)

    try:
        # Discover TV shows by genre
        api_response = api_instance.discover_tv_genre_genre_id_get(genre_id, page=page, language=language)
        print("The response of SearchApi->discover_tv_genre_genre_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->discover_tv_genre_genre_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **genre_id** | **str**|  | 
 **page** | **float**|  | [optional] [default to 1]
 **language** | **str**|  | [optional] 

### Return type

[**DiscoverTvGenreGenreIdGet200Response**](DiscoverTvGenreGenreIdGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discover_tv_get**
> DiscoverTvGet200Response discover_tv_get(page=page, language=language, genre=genre, network=network, keywords=keywords, sort_by=sort_by, first_air_date_gte=first_air_date_gte, first_air_date_lte=first_air_date_lte, with_runtime_gte=with_runtime_gte, with_runtime_lte=with_runtime_lte, vote_average_gte=vote_average_gte, vote_average_lte=vote_average_lte, vote_count_gte=vote_count_gte, vote_count_lte=vote_count_lte, watch_region=watch_region, watch_providers=watch_providers)

Discover TV shows

Returns a list of TV shows in a JSON object.

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
    api_instance = overseerr_api.SearchApi(api_client)
    page = 1 # float |  (optional) (default to 1)
    language = 'en' # str |  (optional)
    genre = '18' # str |  (optional)
    network = 1 # float |  (optional)
    keywords = '1,2' # str |  (optional)
    sort_by = 'popularity.desc' # str |  (optional)
    first_air_date_gte = '2022-01-01' # str |  (optional)
    first_air_date_lte = '2023-01-01' # str |  (optional)
    with_runtime_gte = 60 # float |  (optional)
    with_runtime_lte = 120 # float |  (optional)
    vote_average_gte = 7 # float |  (optional)
    vote_average_lte = 10 # float |  (optional)
    vote_count_gte = 7 # float |  (optional)
    vote_count_lte = 10 # float |  (optional)
    watch_region = 'US' # str |  (optional)
    watch_providers = '8|9' # str |  (optional)

    try:
        # Discover TV shows
        api_response = api_instance.discover_tv_get(page=page, language=language, genre=genre, network=network, keywords=keywords, sort_by=sort_by, first_air_date_gte=first_air_date_gte, first_air_date_lte=first_air_date_lte, with_runtime_gte=with_runtime_gte, with_runtime_lte=with_runtime_lte, vote_average_gte=vote_average_gte, vote_average_lte=vote_average_lte, vote_count_gte=vote_count_gte, vote_count_lte=vote_count_lte, watch_region=watch_region, watch_providers=watch_providers)
        print("The response of SearchApi->discover_tv_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->discover_tv_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**|  | [optional] [default to 1]
 **language** | **str**|  | [optional] 
 **genre** | **str**|  | [optional] 
 **network** | **float**|  | [optional] 
 **keywords** | **str**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **first_air_date_gte** | **str**|  | [optional] 
 **first_air_date_lte** | **str**|  | [optional] 
 **with_runtime_gte** | **float**|  | [optional] 
 **with_runtime_lte** | **float**|  | [optional] 
 **vote_average_gte** | **float**|  | [optional] 
 **vote_average_lte** | **float**|  | [optional] 
 **vote_count_gte** | **float**|  | [optional] 
 **vote_count_lte** | **float**|  | [optional] 
 **watch_region** | **str**|  | [optional] 
 **watch_providers** | **str**|  | [optional] 

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
**200** | Results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discover_tv_language_language_get**
> DiscoverTvLanguageLanguageGet200Response discover_tv_language_language_get(language, page=page, language2=language2)

Discover TV shows by original language

Returns a list of TV shows based on the provided ISO 639-1 language code in a JSON object.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.discover_tv_language_language_get200_response import DiscoverTvLanguageLanguageGet200Response
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
    api_instance = overseerr_api.SearchApi(api_client)
    language = 'en' # str | 
    page = 1 # float |  (optional) (default to 1)
    language2 = 'en' # str |  (optional)

    try:
        # Discover TV shows by original language
        api_response = api_instance.discover_tv_language_language_get(language, page=page, language2=language2)
        print("The response of SearchApi->discover_tv_language_language_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->discover_tv_language_language_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**|  | 
 **page** | **float**|  | [optional] [default to 1]
 **language2** | **str**|  | [optional] 

### Return type

[**DiscoverTvLanguageLanguageGet200Response**](DiscoverTvLanguageLanguageGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discover_tv_network_network_id_get**
> DiscoverTvNetworkNetworkIdGet200Response discover_tv_network_network_id_get(network_id, page=page, language=language)

Discover TV shows by network

Returns a list of TV shows based on the provided network ID in a JSON object.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.discover_tv_network_network_id_get200_response import DiscoverTvNetworkNetworkIdGet200Response
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
    api_instance = overseerr_api.SearchApi(api_client)
    network_id = '1' # str | 
    page = 1 # float |  (optional) (default to 1)
    language = 'en' # str |  (optional)

    try:
        # Discover TV shows by network
        api_response = api_instance.discover_tv_network_network_id_get(network_id, page=page, language=language)
        print("The response of SearchApi->discover_tv_network_network_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->discover_tv_network_network_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **str**|  | 
 **page** | **float**|  | [optional] [default to 1]
 **language** | **str**|  | [optional] 

### Return type

[**DiscoverTvNetworkNetworkIdGet200Response**](DiscoverTvNetworkNetworkIdGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discover_tv_upcoming_get**
> DiscoverTvGet200Response discover_tv_upcoming_get(page=page, language=language)

Discover Upcoming TV shows

Returns a list of upcoming TV shows in a JSON object.

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
    api_instance = overseerr_api.SearchApi(api_client)
    page = 1 # float |  (optional) (default to 1)
    language = 'en' # str |  (optional)

    try:
        # Discover Upcoming TV shows
        api_response = api_instance.discover_tv_upcoming_get(page=page, language=language)
        print("The response of SearchApi->discover_tv_upcoming_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->discover_tv_upcoming_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**200** | Results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discover_watchlist_get**
> DiscoverWatchlistGet200Response discover_watchlist_get(page=page)

Get the Plex watchlist.

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
    api_instance = overseerr_api.SearchApi(api_client)
    page = 1 # float |  (optional) (default to 1)

    try:
        # Get the Plex watchlist.
        api_response = api_instance.discover_watchlist_get(page=page)
        print("The response of SearchApi->discover_watchlist_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->discover_watchlist_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **search_company_get**
> SearchCompanyGet200Response search_company_get(query, page=page)

Search for companies

Returns a list of TMDB companies matching the search query. (Will not return origin country)

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.search_company_get200_response import SearchCompanyGet200Response
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
    api_instance = overseerr_api.SearchApi(api_client)
    query = 'Disney' # str | 
    page = 1 # float |  (optional) (default to 1)

    try:
        # Search for companies
        api_response = api_instance.search_company_get(query, page=page)
        print("The response of SearchApi->search_company_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_company_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | 
 **page** | **float**|  | [optional] [default to 1]

### Return type

[**SearchCompanyGet200Response**](SearchCompanyGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_get**
> DiscoverTrendingGet200Response search_get(query, page=page, language=language)

Search for movies, TV shows, or people

Returns a list of movies, TV shows, or people a JSON object.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.discover_trending_get200_response import DiscoverTrendingGet200Response
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
    api_instance = overseerr_api.SearchApi(api_client)
    query = 'Mulan' # str | 
    page = 1 # float |  (optional) (default to 1)
    language = 'en' # str |  (optional)

    try:
        # Search for movies, TV shows, or people
        api_response = api_instance.search_get(query, page=page, language=language)
        print("The response of SearchApi->search_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | 
 **page** | **float**|  | [optional] [default to 1]
 **language** | **str**|  | [optional] 

### Return type

[**DiscoverTrendingGet200Response**](DiscoverTrendingGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_keyword_get**
> SearchKeywordGet200Response search_keyword_get(query, page=page)

Search for keywords

Returns a list of TMDB keywords matching the search query

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):
```python
import time
import os
import overseerr_api
from overseerr_api.models.search_keyword_get200_response import SearchKeywordGet200Response
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
    api_instance = overseerr_api.SearchApi(api_client)
    query = 'christmas' # str | 
    page = 1 # float |  (optional) (default to 1)

    try:
        # Search for keywords
        api_response = api_instance.search_keyword_get(query, page=page)
        print("The response of SearchApi->search_keyword_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_keyword_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | 
 **page** | **float**|  | [optional] [default to 1]

### Return type

[**SearchKeywordGet200Response**](SearchKeywordGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

