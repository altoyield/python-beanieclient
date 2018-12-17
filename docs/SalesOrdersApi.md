# beanie.SalesOrdersApi

All URIs are relative to *https://bean.ie*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_sales_order**](SalesOrdersApi.md#add_sales_order) | **POST** /sales_orders | 
[**find_sales_order_by_id**](SalesOrdersApi.md#find_sales_order_by_id) | **GET** /sales_orders/{id} | Find Sales order by ID


# **add_sales_order**
> SalesOrder add_sales_order(sales_orders)



Creates a new sales order in the system

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
api_instance = beanie.SalesOrdersApi(beanie.ApiClient(configuration))
sales_orders = beanie.SalesOrderInput() # SalesOrderInput | Sales order to add to the system

try:
    api_response = api_instance.add_sales_order(sales_orders)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesOrdersApi->add_sales_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sales_orders** | [**SalesOrderInput**](SalesOrderInput.md)| Sales order to add to the system | 

### Return type

[**SalesOrder**](SalesOrder.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_sales_order_by_id**
> SalesOrder find_sales_order_by_id(id)

Find Sales order by ID

Returns a single sales order if the user has access

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
api_instance = beanie.SalesOrdersApi(beanie.ApiClient(configuration))
id = 789 # int | ID of sales order to fetch

try:
    # Find Sales order by ID
    api_response = api_instance.find_sales_order_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesOrdersApi->find_sales_order_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of sales order to fetch | 

### Return type

[**SalesOrder**](SalesOrder.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

