# beanie.CompanyApi

All URIs are relative to *https://bean.ie*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_company_by_id**](CompanyApi.md#find_company_by_id) | **GET** /companies/{id} | Find Company details by ID


# **find_company_by_id**
> Company find_company_by_id(id)

Find Company details by ID

Returns a single company details if the user has access

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
api_instance = beanie.CompanyApi(beanie.ApiClient(configuration))
id = 789 # int | ID of company details to fetch

try:
    # Find Company details by ID
    api_response = api_instance.find_company_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->find_company_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of company details to fetch | 

### Return type

[**Company**](Company.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

