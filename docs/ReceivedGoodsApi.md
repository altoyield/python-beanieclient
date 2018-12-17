# beanie.ReceivedGoodsApi

All URIs are relative to *https://bean.ie*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_received_goods**](ReceivedGoodsApi.md#add_received_goods) | **POST** /received_goods | 
[**find_received_goods**](ReceivedGoodsApi.md#find_received_goods) | **GET** /received_goods | All received goods
[**find_received_goods_by_id**](ReceivedGoodsApi.md#find_received_goods_by_id) | **GET** /received_goods/{id} | Find Received goods by ID


# **add_received_goods**
> ReceivedGoods add_received_goods(received_goods)



Creates a new received goods in the system

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
api_instance = beanie.ReceivedGoodsApi(beanie.ApiClient(configuration))
received_goods = beanie.ReceivedGoodsInput() # ReceivedGoodsInput | Received goods to add to the system

try:
    api_response = api_instance.add_received_goods(received_goods)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceivedGoodsApi->add_received_goods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **received_goods** | [**ReceivedGoodsInput**](ReceivedGoodsInput.md)| Received goods to add to the system | 

### Return type

[**ReceivedGoods**](ReceivedGoods.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_received_goods**
> list[ReceivedGoods] find_received_goods(tags=tags, limit=limit)

All received goods

Returns all received goods from the system that the user has access to

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
api_instance = beanie.ReceivedGoodsApi(beanie.ApiClient(configuration))
tags = ['tags_example'] # list[str] | tags to filter by (optional)
limit = 56 # int | Maximum number of results to return (optional)

try:
    # All received goods
    api_response = api_instance.find_received_goods(tags=tags, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceivedGoodsApi->find_received_goods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tags** | [**list[str]**](str.md)| tags to filter by | [optional] 
 **limit** | **int**| Maximum number of results to return | [optional] 

### Return type

[**list[ReceivedGoods]**](ReceivedGoods.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_received_goods_by_id**
> ReceivedGoods find_received_goods_by_id(id)

Find Received goods by ID

Returns a single received goods if the user has access

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
api_instance = beanie.ReceivedGoodsApi(beanie.ApiClient(configuration))
id = 789 # int | ID of received goods to fetch

try:
    # Find Received goods by ID
    api_response = api_instance.find_received_goods_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceivedGoodsApi->find_received_goods_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of received goods to fetch | 

### Return type

[**ReceivedGoods**](ReceivedGoods.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

