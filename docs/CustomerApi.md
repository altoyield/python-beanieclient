# beanie.CustomerApi

All URIs are relative to *https://bean.ie*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_customer**](CustomerApi.md#add_customer) | **POST** /customers | 
[**find_customer_by_id**](CustomerApi.md#find_customer_by_id) | **GET** /customers/{id} | Find Customer by ID
[**find_customers**](CustomerApi.md#find_customers) | **GET** /customers | All customer


# **add_customer**
> Customer add_customer(customers)



Creates a new customer in the system

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
api_instance = beanie.CustomerApi(beanie.ApiClient(configuration))
customers = beanie.CustomerInput() # CustomerInput | Customer to add to the system

try:
    api_response = api_instance.add_customer(customers)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->add_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customers** | [**CustomerInput**](CustomerInput.md)| Customer to add to the system | 

### Return type

[**Customer**](Customer.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_customer_by_id**
> Customer find_customer_by_id(id)

Find Customer by ID

Returns a single customer if the user has access

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
api_instance = beanie.CustomerApi(beanie.ApiClient(configuration))
id = 789 # int | ID of customer to fetch

try:
    # Find Customer by ID
    api_response = api_instance.find_customer_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->find_customer_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of customer to fetch | 

### Return type

[**Customer**](Customer.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_customers**
> list[Customer] find_customers(tags=tags, limit=limit)

All customer

Returns all customer from the system that the user has access to

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
api_instance = beanie.CustomerApi(beanie.ApiClient(configuration))
tags = ['tags_example'] # list[str] | tags to filter by (optional)
limit = 56 # int | Maximum number of results to return (optional)

try:
    # All customer
    api_response = api_instance.find_customers(tags=tags, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->find_customers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tags** | [**list[str]**](str.md)| tags to filter by | [optional] 
 **limit** | **int**| Maximum number of results to return | [optional] 

### Return type

[**list[Customer]**](Customer.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

