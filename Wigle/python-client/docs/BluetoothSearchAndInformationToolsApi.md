# swagger_client.BluetoothSearchAndInformationToolsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**detail**](BluetoothSearchAndInformationToolsApi.md#detail) | **GET** /api/v2/bluetooth/detail | Get details and observation records for a single network.
[**search**](BluetoothSearchAndInformationToolsApi.md#search) | **GET** /api/v2/bluetooth/search | Search the WiGLE Bluetooth database.


# **detail**
> NetSearchResponse detail(netid=netid, reverse_address=reverse_address)

Get details and observation records for a single network.

Provide unique information for a Bluetooth network. API and session authentication default to a page size of 100 results/page. Number of daily queries allowed per user are throttled based on history and participation. Detail endpoints are NOT included in COMMAPI subscriptions at this time.

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
api_instance = swagger_client.BluetoothSearchAndInformationToolsApi(swagger_client.ApiClient(configuration))
netid = 'netid_example' # str | The full Bluetooth Device ID to search (optional)
reverse_address = 'reverse_address_example' # str | Reverse geocode for an approximate address (optional)

try:
    # Get details and observation records for a single network.
    api_response = api_instance.detail(netid=netid, reverse_address=reverse_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BluetoothSearchAndInformationToolsApi->detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **netid** | **str**| The full Bluetooth Device ID to search | [optional] 
 **reverse_address** | **str**| Reverse geocode for an approximate address | [optional] 

### Return type

[**NetSearchResponse**](NetSearchResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search**
> NetSearchResponse search(onlymine=onlymine, notmine=notmine, latrange1=latrange1, latrange2=latrange2, longrange1=longrange1, longrange2=longrange2, lastupdt=lastupdt, start_trans_id=start_trans_id, end_trans_id=end_trans_id, netid=netid, name=name, namelike=namelike, show_bt=show_bt, show_ble=show_ble, min_qo_s=min_qo_s, variance=variance, house_number=house_number, road=road, city=city, region=region, postal_code=postal_code, country=country, results_per_page=results_per_page, search_after=search_after)

Search the WiGLE Bluetooth database.

Query the WiGLE database for paginated results based on multiple criteria. API and session authentication default to a page size of 100 results/page. COMMAPI defaults to a page size of 25 with a maximum of 1000 results per return. Number of daily queries allowed per user are throttled based on history and participation. Search endpoints are the only feature included in COMMAPI subscriptions at this time.<br><br>To get next page of results put the previous request's searchAfter value as a parameter in the new request's searchAfter.

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
api_instance = swagger_client.BluetoothSearchAndInformationToolsApi(swagger_client.ApiClient(configuration))
onlymine = 'false' # str | Search only for points first discovered by the current user. Use any string to set, leave unset for general search. Can't be used with COMMAPI auth, since these are points you have locally. (optional) (default to false)
notmine = 'notmine_example' # str | Only search for networks first seen by other users (optional)
latrange1 = 8.14 # float | Lesser of two latitudes by which to bound the search (specify both) (optional)
latrange2 = 8.14 # float | Greater of two latitudes by which to bound the search (specify both) (optional)
longrange1 = 8.14 # float | Lesser of two longitudes by which to bound the search (specify both) (optional)
longrange2 = 8.14 # float | Greater of two longitudes by which to bound the search (specify both) (optional)
lastupdt = 'lastupdt_example' # str | Filter points by how recently they've been updated, condensed date/time numeric string format 'yyyyMMdd[hhmm[ss]]' (optional)
start_trans_id = 'start_trans_id_example' # str | Earliest transid by which to bound (year-level precision only), format 'yyyyMMdd-00000' (optional)
end_trans_id = 'end_trans_id_example' # str | Latest transid by which to bound (year-level precision only), format 'yyyyMMdd-00000' (optional)
netid = 'netid_example' # str | Include only networks matching the string network BSSID, e.g. '0A:2C:EF:3D:25:1B' or '0A:2C:EF'. The first three octets are required. (optional)
name = 'name_example' # str | Include only networks exactly matching the string network name. (optional)
namelike = 'namelike_example' # str | Include only networks matching the string network name, allowing wildcards '%' (any string) and '_' (any character). (optional)
show_bt = 'true' # str | Include BT networks (optional) (default to true)
show_ble = 'true' # str | Include BLE networks (optional) (default to true)
min_qo_s = 56 # int | Minimum Quality of Signal (0-7). (optional)
variance = 8.14 # float | How tightly to bound queries against the provided latitude/longitude box. Value must be between 0.001 and 0.2. Intended for use with non-exact decimals and geocoded bounds. (optional)
house_number = 'house_number_example' # str | Street address house number (optional)
road = 'road_example' # str | Street address road (optional)
city = 'city_example' # str | Street address city (optional)
region = 'region_example' # str | Street address region (optional)
postal_code = 'postal_code_example' # str | Street address postal code (optional)
country = 'country_example' # str | Street address country (optional)
results_per_page = 789 # int | How many results to return per request. Defaults to 25 for COMMAPI, 100 for site. Bounded at 1000 for COMMAPI, 100 for site. (optional)
search_after = 'search_after_example' # str | Put in the previous page's searchAfter result to get the next page. Use this instead of 'first' (optional)

try:
    # Search the WiGLE Bluetooth database.
    api_response = api_instance.search(onlymine=onlymine, notmine=notmine, latrange1=latrange1, latrange2=latrange2, longrange1=longrange1, longrange2=longrange2, lastupdt=lastupdt, start_trans_id=start_trans_id, end_trans_id=end_trans_id, netid=netid, name=name, namelike=namelike, show_bt=show_bt, show_ble=show_ble, min_qo_s=min_qo_s, variance=variance, house_number=house_number, road=road, city=city, region=region, postal_code=postal_code, country=country, results_per_page=results_per_page, search_after=search_after)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BluetoothSearchAndInformationToolsApi->search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **onlymine** | **str**| Search only for points first discovered by the current user. Use any string to set, leave unset for general search. Can&#39;t be used with COMMAPI auth, since these are points you have locally. | [optional] [default to false]
 **notmine** | **str**| Only search for networks first seen by other users | [optional] 
 **latrange1** | **float**| Lesser of two latitudes by which to bound the search (specify both) | [optional] 
 **latrange2** | **float**| Greater of two latitudes by which to bound the search (specify both) | [optional] 
 **longrange1** | **float**| Lesser of two longitudes by which to bound the search (specify both) | [optional] 
 **longrange2** | **float**| Greater of two longitudes by which to bound the search (specify both) | [optional] 
 **lastupdt** | **str**| Filter points by how recently they&#39;ve been updated, condensed date/time numeric string format &#39;yyyyMMdd[hhmm[ss]]&#39; | [optional] 
 **start_trans_id** | **str**| Earliest transid by which to bound (year-level precision only), format &#39;yyyyMMdd-00000&#39; | [optional] 
 **end_trans_id** | **str**| Latest transid by which to bound (year-level precision only), format &#39;yyyyMMdd-00000&#39; | [optional] 
 **netid** | **str**| Include only networks matching the string network BSSID, e.g. &#39;0A:2C:EF:3D:25:1B&#39; or &#39;0A:2C:EF&#39;. The first three octets are required. | [optional] 
 **name** | **str**| Include only networks exactly matching the string network name. | [optional] 
 **namelike** | **str**| Include only networks matching the string network name, allowing wildcards &#39;%&#39; (any string) and &#39;_&#39; (any character). | [optional] 
 **show_bt** | **str**| Include BT networks | [optional] [default to true]
 **show_ble** | **str**| Include BLE networks | [optional] [default to true]
 **min_qo_s** | **int**| Minimum Quality of Signal (0-7). | [optional] 
 **variance** | **float**| How tightly to bound queries against the provided latitude/longitude box. Value must be between 0.001 and 0.2. Intended for use with non-exact decimals and geocoded bounds. | [optional] 
 **house_number** | **str**| Street address house number | [optional] 
 **road** | **str**| Street address road | [optional] 
 **city** | **str**| Street address city | [optional] 
 **region** | **str**| Street address region | [optional] 
 **postal_code** | **str**| Street address postal code | [optional] 
 **country** | **str**| Street address country | [optional] 
 **results_per_page** | **int**| How many results to return per request. Defaults to 25 for COMMAPI, 100 for site. Bounded at 1000 for COMMAPI, 100 for site. | [optional] 
 **search_after** | **str**| Put in the previous page&#39;s searchAfter result to get the next page. Use this instead of &#39;first&#39; | [optional] 

### Return type

[**NetSearchResponse**](NetSearchResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

