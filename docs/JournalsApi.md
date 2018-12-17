# beanie.JournalsApi

All URIs are relative to *https://bean.ie*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_journal**](JournalsApi.md#add_journal) | **POST** /journals | 
[**find_journal_by_id**](JournalsApi.md#find_journal_by_id) | **GET** /journals/{id} | Find Journal by ID


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
api_instance = beanie.JournalsApi(beanie.ApiClient(configuration))
journals = beanie.JournalInput() # JournalInput | Journal to add to the system

try:
    api_response = api_instance.add_journal(journals)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalsApi->add_journal: %s\n" % e)
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
api_instance = beanie.JournalsApi(beanie.ApiClient(configuration))
id = 789 # int | ID of journal to fetch

try:
    # Find Journal by ID
    api_response = api_instance.find_journal_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalsApi->find_journal_by_id: %s\n" % e)
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

