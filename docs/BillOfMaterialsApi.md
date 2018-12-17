# beanie.BillOfMaterialsApi

All URIs are relative to *https://bean.ie*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_bill_of_material**](BillOfMaterialsApi.md#add_bill_of_material) | **POST** /bill_of_materials | 
[**find_bill_of_material_by_id**](BillOfMaterialsApi.md#find_bill_of_material_by_id) | **GET** /bill_of_materials/{id} | Find Bill of Materials by ID
[**find_bill_of_materials**](BillOfMaterialsApi.md#find_bill_of_materials) | **GET** /bill_of_materials | All bill of materials


# **add_bill_of_material**
> BillOfMaterial add_bill_of_material(bill_of_materials)



Creates a new bill of materials in the system

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
api_instance = beanie.BillOfMaterialsApi(beanie.ApiClient(configuration))
bill_of_materials = beanie.BillOfMaterialInput() # BillOfMaterialInput | Bill of Materials to add to the system

try:
    api_response = api_instance.add_bill_of_material(bill_of_materials)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillOfMaterialsApi->add_bill_of_material: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bill_of_materials** | [**BillOfMaterialInput**](BillOfMaterialInput.md)| Bill of Materials to add to the system | 

### Return type

[**BillOfMaterial**](BillOfMaterial.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_bill_of_material_by_id**
> BillOfMaterial find_bill_of_material_by_id(id)

Find Bill of Materials by ID

Returns a single bill of materials if the user has access

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
api_instance = beanie.BillOfMaterialsApi(beanie.ApiClient(configuration))
id = 789 # int | ID of bill of materials to fetch

try:
    # Find Bill of Materials by ID
    api_response = api_instance.find_bill_of_material_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillOfMaterialsApi->find_bill_of_material_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of bill of materials to fetch | 

### Return type

[**BillOfMaterial**](BillOfMaterial.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = beanie.BillOfMaterialsApi(beanie.ApiClient(configuration))
tags = ['tags_example'] # list[str] | tags to filter by (optional)
limit = 56 # int | Maximum number of results to return (optional)

try:
    # All bill of materials
    api_response = api_instance.find_bill_of_materials(tags=tags, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillOfMaterialsApi->find_bill_of_materials: %s\n" % e)
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

