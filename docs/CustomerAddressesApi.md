# beanie.CustomerAddressesApi

All URIs are relative to *https://bean.ie*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_customer_address**](CustomerAddressesApi.md#add_customer_address) | **POST** /customer_addresses | 
[**find_customer_address_by_id**](CustomerAddressesApi.md#find_customer_address_by_id) | **GET** /customer_addresses/{id} | Find Customer address by ID


# **add_customer_address**
> CustomerAddress add_customer_address(customer_addresses)



Creates a new customer address in the system

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
api_instance = beanie.CustomerAddressesApi(beanie.ApiClient(configuration))
customer_addresses = beanie.CustomerAddressInput() # CustomerAddressInput | Customer address to add to the system

try:
    api_response = api_instance.add_customer_address(customer_addresses)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerAddressesApi->add_customer_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_addresses** | [**CustomerAddressInput**](CustomerAddressInput.md)| Customer address to add to the system | 

### Return type

[**CustomerAddress**](CustomerAddress.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_customer_address_by_id**
> CustomerAddress find_customer_address_by_id(id)

Find Customer address by ID

Returns a single customer address if the user has access

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
api_instance = beanie.CustomerAddressesApi(beanie.ApiClient(configuration))
id = 789 # int | ID of customer address to fetch

try:
    # Find Customer address by ID
    api_response = api_instance.find_customer_address_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerAddressesApi->find_customer_address_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of customer address to fetch | 

### Return type

[**CustomerAddress**](CustomerAddress.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

