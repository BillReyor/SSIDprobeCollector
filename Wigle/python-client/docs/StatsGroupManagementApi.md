# swagger_client.StatsGroupManagementApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_group**](StatsGroupManagementApi.md#admin_group) | **GET** /api/v2/group/admin | Get group info as a stats group administrator
[**group_members**](StatsGroupManagementApi.md#group_members) | **GET** /api/v2/group/groupMembers | Get group members


# **admin_group**
> GroupResponse admin_group(groupid=groupid)

Get group info as a stats group administrator



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatsGroupManagementApi()
groupid = 'groupid_example' # str | The unique string key of the group (optional)

try:
    # Get group info as a stats group administrator
    api_response = api_instance.admin_group(groupid=groupid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsGroupManagementApi->admin_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groupid** | **str**| The unique string key of the group | [optional] 

### Return type

[**GroupResponse**](GroupResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_members**
> GroupMemberResponse group_members(groupid=groupid)

Get group members



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatsGroupManagementApi()
groupid = 'groupid_example' # str | The unique numeric ID of the group (optional)

try:
    # Get group members
    api_response = api_instance.group_members(groupid=groupid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsGroupManagementApi->group_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groupid** | **str**| The unique numeric ID of the group | [optional] 

### Return type

[**GroupMemberResponse**](GroupMemberResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

