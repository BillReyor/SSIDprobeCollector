# swagger_client.NetworkObservationFileUploadAndStatus_Api

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_kml_for_trans_id**](NetworkObservationFileUploadAndStatus_Api.md#get_kml_for_trans_id) | **GET** /api/v2/file/kml/{transid} | Download a KML summary of a file
[**get_trans_logs_for_user**](NetworkObservationFileUploadAndStatus_Api.md#get_trans_logs_for_user) | **GET** /api/v2/file/transactions | Get the status of files uploaded by the current user
[**upload**](NetworkObservationFileUploadAndStatus_Api.md#upload) | **POST** /api/v2/file/upload | Upload a file


# **get_kml_for_trans_id**
> get_kml_for_trans_id(transid)

Download a KML summary of a file

Get a KML summary approximation for a successfully processed file uploaded by the current user

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
api_instance = swagger_client.NetworkObservationFileUploadAndStatus_Api(swagger_client.ApiClient(configuration))
transid = 'transid_example' # str | The unique transaction ID for the file

try:
    # Download a KML summary of a file
    api_instance.get_kml_for_trans_id(transid)
except ApiException as e:
    print("Exception when calling NetworkObservationFileUploadAndStatus_Api->get_kml_for_trans_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transid** | **str**| The unique transaction ID for the file | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.google-earth.kml+xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trans_logs_for_user**
> TranslogResponse get_trans_logs_for_user(pagestart=pagestart, pageend=pageend)

Get the status of files uploaded by the current user

Results in response model paginated at 100 results per page

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
api_instance = swagger_client.NetworkObservationFileUploadAndStatus_Api(swagger_client.ApiClient(configuration))
pagestart = 0 # int | Most recent record to fetch descending chronologically. Defaults to 0 (optional) (default to 0)
pageend = 789 # int | Number of results to fetch from offset. Defaults to 100 (optional)

try:
    # Get the status of files uploaded by the current user
    api_response = api_instance.get_trans_logs_for_user(pagestart=pagestart, pageend=pageend)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkObservationFileUploadAndStatus_Api->get_trans_logs_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagestart** | **int**| Most recent record to fetch descending chronologically. Defaults to 0 | [optional] [default to 0]
 **pageend** | **int**| Number of results to fetch from offset. Defaults to 100 | [optional] 

### Return type

[**TranslogResponse**](TranslogResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload**
> UploadResponse upload(file, donate=donate)

Upload a file

Transmit a file for processing and incorporation into the database. Supports DStumbler, G-Mon, inSSIDer, Kismac, Kismet, MacStumbler, NetStumbler, Pocket Warrior, Wardrive-Android, WiFiFoFum, WiFi-Where, WiGLE WiFi Wardriving, and Apple consolidated DB formats. One or more files may be enclosed within a zip, tar, or tar.gz archive. Files may not exceed 180MiB, and archives WILL IGNORE more than 200 member files. For documentation on WiGLE Wireless CSV files, see https://api.wigle.net/csvFormat.html

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetworkObservationFileUploadAndStatus_Api()
file = '/path/to/file.txt' # file | multipart/form-data file; proper formulation requires both filename and payload.
donate = 'on' # str | Allow commercial use of the file contents - 'on' to allow. (optional) (default to on)

try:
    # Upload a file
    api_response = api_instance.upload(file, donate=donate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkObservationFileUploadAndStatus_Api->upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| multipart/form-data file; proper formulation requires both filename and payload. | 
 **donate** | **str**| Allow commercial use of the file contents - &#39;on&#39; to allow. | [optional] [default to on]

### Return type

[**UploadResponse**](UploadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

