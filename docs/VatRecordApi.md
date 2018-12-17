# beanie.VatRecordApi

All URIs are relative to *https://bean.ie*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_vat_record**](VatRecordApi.md#add_vat_record) | **POST** /vat_records | 
[**find_vat_record_by_id**](VatRecordApi.md#find_vat_record_by_id) | **GET** /vat_records/{id} | Find VAT record by ID
[**find_vat_records**](VatRecordApi.md#find_vat_records) | **GET** /vat_records | All vat record


# **add_vat_record**
> VatRecord add_vat_record(vat_records)



Creates a new vat record in the system

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
api_instance = beanie.VatRecordApi(beanie.ApiClient(configuration))
vat_records = beanie.VatRecordInput() # VatRecordInput | VAT record to add to the system

try:
    api_response = api_instance.add_vat_record(vat_records)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VatRecordApi->add_vat_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vat_records** | [**VatRecordInput**](VatRecordInput.md)| VAT record to add to the system | 

### Return type

[**VatRecord**](VatRecord.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_vat_record_by_id**
> VatRecord find_vat_record_by_id(id)

Find VAT record by ID

Returns a single vat record if the user has access

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
api_instance = beanie.VatRecordApi(beanie.ApiClient(configuration))
id = 789 # int | ID of vat record to fetch

try:
    # Find VAT record by ID
    api_response = api_instance.find_vat_record_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VatRecordApi->find_vat_record_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of vat record to fetch | 

### Return type

[**VatRecord**](VatRecord.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_vat_records**
> list[VatRecord] find_vat_records(tags=tags, limit=limit)

All vat record

Returns all vat record from the system that the user has access to

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
api_instance = beanie.VatRecordApi(beanie.ApiClient(configuration))
tags = ['tags_example'] # list[str] | tags to filter by (optional)
limit = 56 # int | Maximum number of results to return (optional)

try:
    # All vat record
    api_response = api_instance.find_vat_records(tags=tags, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VatRecordApi->find_vat_records: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tags** | [**list[str]**](str.md)| tags to filter by | [optional] 
 **limit** | **int**| Maximum number of results to return | [optional] 

### Return type

[**list[VatRecord]**](VatRecord.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

