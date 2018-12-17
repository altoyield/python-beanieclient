# beanie.FixedAssetApi

All URIs are relative to *https://bean.ie*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_fixed_asset**](FixedAssetApi.md#add_fixed_asset) | **POST** /fixed_assets | 
[**find_fixed_asset_by_id**](FixedAssetApi.md#find_fixed_asset_by_id) | **GET** /fixed_assets/{id} | Find Fixed asset by ID
[**find_fixed_assets**](FixedAssetApi.md#find_fixed_assets) | **GET** /fixed_assets | All fixed asset


# **add_fixed_asset**
> FixedAsset add_fixed_asset(fixed_assets)



Creates a new fixed asset in the system

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
api_instance = beanie.FixedAssetApi(beanie.ApiClient(configuration))
fixed_assets = beanie.FixedAssetInput() # FixedAssetInput | Fixed asset to add to the system

try:
    api_response = api_instance.add_fixed_asset(fixed_assets)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FixedAssetApi->add_fixed_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fixed_assets** | [**FixedAssetInput**](FixedAssetInput.md)| Fixed asset to add to the system | 

### Return type

[**FixedAsset**](FixedAsset.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_fixed_asset_by_id**
> FixedAsset find_fixed_asset_by_id(id)

Find Fixed asset by ID

Returns a single fixed asset if the user has access

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
api_instance = beanie.FixedAssetApi(beanie.ApiClient(configuration))
id = 789 # int | ID of fixed asset to fetch

try:
    # Find Fixed asset by ID
    api_response = api_instance.find_fixed_asset_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FixedAssetApi->find_fixed_asset_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of fixed asset to fetch | 

### Return type

[**FixedAsset**](FixedAsset.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_fixed_assets**
> list[FixedAsset] find_fixed_assets(tags=tags, limit=limit)

All fixed asset

Returns all fixed asset from the system that the user has access to

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
api_instance = beanie.FixedAssetApi(beanie.ApiClient(configuration))
tags = ['tags_example'] # list[str] | tags to filter by (optional)
limit = 56 # int | Maximum number of results to return (optional)

try:
    # All fixed asset
    api_response = api_instance.find_fixed_assets(tags=tags, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FixedAssetApi->find_fixed_assets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tags** | [**list[str]**](str.md)| tags to filter by | [optional] 
 **limit** | **int**| Maximum number of results to return | [optional] 

### Return type

[**list[FixedAsset]**](FixedAsset.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

