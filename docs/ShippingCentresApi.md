# beanie.ShippingCentresApi

All URIs are relative to *https://bean.ie*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_shipping_centre**](ShippingCentresApi.md#add_shipping_centre) | **POST** /shipping_centres | 
[**find_shipping_centre_by_id**](ShippingCentresApi.md#find_shipping_centre_by_id) | **GET** /shipping_centres/{id} | Find Shipping centre by ID


# **add_shipping_centre**
> ShippingCentre add_shipping_centre(shipping_centres)



Creates a new shipping centre in the system

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
api_instance = beanie.ShippingCentresApi(beanie.ApiClient(configuration))
shipping_centres = beanie.ShippingCentreInput() # ShippingCentreInput | Shipping centre to add to the system

try:
    api_response = api_instance.add_shipping_centre(shipping_centres)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShippingCentresApi->add_shipping_centre: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_centres** | [**ShippingCentreInput**](ShippingCentreInput.md)| Shipping centre to add to the system | 

### Return type

[**ShippingCentre**](ShippingCentre.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_shipping_centre_by_id**
> ShippingCentre find_shipping_centre_by_id(id)

Find Shipping centre by ID

Returns a single shipping centre if the user has access

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
api_instance = beanie.ShippingCentresApi(beanie.ApiClient(configuration))
id = 789 # int | ID of shipping centre to fetch

try:
    # Find Shipping centre by ID
    api_response = api_instance.find_shipping_centre_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShippingCentresApi->find_shipping_centre_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of shipping centre to fetch | 

### Return type

[**ShippingCentre**](ShippingCentre.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

