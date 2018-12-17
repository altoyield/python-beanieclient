# beanie.ProductionOrdersApi

All URIs are relative to *https://bean.ie*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_production_order**](ProductionOrdersApi.md#add_production_order) | **POST** /production_orders | 
[**find_production_order_by_id**](ProductionOrdersApi.md#find_production_order_by_id) | **GET** /production_orders/{id} | Find Production order by ID


# **add_production_order**
> ProductionOrder add_production_order(production_orders)



Creates a new production order in the system

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
api_instance = beanie.ProductionOrdersApi(beanie.ApiClient(configuration))
production_orders = beanie.ProductionOrderInput() # ProductionOrderInput | Production order to add to the system

try:
    api_response = api_instance.add_production_order(production_orders)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductionOrdersApi->add_production_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **production_orders** | [**ProductionOrderInput**](ProductionOrderInput.md)| Production order to add to the system | 

### Return type

[**ProductionOrder**](ProductionOrder.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_production_order_by_id**
> ProductionOrder find_production_order_by_id(id)

Find Production order by ID

Returns a single production order if the user has access

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
api_instance = beanie.ProductionOrdersApi(beanie.ApiClient(configuration))
id = 789 # int | ID of production order to fetch

try:
    # Find Production order by ID
    api_response = api_instance.find_production_order_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductionOrdersApi->find_production_order_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of production order to fetch | 

### Return type

[**ProductionOrder**](ProductionOrder.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

