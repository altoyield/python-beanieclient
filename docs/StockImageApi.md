# beanie.StockImageApi

All URIs are relative to *https://bean.ie*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_stock_image**](StockImageApi.md#add_stock_image) | **POST** /stock_images | 
[**find_stock_image_by_id**](StockImageApi.md#find_stock_image_by_id) | **GET** /stock_images/{id} | Find Stock image by ID
[**find_stock_images**](StockImageApi.md#find_stock_images) | **GET** /stock_images | All stock image


# **add_stock_image**
> StockImage add_stock_image(stock_images)



Creates a new stock image in the system

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
api_instance = beanie.StockImageApi(beanie.ApiClient(configuration))
stock_images = beanie.StockImageInput() # StockImageInput | Stock image to add to the system

try:
    api_response = api_instance.add_stock_image(stock_images)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockImageApi->add_stock_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_images** | [**StockImageInput**](StockImageInput.md)| Stock image to add to the system | 

### Return type

[**StockImage**](StockImage.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_stock_image_by_id**
> StockImage find_stock_image_by_id(id)

Find Stock image by ID

Returns a single stock image if the user has access

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
api_instance = beanie.StockImageApi(beanie.ApiClient(configuration))
id = 789 # int | ID of stock image to fetch

try:
    # Find Stock image by ID
    api_response = api_instance.find_stock_image_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockImageApi->find_stock_image_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of stock image to fetch | 

### Return type

[**StockImage**](StockImage.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_stock_images**
> list[StockImage] find_stock_images(tags=tags, limit=limit)

All stock image

Returns all stock image from the system that the user has access to

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
api_instance = beanie.StockImageApi(beanie.ApiClient(configuration))
tags = ['tags_example'] # list[str] | tags to filter by (optional)
limit = 56 # int | Maximum number of results to return (optional)

try:
    # All stock image
    api_response = api_instance.find_stock_images(tags=tags, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockImageApi->find_stock_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tags** | [**list[str]**](str.md)| tags to filter by | [optional] 
 **limit** | **int**| Maximum number of results to return | [optional] 

### Return type

[**list[StockImage]**](StockImage.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

