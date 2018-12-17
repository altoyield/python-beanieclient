# beanie.StockItemApi

All URIs are relative to *https://bean.ie*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_stock_item**](StockItemApi.md#add_stock_item) | **POST** /stock_items | 
[**find_stock_item_by_id**](StockItemApi.md#find_stock_item_by_id) | **GET** /stock_items/{id} | Find Stock item by ID
[**find_stock_items**](StockItemApi.md#find_stock_items) | **GET** /stock_items | All stock item


# **add_stock_item**
> StockItem add_stock_item(stock_items)



Creates a new stock item in the system

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
api_instance = beanie.StockItemApi(beanie.ApiClient(configuration))
stock_items = beanie.StockItemInput() # StockItemInput | Stock item to add to the system

try:
    api_response = api_instance.add_stock_item(stock_items)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockItemApi->add_stock_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_items** | [**StockItemInput**](StockItemInput.md)| Stock item to add to the system | 

### Return type

[**StockItem**](StockItem.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_stock_item_by_id**
> StockItem find_stock_item_by_id(id)

Find Stock item by ID

Returns a single stock item if the user has access

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
api_instance = beanie.StockItemApi(beanie.ApiClient(configuration))
id = 789 # int | ID of stock item to fetch

try:
    # Find Stock item by ID
    api_response = api_instance.find_stock_item_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockItemApi->find_stock_item_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of stock item to fetch | 

### Return type

[**StockItem**](StockItem.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_stock_items**
> list[StockItem] find_stock_items(tags=tags, limit=limit)

All stock item

Returns all stock item from the system that the user has access to

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
api_instance = beanie.StockItemApi(beanie.ApiClient(configuration))
tags = ['tags_example'] # list[str] | tags to filter by (optional)
limit = 56 # int | Maximum number of results to return (optional)

try:
    # All stock item
    api_response = api_instance.find_stock_items(tags=tags, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockItemApi->find_stock_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tags** | [**list[str]**](str.md)| tags to filter by | [optional] 
 **limit** | **int**| Maximum number of results to return | [optional] 

### Return type

[**list[StockItem]**](StockItem.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

