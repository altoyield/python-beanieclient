# beanie.BillablesApi

All URIs are relative to *https://bean.ie*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_billable**](BillablesApi.md#add_billable) | **POST** /billables | 
[**find_billable_by_id**](BillablesApi.md#find_billable_by_id) | **GET** /billables/{id} | Find Billable record by ID


# **add_billable**
> Billable add_billable(billables)



Creates a new billable record in the system

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
api_instance = beanie.BillablesApi(beanie.ApiClient(configuration))
billables = beanie.BillableInput() # BillableInput | Billable record to add to the system

try:
    api_response = api_instance.add_billable(billables)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillablesApi->add_billable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billables** | [**BillableInput**](BillableInput.md)| Billable record to add to the system | 

### Return type

[**Billable**](Billable.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_billable_by_id**
> Billable find_billable_by_id(id)

Find Billable record by ID

Returns a single billable record if the user has access

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
api_instance = beanie.BillablesApi(beanie.ApiClient(configuration))
id = 789 # int | ID of billable record to fetch

try:
    # Find Billable record by ID
    api_response = api_instance.find_billable_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillablesApi->find_billable_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of billable record to fetch | 

### Return type

[**Billable**](Billable.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

