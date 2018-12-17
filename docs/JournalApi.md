# beanie.JournalApi

All URIs are relative to *https://bean.ie*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_journal**](JournalApi.md#add_journal) | **POST** /journals | 
[**find_journal_by_id**](JournalApi.md#find_journal_by_id) | **GET** /journals/{id} | Find Journal by ID
[**find_journals**](JournalApi.md#find_journals) | **GET** /journals | All journal


# **add_journal**
> Journal add_journal(journals)



Creates a new journal in the system

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
api_instance = beanie.JournalApi(beanie.ApiClient(configuration))
journals = beanie.JournalInput() # JournalInput | Journal to add to the system

try:
    api_response = api_instance.add_journal(journals)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->add_journal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **journals** | [**JournalInput**](JournalInput.md)| Journal to add to the system | 

### Return type

[**Journal**](Journal.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_journal_by_id**
> Journal find_journal_by_id(id)

Find Journal by ID

Returns a single journal if the user has access

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
api_instance = beanie.JournalApi(beanie.ApiClient(configuration))
id = 789 # int | ID of journal to fetch

try:
    # Find Journal by ID
    api_response = api_instance.find_journal_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->find_journal_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of journal to fetch | 

### Return type

[**Journal**](Journal.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_journals**
> list[Journal] find_journals(tags=tags, limit=limit)

All journal

Returns all journal from the system that the user has access to

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
api_instance = beanie.JournalApi(beanie.ApiClient(configuration))
tags = ['tags_example'] # list[str] | tags to filter by (optional)
limit = 56 # int | Maximum number of results to return (optional)

try:
    # All journal
    api_response = api_instance.find_journals(tags=tags, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->find_journals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tags** | [**list[str]**](str.md)| tags to filter by | [optional] 
 **limit** | **int**| Maximum number of results to return | [optional] 

### Return type

[**list[Journal]**](Journal.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

