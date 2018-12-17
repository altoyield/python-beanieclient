# beanie.StockLocationApi

All URIs are relative to *https://bean.ie*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_stock_location**](StockLocationApi.md#add_stock_location) | **POST** /stock_locations | 
[**find_stock_location_by_id**](StockLocationApi.md#find_stock_location_by_id) | **GET** /stock_locations/{id} | Find Stock location by ID
[**find_stock_locations**](StockLocationApi.md#find_stock_locations) | **GET** /stock_locations | All stock location


# **add_stock_location**
> StockLocation add_stock_location(stock_locations)



Creates a new stock location in the system

### Example
```python
from __future__ import print_function
import time
import beanie
from beanie.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = beanie.Configuration()
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# create an instance of the API class
api_instance = beanie.StockLocationApi(beanie.ApiClient(configuration))
stock_locations = beanie.StockLocationInput() # StockLocationInput | Stock location to add to the system

try:
    api_response = api_instance.add_stock_location(stock_locations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockLocationApi->add_stock_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_locations** | [**StockLocationInput**](StockLocationInput.md)| Stock location to add to the system | 

### Return type

[**StockLocation**](StockLocation.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_stock_location_by_id**
> StockLocation find_stock_location_by_id(id)

Find Stock location by ID

Returns a single stock location if the user has access

### Example
```python
from __future__ import print_function
import time
import beanie
from beanie.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = beanie.Configuration()
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# create an instance of the API class
api_instance = beanie.StockLocationApi(beanie.ApiClient(configuration))
id = 789 # int | ID of stock location to fetch

try:
    # Find Stock location by ID
    api_response = api_instance.find_stock_location_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockLocationApi->find_stock_location_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of stock location to fetch | 

### Return type

[**StockLocation**](StockLocation.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_stock_locations**
> list[StockLocation] find_stock_locations(tags=tags, limit=limit)

All stock location

Returns all stock location from the system that the user has access to

### Example
```python
from __future__ import print_function
import time
import beanie
from beanie.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = beanie.Configuration()
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# create an instance of the API class
api_instance = beanie.StockLocationApi(beanie.ApiClient(configuration))
tags = ['tags_example'] # list[str] | tags to filter by (optional)
limit = 56 # int | Maximum number of results to return (optional)

try:
    # All stock location
    api_response = api_instance.find_stock_locations(tags=tags, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockLocationApi->find_stock_locations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tags** | [**list[str]**](str.md)| tags to filter by | [optional] 
 **limit** | **int**| Maximum number of results to return | [optional] 

### Return type

[**list[StockLocation]**](StockLocation.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

