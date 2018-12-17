# beanie.ShippingCentreApi

All URIs are relative to *https://bean.ie*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_shipping_centre**](ShippingCentreApi.md#add_shipping_centre) | **POST** /shipping_centres | 
[**find_shipping_centre_by_id**](ShippingCentreApi.md#find_shipping_centre_by_id) | **GET** /shipping_centres/{id} | Find Shipping centre by ID
[**find_shipping_centres**](ShippingCentreApi.md#find_shipping_centres) | **GET** /shipping_centres | All shipping centre


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
api_instance = beanie.ShippingCentreApi(beanie.ApiClient(configuration))
shipping_centres = beanie.ShippingCentreInput() # ShippingCentreInput | Shipping centre to add to the system

try:
    api_response = api_instance.add_shipping_centre(shipping_centres)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShippingCentreApi->add_shipping_centre: %s\n" % e)
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
api_instance = beanie.ShippingCentreApi(beanie.ApiClient(configuration))
id = 789 # int | ID of shipping centre to fetch

try:
    # Find Shipping centre by ID
    api_response = api_instance.find_shipping_centre_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShippingCentreApi->find_shipping_centre_by_id: %s\n" % e)
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

# **find_shipping_centres**
> list[ShippingCentre] find_shipping_centres(tags=tags, limit=limit)

All shipping centre

Returns all shipping centre from the system that the user has access to

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
api_instance = beanie.ShippingCentreApi(beanie.ApiClient(configuration))
tags = ['tags_example'] # list[str] | tags to filter by (optional)
limit = 56 # int | Maximum number of results to return (optional)

try:
    # All shipping centre
    api_response = api_instance.find_shipping_centres(tags=tags, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShippingCentreApi->find_shipping_centres: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tags** | [**list[str]**](str.md)| tags to filter by | [optional] 
 **limit** | **int**| Maximum number of results to return | [optional] 

### Return type

[**list[ShippingCentre]**](ShippingCentre.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

