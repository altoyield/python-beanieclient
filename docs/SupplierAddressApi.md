# beanie.SupplierAddressApi

All URIs are relative to *https://bean.ie*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_supplier_address**](SupplierAddressApi.md#add_supplier_address) | **POST** /supplier_addresses | 
[**find_supplier_address_by_id**](SupplierAddressApi.md#find_supplier_address_by_id) | **GET** /supplier_addresses/{id} | Find Supplier address by ID
[**find_supplier_addresses**](SupplierAddressApi.md#find_supplier_addresses) | **GET** /supplier_addresses | All supplier address


# **add_supplier_address**
> SupplierAddress add_supplier_address(supplier_addresses)



Creates a new supplier address in the system

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
api_instance = beanie.SupplierAddressApi(beanie.ApiClient(configuration))
supplier_addresses = beanie.SupplierAddressInput() # SupplierAddressInput | Supplier address to add to the system

try:
    api_response = api_instance.add_supplier_address(supplier_addresses)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierAddressApi->add_supplier_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_addresses** | [**SupplierAddressInput**](SupplierAddressInput.md)| Supplier address to add to the system | 

### Return type

[**SupplierAddress**](SupplierAddress.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_supplier_address_by_id**
> SupplierAddress find_supplier_address_by_id(id)

Find Supplier address by ID

Returns a single supplier address if the user has access

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
api_instance = beanie.SupplierAddressApi(beanie.ApiClient(configuration))
id = 789 # int | ID of supplier address to fetch

try:
    # Find Supplier address by ID
    api_response = api_instance.find_supplier_address_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierAddressApi->find_supplier_address_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of supplier address to fetch | 

### Return type

[**SupplierAddress**](SupplierAddress.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_supplier_addresses**
> list[SupplierAddress] find_supplier_addresses(tags=tags, limit=limit)

All supplier address

Returns all supplier address from the system that the user has access to

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
api_instance = beanie.SupplierAddressApi(beanie.ApiClient(configuration))
tags = ['tags_example'] # list[str] | tags to filter by (optional)
limit = 56 # int | Maximum number of results to return (optional)

try:
    # All supplier address
    api_response = api_instance.find_supplier_addresses(tags=tags, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierAddressApi->find_supplier_addresses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tags** | [**list[str]**](str.md)| tags to filter by | [optional] 
 **limit** | **int**| Maximum number of results to return | [optional] 

### Return type

[**list[SupplierAddress]**](SupplierAddress.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

