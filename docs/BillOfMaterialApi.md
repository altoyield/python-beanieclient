# beanie.BillOfMaterialApi

All URIs are relative to *https://bean.ie*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_bill_of_materials**](BillOfMaterialApi.md#find_bill_of_materials) | **GET** /bill_of_materials | All bill of materials


# **find_bill_of_materials**
> list[BillOfMaterial] find_bill_of_materials(tags=tags, limit=limit)

All bill of materials

Returns all bill of materials from the system that the user has access to

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
api_instance = beanie.BillOfMaterialApi(beanie.ApiClient(configuration))
tags = ['tags_example'] # list[str] | tags to filter by (optional)
limit = 56 # int | Maximum number of results to return (optional)

try:
    # All bill of materials
    api_response = api_instance.find_bill_of_materials(tags=tags, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillOfMaterialApi->find_bill_of_materials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tags** | [**list[str]**](str.md)| tags to filter by | [optional] 
 **limit** | **int**| Maximum number of results to return | [optional] 

### Return type

[**list[BillOfMaterial]**](BillOfMaterial.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

