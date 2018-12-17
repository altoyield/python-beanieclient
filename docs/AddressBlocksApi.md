# beanie.AddressBlocksApi

All URIs are relative to *https://bean.ie*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_address_block**](AddressBlocksApi.md#add_address_block) | **POST** /address_blocks | 
[**find_address_block_by_id**](AddressBlocksApi.md#find_address_block_by_id) | **GET** /address_blocks/{id} | Find Address block by ID


# **add_address_block**
> AddressBlock add_address_block(address_blocks)



Creates a new address block in the system

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
api_instance = beanie.AddressBlocksApi(beanie.ApiClient(configuration))
address_blocks = beanie.AddressBlockInput() # AddressBlockInput | Address block to add to the system

try:
    api_response = api_instance.add_address_block(address_blocks)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressBlocksApi->add_address_block: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address_blocks** | [**AddressBlockInput**](AddressBlockInput.md)| Address block to add to the system | 

### Return type

[**AddressBlock**](AddressBlock.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_address_block_by_id**
> AddressBlock find_address_block_by_id(id)

Find Address block by ID

Returns a single address block if the user has access

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
api_instance = beanie.AddressBlocksApi(beanie.ApiClient(configuration))
id = 789 # int | ID of address block to fetch

try:
    # Find Address block by ID
    api_response = api_instance.find_address_block_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressBlocksApi->find_address_block_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of address block to fetch | 

### Return type

[**AddressBlock**](AddressBlock.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

