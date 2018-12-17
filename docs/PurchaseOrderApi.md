# beanie.PurchaseOrderApi

All URIs are relative to *https://bean.ie*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_purchase_order**](PurchaseOrderApi.md#add_purchase_order) | **POST** /purchase_orders | 
[**find_purchase_order_by_id**](PurchaseOrderApi.md#find_purchase_order_by_id) | **GET** /purchase_orders/{id} | Find Purchase order by ID
[**find_purchase_orders**](PurchaseOrderApi.md#find_purchase_orders) | **GET** /purchase_orders | All purchase order


# **add_purchase_order**
> PurchaseOrder add_purchase_order(purchase_orders)



Creates a new purchase order in the system

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
api_instance = beanie.PurchaseOrderApi(beanie.ApiClient(configuration))
purchase_orders = beanie.PurchaseOrderInput() # PurchaseOrderInput | Purchase order to add to the system

try:
    api_response = api_instance.add_purchase_order(purchase_orders)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurchaseOrderApi->add_purchase_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purchase_orders** | [**PurchaseOrderInput**](PurchaseOrderInput.md)| Purchase order to add to the system | 

### Return type

[**PurchaseOrder**](PurchaseOrder.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_purchase_order_by_id**
> PurchaseOrder find_purchase_order_by_id(id)

Find Purchase order by ID

Returns a single purchase order if the user has access

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
api_instance = beanie.PurchaseOrderApi(beanie.ApiClient(configuration))
id = 789 # int | ID of purchase order to fetch

try:
    # Find Purchase order by ID
    api_response = api_instance.find_purchase_order_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurchaseOrderApi->find_purchase_order_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of purchase order to fetch | 

### Return type

[**PurchaseOrder**](PurchaseOrder.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_purchase_orders**
> list[PurchaseOrder] find_purchase_orders(tags=tags, limit=limit)

All purchase order

Returns all purchase order from the system that the user has access to

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
api_instance = beanie.PurchaseOrderApi(beanie.ApiClient(configuration))
tags = ['tags_example'] # list[str] | tags to filter by (optional)
limit = 56 # int | Maximum number of results to return (optional)

try:
    # All purchase order
    api_response = api_instance.find_purchase_orders(tags=tags, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurchaseOrderApi->find_purchase_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tags** | [**list[str]**](str.md)| tags to filter by | [optional] 
 **limit** | **int**| Maximum number of results to return | [optional] 

### Return type

[**list[PurchaseOrder]**](PurchaseOrder.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

