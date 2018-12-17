# beanie.VatReturnsApi

All URIs are relative to *https://bean.ie*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_vat_return**](VatReturnsApi.md#add_vat_return) | **POST** /vat_returns | 
[**find_vat_return_by_id**](VatReturnsApi.md#find_vat_return_by_id) | **GET** /vat_returns/{id} | Find VAT return by ID


# **add_vat_return**
> VatReturn add_vat_return(vat_returns)



Creates a new vat return in the system

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
api_instance = beanie.VatReturnsApi(beanie.ApiClient(configuration))
vat_returns = beanie.VatReturnInput() # VatReturnInput | VAT return to add to the system

try:
    api_response = api_instance.add_vat_return(vat_returns)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VatReturnsApi->add_vat_return: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vat_returns** | [**VatReturnInput**](VatReturnInput.md)| VAT return to add to the system | 

### Return type

[**VatReturn**](VatReturn.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_vat_return_by_id**
> VatReturn find_vat_return_by_id(id)

Find VAT return by ID

Returns a single vat return if the user has access

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
api_instance = beanie.VatReturnsApi(beanie.ApiClient(configuration))
id = 789 # int | ID of vat return to fetch

try:
    # Find VAT return by ID
    api_response = api_instance.find_vat_return_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VatReturnsApi->find_vat_return_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of vat return to fetch | 

### Return type

[**VatReturn**](VatReturn.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

