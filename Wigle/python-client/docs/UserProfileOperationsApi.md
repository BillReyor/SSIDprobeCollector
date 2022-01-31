# swagger_client.UserProfileOperationsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_token**](UserProfileOperationsApi.md#api_token) | **GET** /api/v2/profile/apiToken | Get all authorization tokens for the logged-in user
[**user**](UserProfileOperationsApi.md#user) | **GET** /api/v2/profile/user | Get the user object for the current logged-in user


# **api_token**
> AuthTokensResponse api_token(type=type)

Get all authorization tokens for the logged-in user



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
api_instance = swagger_client.UserProfileOperationsApi(swagger_client.ApiClient(configuration))
type = 'type_example' # str | Token types - 'API', 'COMMAPI', or 'ANDROID' (optional)

try:
    # Get all authorization tokens for the logged-in user
    api_response = api_instance.api_token(type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserProfileOperationsApi->api_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Token types - &#39;API&#39;, &#39;COMMAPI&#39;, or &#39;ANDROID&#39; | [optional] 

### Return type

[**AuthTokensResponse**](AuthTokensResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user**
> Person user()

Get the user object for the current logged-in user

See basic user information.

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
api_instance = swagger_client.UserProfileOperationsApi(swagger_client.ApiClient(configuration))

try:
    # Get the user object for the current logged-in user
    api_response = api_instance.user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserProfileOperationsApi->user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Person**](Person.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

