# beanie.StockCategoryApi

All URIs are relative to *https://bean.ie*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_stock_category**](StockCategoryApi.md#add_stock_category) | **POST** /stock_categories | 
[**find_stock_categories**](StockCategoryApi.md#find_stock_categories) | **GET** /stock_categories | All stock category
[**find_stock_category_by_id**](StockCategoryApi.md#find_stock_category_by_id) | **GET** /stock_categories/{id} | Find Stock category by ID


# **add_stock_category**
> StockCategory add_stock_category(stock_categories)



Creates a new stock category in the system

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
api_instance = beanie.StockCategoryApi(beanie.ApiClient(configuration))
stock_categories = beanie.StockCategoryInput() # StockCategoryInput | Stock category to add to the system

try:
    api_response = api_instance.add_stock_category(stock_categories)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockCategoryApi->add_stock_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_categories** | [**StockCategoryInput**](StockCategoryInput.md)| Stock category to add to the system | 

### Return type

[**StockCategory**](StockCategory.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_stock_categories**
> list[StockCategory] find_stock_categories(tags=tags, limit=limit)

All stock category

Returns all stock category from the system that the user has access to

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
api_instance = beanie.StockCategoryApi(beanie.ApiClient(configuration))
tags = ['tags_example'] # list[str] | tags to filter by (optional)
limit = 56 # int | Maximum number of results to return (optional)

try:
    # All stock category
    api_response = api_instance.find_stock_categories(tags=tags, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockCategoryApi->find_stock_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tags** | [**list[str]**](str.md)| tags to filter by | [optional] 
 **limit** | **int**| Maximum number of results to return | [optional] 

### Return type

[**list[StockCategory]**](StockCategory.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_stock_category_by_id**
> StockCategory find_stock_category_by_id(id)

Find Stock category by ID

Returns a single stock category if the user has access

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
api_instance = beanie.StockCategoryApi(beanie.ApiClient(configuration))
id = 789 # int | ID of stock category to fetch

try:
    # Find Stock category by ID
    api_response = api_instance.find_stock_category_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockCategoryApi->find_stock_category_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of stock category to fetch | 

### Return type

[**StockCategory**](StockCategory.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

