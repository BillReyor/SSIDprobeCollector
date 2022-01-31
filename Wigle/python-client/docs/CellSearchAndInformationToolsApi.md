# swagger_client.CellSearchAndInformationToolsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mcc_mnc**](CellSearchAndInformationToolsApi.md#mcc_mnc) | **GET** /api/v2/cell/mccMnc | Get MCC and MNC codes for Cellular networks
[**search1**](CellSearchAndInformationToolsApi.md#search1) | **GET** /api/v2/cell/search | Search the WiGLE Cell database.


# **mcc_mnc**
> mcc_mnc(mcc=mcc, mnc=mnc)

Get MCC and MNC codes for Cellular networks

Get metadata for cell networks - optionally filter by country and network codes

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CellSearchAndInformationToolsApi()
mcc = 'mcc_example' # str | MCC to filter (optional)
mnc = 'mnc_example' # str | MNC to filter (optional)

try:
    # Get MCC and MNC codes for Cellular networks
    api_instance.mcc_mnc(mcc=mcc, mnc=mnc)
except ApiException as e:
    print("Exception when calling CellSearchAndInformationToolsApi->mcc_mnc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mcc** | **str**| MCC to filter | [optional] 
 **mnc** | **str**| MNC to filter | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search1**
> NetSearchResponse search1(onlymine=onlymine, notmine=notmine, latrange1=latrange1, latrange2=latrange2, longrange1=longrange1, longrange2=longrange2, lastupdt=lastupdt, start_trans_id=start_trans_id, end_trans_id=end_trans_id, cell_op=cell_op, cell_net=cell_net, cell_id=cell_id, ssid=ssid, ssidlike=ssidlike, min_qo_s=min_qo_s, show_gsm=show_gsm, show_cdma=show_cdma, show_lte=show_lte, show_wcdma=show_wcdma, variance=variance, house_number=house_number, road=road, city=city, region=region, postal_code=postal_code, country=country, results_per_page=results_per_page, search_after=search_after)

Search the WiGLE Cell database.

Query the WiGLE database for paginated results based on multiple criteria. API and session authentication default to a page size of 100 results/page. COMMAPI defaults to a page size of 25 with a maximum of 1000 results per return. Number of daily queries allowed per user are throttled based on history and participation.  Search endpoints are the only feature included in COMMAPI subscriptions at this time.<br><br>To get next page of results put the previous request's searchAfter value as a parameter in the new request's searchAfter.

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
api_instance = swagger_client.CellSearchAndInformationToolsApi(swagger_client.ApiClient(configuration))
onlymine = 'false' # str | Search only for points first discovered by the current user. Use any string to set, leave unset for general search. Can't be used with COMMAPI auth, since these are points you have locally. (optional) (default to false)
notmine = 'notmine_example' # str | Only search for networks first seen by other users (optional)
latrange1 = 8.14 # float | Lesser of two latitudes by which to bound the search (specify both) (optional)
latrange2 = 8.14 # float | Greater of two latitudes by which to bound the search (specify both) (optional)
longrange1 = 8.14 # float | Lesser of two longitudes by which to bound the search (specify both) (optional)
longrange2 = 8.14 # float | Greater of two longitudes by which to bound the search (specify both) (optional)
lastupdt = 'lastupdt_example' # str | Filter points by how recently they've been updated, condensed date/time numeric string format 'yyyyMMdd[hhmm[ss]]' (optional)
start_trans_id = 'start_trans_id_example' # str | Earliest transid by which to bound (year-level precision only), format 'yyyyMMdd-00000' (optional)
end_trans_id = 'end_trans_id_example' # str | Latest transid by which to bound (year-level precision only), format 'yyyyMMdd-00000' (optional)
cell_op = 'cell_op_example' # str | Cell Operator (GSM/LTE/WCDMA) or System (CDMA) ID parameter by which to filter (optional)
cell_net = 'cell_net_example' # str | Cell LAC (GSM/LTE/WCDMA) or Network (CDMA) ID parameter by which to filter (optional)
cell_id = 'cell_id_example' # str | Cell ID(GSM/LTE/WCDMA) or Basestation (CDMA) parameter by which to filter (optional)
ssid = 'ssid_example' # str | Include only cell towers exactly matching the string network name. (optional)
ssidlike = 'ssidlike_example' # str | Include only cell towers matching the string network name, allowing wildcards '%' (any string) and '_' (any character). (optional)
min_qo_s = 56 # int | Minimum Quality of Signal (0-7). (optional)
show_gsm = 'true' # str | Include GSM cell networks (optional) (default to true)
show_cdma = 'true' # str | Include CDMA cell networks (optional) (default to true)
show_lte = 'true' # str | Include LTE cell networks (optional) (default to true)
show_wcdma = 'true' # str | Include WCDMA cell networks (optional) (default to true)
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
    # Search the WiGLE Cell database.
    api_response = api_instance.search1(onlymine=onlymine, notmine=notmine, latrange1=latrange1, latrange2=latrange2, longrange1=longrange1, longrange2=longrange2, lastupdt=lastupdt, start_trans_id=start_trans_id, end_trans_id=end_trans_id, cell_op=cell_op, cell_net=cell_net, cell_id=cell_id, ssid=ssid, ssidlike=ssidlike, min_qo_s=min_qo_s, show_gsm=show_gsm, show_cdma=show_cdma, show_lte=show_lte, show_wcdma=show_wcdma, variance=variance, house_number=house_number, road=road, city=city, region=region, postal_code=postal_code, country=country, results_per_page=results_per_page, search_after=search_after)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CellSearchAndInformationToolsApi->search1: %s\n" % e)
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
 **cell_op** | **str**| Cell Operator (GSM/LTE/WCDMA) or System (CDMA) ID parameter by which to filter | [optional] 
 **cell_net** | **str**| Cell LAC (GSM/LTE/WCDMA) or Network (CDMA) ID parameter by which to filter | [optional] 
 **cell_id** | **str**| Cell ID(GSM/LTE/WCDMA) or Basestation (CDMA) parameter by which to filter | [optional] 
 **ssid** | **str**| Include only cell towers exactly matching the string network name. | [optional] 
 **ssidlike** | **str**| Include only cell towers matching the string network name, allowing wildcards &#39;%&#39; (any string) and &#39;_&#39; (any character). | [optional] 
 **min_qo_s** | **int**| Minimum Quality of Signal (0-7). | [optional] 
 **show_gsm** | **str**| Include GSM cell networks | [optional] [default to true]
 **show_cdma** | **str**| Include CDMA cell networks | [optional] [default to true]
 **show_lte** | **str**| Include LTE cell networks | [optional] [default to true]
 **show_wcdma** | **str**| Include WCDMA cell networks | [optional] [default to true]
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

