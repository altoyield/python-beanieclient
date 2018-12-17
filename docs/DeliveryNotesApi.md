# beanie.DeliveryNotesApi

All URIs are relative to *https://bean.ie*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_delivery_note**](DeliveryNotesApi.md#add_delivery_note) | **POST** /delivery_notes | 
[**find_delivery_note_by_id**](DeliveryNotesApi.md#find_delivery_note_by_id) | **GET** /delivery_notes/{id} | Find Delivery note by ID


# **add_delivery_note**
> DeliveryNote add_delivery_note(delivery_notes)



Creates a new delivery note in the system

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
api_instance = beanie.DeliveryNotesApi(beanie.ApiClient(configuration))
delivery_notes = beanie.DeliveryNoteInput() # DeliveryNoteInput | Delivery note to add to the system

try:
    api_response = api_instance.add_delivery_note(delivery_notes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeliveryNotesApi->add_delivery_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delivery_notes** | [**DeliveryNoteInput**](DeliveryNoteInput.md)| Delivery note to add to the system | 

### Return type

[**DeliveryNote**](DeliveryNote.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_delivery_note_by_id**
> DeliveryNote find_delivery_note_by_id(id)

Find Delivery note by ID

Returns a single delivery note if the user has access

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
api_instance = beanie.DeliveryNotesApi(beanie.ApiClient(configuration))
id = 789 # int | ID of delivery note to fetch

try:
    # Find Delivery note by ID
    api_response = api_instance.find_delivery_note_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeliveryNotesApi->find_delivery_note_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of delivery note to fetch | 

### Return type

[**DeliveryNote**](DeliveryNote.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

