# beanie.DocumentsApi

All URIs are relative to *https://bean.ie*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_document**](DocumentsApi.md#add_document) | **POST** /documents | 
[**find_document_by_id**](DocumentsApi.md#find_document_by_id) | **GET** /documents/{id} | Find Document by ID


# **add_document**
> Document add_document(documents)



Creates a new document in the system

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
api_instance = beanie.DocumentsApi(beanie.ApiClient(configuration))
documents = beanie.DocumentInput() # DocumentInput | Document to add to the system

try:
    api_response = api_instance.add_document(documents)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->add_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documents** | [**DocumentInput**](DocumentInput.md)| Document to add to the system | 

### Return type

[**Document**](Document.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_document_by_id**
> Document find_document_by_id(id)

Find Document by ID

Returns a single document if the user has access

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
api_instance = beanie.DocumentsApi(beanie.ApiClient(configuration))
id = 789 # int | ID of document to fetch

try:
    # Find Document by ID
    api_response = api_instance.find_document_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->find_document_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of document to fetch | 

### Return type

[**Document**](Document.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

