# beanie.ProductCategoriesApi

All URIs are relative to *https://bean.ie*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_product_category**](ProductCategoriesApi.md#add_product_category) | **POST** /product_categories | 
[**find_product_category_by_id**](ProductCategoriesApi.md#find_product_category_by_id) | **GET** /product_categories/{id} | Find Product category by ID


# **add_product_category**
> ProductCategory add_product_category(product_categories)



Creates a new product category in the system

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
api_instance = beanie.ProductCategoriesApi(beanie.ApiClient(configuration))
product_categories = beanie.ProductCategoryInput() # ProductCategoryInput | Product category to add to the system

try:
    api_response = api_instance.add_product_category(product_categories)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductCategoriesApi->add_product_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_categories** | [**ProductCategoryInput**](ProductCategoryInput.md)| Product category to add to the system | 

### Return type

[**ProductCategory**](ProductCategory.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_product_category_by_id**
> ProductCategory find_product_category_by_id(id)

Find Product category by ID

Returns a single product category if the user has access

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
api_instance = beanie.ProductCategoriesApi(beanie.ApiClient(configuration))
id = 789 # int | ID of product category to fetch

try:
    # Find Product category by ID
    api_response = api_instance.find_product_category_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductCategoriesApi->find_product_category_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of product category to fetch | 

### Return type

[**ProductCategory**](ProductCategory.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

