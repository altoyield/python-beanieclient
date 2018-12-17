# beanie.StockAdjustmentsApi

All URIs are relative to *https://bean.ie*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_stock_adjustment**](StockAdjustmentsApi.md#add_stock_adjustment) | **POST** /stock_adjustments | 
[**find_stock_adjustment_by_id**](StockAdjustmentsApi.md#find_stock_adjustment_by_id) | **GET** /stock_adjustments/{id} | Find Stock adjustment by ID


# **add_stock_adjustment**
> StockAdjustment add_stock_adjustment(stock_adjustments)



Creates a new stock adjustment in the system

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
api_instance = beanie.StockAdjustmentsApi(beanie.ApiClient(configuration))
stock_adjustments = beanie.StockAdjustmentInput() # StockAdjustmentInput | Stock adjustment to add to the system

try:
    api_response = api_instance.add_stock_adjustment(stock_adjustments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockAdjustmentsApi->add_stock_adjustment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_adjustments** | [**StockAdjustmentInput**](StockAdjustmentInput.md)| Stock adjustment to add to the system | 

### Return type

[**StockAdjustment**](StockAdjustment.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_stock_adjustment_by_id**
> StockAdjustment find_stock_adjustment_by_id(id)

Find Stock adjustment by ID

Returns a single stock adjustment if the user has access

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
api_instance = beanie.StockAdjustmentsApi(beanie.ApiClient(configuration))
id = 789 # int | ID of stock adjustment to fetch

try:
    # Find Stock adjustment by ID
    api_response = api_instance.find_stock_adjustment_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockAdjustmentsApi->find_stock_adjustment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of stock adjustment to fetch | 

### Return type

[**StockAdjustment**](StockAdjustment.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

