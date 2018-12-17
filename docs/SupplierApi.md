# beanie.SupplierApi

All URIs are relative to *https://bean.ie*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_supplier**](SupplierApi.md#add_supplier) | **POST** /suppliers | 
[**find_supplier_by_id**](SupplierApi.md#find_supplier_by_id) | **GET** /suppliers/{id} | Find Supplier by ID
[**find_suppliers**](SupplierApi.md#find_suppliers) | **GET** /suppliers | All supplier


# **add_supplier**
> Supplier add_supplier(suppliers)



Creates a new supplier in the system

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
api_instance = beanie.SupplierApi(beanie.ApiClient(configuration))
suppliers = beanie.SupplierInput() # SupplierInput | Supplier to add to the system

try:
    api_response = api_instance.add_supplier(suppliers)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierApi->add_supplier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **suppliers** | [**SupplierInput**](SupplierInput.md)| Supplier to add to the system | 

### Return type

[**Supplier**](Supplier.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_supplier_by_id**
> Supplier find_supplier_by_id(id)

Find Supplier by ID

Returns a single supplier if the user has access

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
api_instance = beanie.SupplierApi(beanie.ApiClient(configuration))
id = 789 # int | ID of supplier to fetch

try:
    # Find Supplier by ID
    api_response = api_instance.find_supplier_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierApi->find_supplier_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of supplier to fetch | 

### Return type

[**Supplier**](Supplier.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_suppliers**
> list[Supplier] find_suppliers(tags=tags, limit=limit)

All supplier

Returns all supplier from the system that the user has access to

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
api_instance = beanie.SupplierApi(beanie.ApiClient(configuration))
tags = ['tags_example'] # list[str] | tags to filter by (optional)
limit = 56 # int | Maximum number of results to return (optional)

try:
    # All supplier
    api_response = api_instance.find_suppliers(tags=tags, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierApi->find_suppliers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tags** | [**list[str]**](str.md)| tags to filter by | [optional] 
 **limit** | **int**| Maximum number of results to return | [optional] 

### Return type

[**list[Supplier]**](Supplier.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

