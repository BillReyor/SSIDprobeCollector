# swagger_client.V3ALPHAApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bt**](V3ALPHAApi.md#bt) | **GET** /api/v3/detail/bt/{btNetworkId} | Request detail for a bluetooth network
[**cdma_cell**](V3ALPHAApi.md#cdma_cell) | **GET** /api/v3/detail/cell/CDMA/{sid}/{nid}/{bsid} | Request detail for a CDMA network
[**cell**](V3ALPHAApi.md#cell) | **GET** /api/v3/detail/cell/{type}/{operator}/{lac}/{cid} | Request detail for a GSM, LTE, or WCDMA network
[**cell_channel**](V3ALPHAApi.md#cell_channel) | **GET** /api/v3/cellChannel/{type} | Request list of channels for GSM, LTE, or WCDMA transmitters in specified region
[**wifi**](V3ALPHAApi.md#wifi) | **GET** /api/v3/detail/wifi/{wifiNetworkId} | Request detail for a WiFi network


# **bt**
> BtDetail bt(bt_network_id)

Request detail for a bluetooth network

Location and detail properties for bluetooth networks. Detail endpoints are NOT included in COMMAPI subscriptions at this time.  Daily query limit subject to user DETAIL limit.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: user
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.V3ALPHAApi(swagger_client.ApiClient(configuration))
bt_network_id = 'bt_network_id_example' # str | Network ID.

try:
    # Request detail for a bluetooth network
    api_response = api_instance.bt(bt_network_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V3ALPHAApi->bt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_network_id** | **str**| Network ID. | 

### Return type

[**BtDetail**](BtDetail.md)

### Authorization

[user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cdma_cell**
> CellDetail cdma_cell(sid, nid, bsid)

Request detail for a CDMA network

Location and detail properties for CDMA networks. Detail endpoints are NOT included in COMMAPI subscriptions at this time.  Daily query limit subject to user DETAIL limit.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: user
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.V3ALPHAApi(swagger_client.ApiClient(configuration))
sid = 'sid_example' # str | CDMA System ID.
nid = 'nid_example' # str | CDMA Network ID.
bsid = 'bsid_example' # str | CDMA Base Station ID.

try:
    # Request detail for a CDMA network
    api_response = api_instance.cdma_cell(sid, nid, bsid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V3ALPHAApi->cdma_cell: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **str**| CDMA System ID. | 
 **nid** | **str**| CDMA Network ID. | 
 **bsid** | **str**| CDMA Base Station ID. | 

### Return type

[**CellDetail**](CellDetail.md)

### Authorization

[user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cell**
> BtDetail cell(operator, lac, cid, type)

Request detail for a GSM, LTE, or WCDMA network

Location and detail properties for non-CDMA cell types. Note that the type parameter is sensitive to current type in the WiGLE database - this means that LTE and WCDMA networks may have been reported as GSM in some packages, a fallback query to GSM is recommended if the LTE/WCDMA network appears to be absent. Detail endpoints are NOT included in COMMAPI subscriptions at this time.  Daily query limit subject to user DETAIL limit.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: user
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.V3ALPHAApi(swagger_client.ApiClient(configuration))
operator = 'operator_example' # str | GSM/LTE/WCDMA Operator ID
lac = 'lac_example' # str | GSM/LTE/WCDMA Location Area Code
cid = 'cid_example' # str | GSM/LTE/WCDMA Cell ID
type = 'type_example' # str | Network Type: GSM/LTE/WCDMA

try:
    # Request detail for a GSM, LTE, or WCDMA network
    api_response = api_instance.cell(operator, lac, cid, type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V3ALPHAApi->cell: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator** | **str**| GSM/LTE/WCDMA Operator ID | 
 **lac** | **str**| GSM/LTE/WCDMA Location Area Code | 
 **cid** | **str**| GSM/LTE/WCDMA Cell ID | 
 **type** | **str**| Network Type: GSM/LTE/WCDMA | 

### Return type

[**BtDetail**](BtDetail.md)

### Authorization

[user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cell_channel**
> ChannelDetailResponse cell_channel(type, latitude1, latitude2, longitude1, longitude2)

Request list of channels for GSM, LTE, or WCDMA transmitters in specified region

List of known channels and QoS values for any of the non-CDMA cell types in a bounding box. Note that the type parameter is sensitive to current type in the WiGLE database - this means that LTE and WCDMA networks may have been reported as GSM in some packages, a fallback query to GSM is recommended if the LTE/WCDMA network appears to be absent. Channel endpoints are NOT included in COMMAPI subscriptions at this time. Region cannot be large than 99 square miles (~256 sq km). Daily query limit subject to user DETAIL limit. Designed to support cell-site simulator detection.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: user
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.V3ALPHAApi(swagger_client.ApiClient(configuration))
type = 'type_example' # str | Network Type: GSM/LTE/WCDMA
latitude1 = 8.14 # float | First bounding latitude
latitude2 = 8.14 # float | Second bounding latitude
longitude1 = 8.14 # float | First bounding longitude
longitude2 = 8.14 # float | Second bounding longitude

try:
    # Request list of channels for GSM, LTE, or WCDMA transmitters in specified region
    api_response = api_instance.cell_channel(type, latitude1, latitude2, longitude1, longitude2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V3ALPHAApi->cell_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Network Type: GSM/LTE/WCDMA | 
 **latitude1** | **float**| First bounding latitude | 
 **latitude2** | **float**| Second bounding latitude | 
 **longitude1** | **float**| First bounding longitude | 
 **longitude2** | **float**| Second bounding longitude | 

### Return type

[**ChannelDetailResponse**](ChannelDetailResponse.md)

### Authorization

[user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wifi**
> WiFiDetail wifi(wifi_network_id)

Request detail for a WiFi network

Location and detail properties for WiFi networks. Detail endpoints are NOT included in COMMAPI subscriptions at this time.  Daily query limit subject to user DETAIL limit.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: user
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.V3ALPHAApi(swagger_client.ApiClient(configuration))
wifi_network_id = 'wifi_network_id_example' # str | Network ID.

try:
    # Request detail for a WiFi network
    api_response = api_instance.wifi(wifi_network_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V3ALPHAApi->wifi: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wifi_network_id** | **str**| Network ID. | 

### Return type

[**WiFiDetail**](WiFiDetail.md)

### Authorization

[user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

