# beanie.ProductPriceApi

All URIs are relative to *https://bean.ie*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_product_price**](ProductPriceApi.md#add_product_price) | **POST** /product_prices | 
[**find_product_price_by_id**](ProductPriceApi.md#find_product_price_by_id) | **GET** /product_prices/{id} | Find Product price by ID
[**find_product_prices**](ProductPriceApi.md#find_product_prices) | **GET** /product_prices | All product price


# **add_product_price**
> ProductPrice add_product_price(product_prices)



Creates a new product price in the system

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
api_instance = beanie.ProductPriceApi(beanie.ApiClient(configuration))
product_prices = beanie.ProductPriceInput() # ProductPriceInput | Product price to add to the system

try:
    api_response = api_instance.add_product_price(product_prices)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductPriceApi->add_product_price: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_prices** | [**ProductPriceInput**](ProductPriceInput.md)| Product price to add to the system | 

### Return type

[**ProductPrice**](ProductPrice.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_product_price_by_id**
> ProductPrice find_product_price_by_id(id)

Find Product price by ID

Returns a single product price if the user has access

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
api_instance = beanie.ProductPriceApi(beanie.ApiClient(configuration))
id = 789 # int | ID of product price to fetch

try:
    # Find Product price by ID
    api_response = api_instance.find_product_price_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductPriceApi->find_product_price_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of product price to fetch | 

### Return type

[**ProductPrice**](ProductPrice.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_product_prices**
> list[ProductPrice] find_product_prices(tags=tags, limit=limit)

All product price

Returns all product price from the system that the user has access to

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
api_instance = beanie.ProductPriceApi(beanie.ApiClient(configuration))
tags = ['tags_example'] # list[str] | tags to filter by (optional)
limit = 56 # int | Maximum number of results to return (optional)

try:
    # All product price
    api_response = api_instance.find_product_prices(tags=tags, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductPriceApi->find_product_prices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tags** | [**list[str]**](str.md)| tags to filter by | [optional] 
 **limit** | **int**| Maximum number of results to return | [optional] 

### Return type

[**list[ProductPrice]**](ProductPrice.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

