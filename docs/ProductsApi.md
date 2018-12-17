# beanie.ProductsApi

All URIs are relative to *https://bean.ie*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_product**](ProductsApi.md#add_product) | **POST** /products | 
[**find_product_by_id**](ProductsApi.md#find_product_by_id) | **GET** /products/{id} | Find Product by ID


# **add_product**
> Product add_product(products)



Creates a new product in the system

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
api_instance = beanie.ProductsApi(beanie.ApiClient(configuration))
products = beanie.ProductInput() # ProductInput | Product to add to the system

try:
    api_response = api_instance.add_product(products)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->add_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **products** | [**ProductInput**](ProductInput.md)| Product to add to the system | 

### Return type

[**Product**](Product.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_product_by_id**
> Product find_product_by_id(id)

Find Product by ID

Returns a single product if the user has access

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
api_instance = beanie.ProductsApi(beanie.ApiClient(configuration))
id = 789 # int | ID of product to fetch

try:
    # Find Product by ID
    api_response = api_instance.find_product_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->find_product_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of product to fetch | 

### Return type

[**Product**](Product.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

