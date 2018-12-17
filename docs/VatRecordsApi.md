# beanie.VatRecordsApi

All URIs are relative to *https://bean.ie*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_vat_record**](VatRecordsApi.md#add_vat_record) | **POST** /vat_records | 
[**find_vat_record_by_id**](VatRecordsApi.md#find_vat_record_by_id) | **GET** /vat_records/{id} | Find VAT record by ID


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
api_instance = beanie.VatRecordsApi(beanie.ApiClient(configuration))
vat_records = beanie.VatRecordInput() # VatRecordInput | VAT record to add to the system

try:
    api_response = api_instance.add_vat_record(vat_records)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VatRecordsApi->add_vat_record: %s\n" % e)
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
api_instance = beanie.VatRecordsApi(beanie.ApiClient(configuration))
id = 789 # int | ID of vat record to fetch

try:
    # Find VAT record by ID
    api_response = api_instance.find_vat_record_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VatRecordsApi->find_vat_record_by_id: %s\n" % e)
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

