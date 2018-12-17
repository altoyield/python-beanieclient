# beanie.ProductVariantsApi

All URIs are relative to *https://bean.ie*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_product_variant**](ProductVariantsApi.md#add_product_variant) | **POST** /product_variants | 
[**find_product_variant_by_id**](ProductVariantsApi.md#find_product_variant_by_id) | **GET** /product_variants/{id} | Find Product variant by ID


# **add_product_variant**
> ProductVariant add_product_variant(product_variants)



Creates a new product variant in the system

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
api_instance = beanie.ProductVariantsApi(beanie.ApiClient(configuration))
product_variants = beanie.ProductVariantInput() # ProductVariantInput | Product variant to add to the system

try:
    api_response = api_instance.add_product_variant(product_variants)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductVariantsApi->add_product_variant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_variants** | [**ProductVariantInput**](ProductVariantInput.md)| Product variant to add to the system | 

### Return type

[**ProductVariant**](ProductVariant.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_product_variant_by_id**
> ProductVariant find_product_variant_by_id(id)

Find Product variant by ID

Returns a single product variant if the user has access

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
api_instance = beanie.ProductVariantsApi(beanie.ApiClient(configuration))
id = 789 # int | ID of product variant to fetch

try:
    # Find Product variant by ID
    api_response = api_instance.find_product_variant_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductVariantsApi->find_product_variant_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of product variant to fetch | 

### Return type

[**ProductVariant**](ProductVariant.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

