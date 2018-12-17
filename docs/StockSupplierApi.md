# beanie.StockSupplierApi

All URIs are relative to *https://bean.ie*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_stock_supplier**](StockSupplierApi.md#add_stock_supplier) | **POST** /stock_suppliers | 
[**find_stock_supplier_by_id**](StockSupplierApi.md#find_stock_supplier_by_id) | **GET** /stock_suppliers/{id} | Find Stock supplier by ID
[**find_stock_suppliers**](StockSupplierApi.md#find_stock_suppliers) | **GET** /stock_suppliers | All stock supplier


# **add_stock_supplier**
> StockSupplier add_stock_supplier(stock_suppliers)



Creates a new stock supplier in the system

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
api_instance = beanie.StockSupplierApi(beanie.ApiClient(configuration))
stock_suppliers = beanie.StockSupplierInput() # StockSupplierInput | Stock supplier to add to the system

try:
    api_response = api_instance.add_stock_supplier(stock_suppliers)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockSupplierApi->add_stock_supplier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_suppliers** | [**StockSupplierInput**](StockSupplierInput.md)| Stock supplier to add to the system | 

### Return type

[**StockSupplier**](StockSupplier.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_stock_supplier_by_id**
> StockSupplier find_stock_supplier_by_id(id)

Find Stock supplier by ID

Returns a single stock supplier if the user has access

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
api_instance = beanie.StockSupplierApi(beanie.ApiClient(configuration))
id = 789 # int | ID of stock supplier to fetch

try:
    # Find Stock supplier by ID
    api_response = api_instance.find_stock_supplier_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockSupplierApi->find_stock_supplier_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of stock supplier to fetch | 

### Return type

[**StockSupplier**](StockSupplier.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_stock_suppliers**
> list[StockSupplier] find_stock_suppliers(tags=tags, limit=limit)

All stock supplier

Returns all stock supplier from the system that the user has access to

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
api_instance = beanie.StockSupplierApi(beanie.ApiClient(configuration))
tags = ['tags_example'] # list[str] | tags to filter by (optional)
limit = 56 # int | Maximum number of results to return (optional)

try:
    # All stock supplier
    api_response = api_instance.find_stock_suppliers(tags=tags, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockSupplierApi->find_stock_suppliers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tags** | [**list[str]**](str.md)| tags to filter by | [optional] 
 **limit** | **int**| Maximum number of results to return | [optional] 

### Return type

[**list[StockSupplier]**](StockSupplier.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

