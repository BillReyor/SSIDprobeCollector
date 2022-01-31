# swagger_client.StatisticsAndInformationApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**countries**](StatisticsAndInformationApi.md#countries) | **GET** /api/v2/stats/countries | Get statistics organized by country
[**country_region**](StatisticsAndInformationApi.md#country_region) | **GET** /api/v2/stats/regions | Get statistics for a specified country, organized by region, postal code, and encryption
[**general_stats**](StatisticsAndInformationApi.md#general_stats) | **GET** /api/v2/stats/general | Get a named map of general statistics
[**group_stats**](StatisticsAndInformationApi.md#group_stats) | **GET** /api/v2/stats/group | Get group standings
[**site_stats**](StatisticsAndInformationApi.md#site_stats) | **GET** /api/v2/stats/site | Get a named map of site-level statistics
[**stats**](StatisticsAndInformationApi.md#stats) | **GET** /api/v2/stats/standings | Get user standings
[**user_statistics**](StatisticsAndInformationApi.md#user_statistics) | **GET** /api/v2/stats/user | Get user statistics


# **countries**
> CountriesResponse countries()

Get statistics organized by country

Fetches all countries and basic stats

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatisticsAndInformationApi()

try:
    # Get statistics organized by country
    api_response = api_instance.countries()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsAndInformationApi->countries: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CountriesResponse**](CountriesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **country_region**
> RegionResponse country_region(country=country)

Get statistics for a specified country, organized by region, postal code, and encryption



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatisticsAndInformationApi()
country = 'US' # str | the two-letter code of the country for which you'd like a regional breakdown. Defaults to 'US' (optional) (default to US)

try:
    # Get statistics for a specified country, organized by region, postal code, and encryption
    api_response = api_instance.country_region(country=country)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsAndInformationApi->country_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| the two-letter code of the country for which you&#39;d like a regional breakdown. Defaults to &#39;US&#39; | [optional] [default to US]

### Return type

[**RegionResponse**](RegionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **general_stats**
> dict(str, object) general_stats()

Get a named map of general statistics



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatisticsAndInformationApi()

try:
    # Get a named map of general statistics
    api_response = api_instance.general_stats()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsAndInformationApi->general_stats: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_stats**
> GroupStatResponse group_stats()

Get group standings

Fetches a list of all teams. Authenticated users receive additional group info for the group they administer.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatisticsAndInformationApi()

try:
    # Get group standings
    api_response = api_instance.group_stats()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsAndInformationApi->group_stats: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GroupStatResponse**](GroupStatResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **site_stats**
> dict(str, object) site_stats()

Get a named map of site-level statistics

A big hash of short-named statistics used in providing site-wide information.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatisticsAndInformationApi()

try:
    # Get a named map of site-level statistics
    api_response = api_instance.site_stats()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsAndInformationApi->site_stats: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stats**
> stats(sort=sort, pagestart=pagestart, pageend=pageend)

Get user standings



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatisticsAndInformationApi()
sort = 'discovered' # str | The criteria by which to sort the results. Values are ['discovered', 'total', 'monthcount', 'prevmonthcount', 'gendisc', 'gentotal', 'firsttransid', 'lasttransid'] (optional) (default to discovered)
pagestart = 0 # int | The first record to request according to the 'sort' parameter (optional) (default to 0)
pageend = 789 # int | The last record to request according to the 'sort' parameter (optional)

try:
    # Get user standings
    api_instance.stats(sort=sort, pagestart=pagestart, pageend=pageend)
except ApiException as e:
    print("Exception when calling StatisticsAndInformationApi->stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| The criteria by which to sort the results. Values are [&#39;discovered&#39;, &#39;total&#39;, &#39;monthcount&#39;, &#39;prevmonthcount&#39;, &#39;gendisc&#39;, &#39;gentotal&#39;, &#39;firsttransid&#39;, &#39;lasttransid&#39;] | [optional] [default to discovered]
 **pagestart** | **int**| The first record to request according to the &#39;sort&#39; parameter | [optional] [default to 0]
 **pageend** | **int**| The last record to request according to the &#39;sort&#39; parameter | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_statistics**
> UserStatsResponse user_statistics(user=user)

Get user statistics

Get statistics and badge image for the authenticated user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.StatisticsAndInformationApi(swagger_client.ApiClient(configuration))
user = 'user_example' # str | the name of the user for whom to get stats (optional)

try:
    # Get user statistics
    api_response = api_instance.user_statistics(user=user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsAndInformationApi->user_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| the name of the user for whom to get stats | [optional] 

### Return type

[**UserStatsResponse**](UserStatsResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

