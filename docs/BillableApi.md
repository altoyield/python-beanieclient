# beanie.BillableApi

All URIs are relative to *https://bean.ie*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_billable**](BillableApi.md#add_billable) | **POST** /billables | 
[**find_billable_by_id**](BillableApi.md#find_billable_by_id) | **GET** /billables/{id} | Find Billable record by ID
[**find_billables**](BillableApi.md#find_billables) | **GET** /billables | All billable record


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
api_instance = beanie.BillableApi(beanie.ApiClient(configuration))
billables = beanie.BillableInput() # BillableInput | Billable record to add to the system

try:
    api_response = api_instance.add_billable(billables)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillableApi->add_billable: %s\n" % e)
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
api_instance = beanie.BillableApi(beanie.ApiClient(configuration))
id = 789 # int | ID of billable record to fetch

try:
    # Find Billable record by ID
    api_response = api_instance.find_billable_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillableApi->find_billable_by_id: %s\n" % e)
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

# **find_billables**
> list[Billable] find_billables(tags=tags, limit=limit)

All billable record

Returns all billable record from the system that the user has access to

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
api_instance = beanie.BillableApi(beanie.ApiClient(configuration))
tags = ['tags_example'] # list[str] | tags to filter by (optional)
limit = 56 # int | Maximum number of results to return (optional)

try:
    # All billable record
    api_response = api_instance.find_billables(tags=tags, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillableApi->find_billables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tags** | [**list[str]**](str.md)| tags to filter by | [optional] 
 **limit** | **int**| Maximum number of results to return | [optional] 

### Return type

[**list[Billable]**](Billable.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

