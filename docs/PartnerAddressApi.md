# beanie.PartnerAddressApi

All URIs are relative to *https://bean.ie*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_partner_address**](PartnerAddressApi.md#add_partner_address) | **POST** /partner_addresses | 
[**find_partner_address_by_id**](PartnerAddressApi.md#find_partner_address_by_id) | **GET** /partner_addresses/{id} | Find Partner address by ID
[**find_partner_addresses**](PartnerAddressApi.md#find_partner_addresses) | **GET** /partner_addresses | All partner address


# **add_partner_address**
> PartnerAddress add_partner_address(partner_addresses)



Creates a new partner address in the system

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
api_instance = beanie.PartnerAddressApi(beanie.ApiClient(configuration))
partner_addresses = beanie.PartnerAddressInput() # PartnerAddressInput | Partner address to add to the system

try:
    api_response = api_instance.add_partner_address(partner_addresses)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartnerAddressApi->add_partner_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partner_addresses** | [**PartnerAddressInput**](PartnerAddressInput.md)| Partner address to add to the system | 

### Return type

[**PartnerAddress**](PartnerAddress.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_partner_address_by_id**
> PartnerAddress find_partner_address_by_id(id)

Find Partner address by ID

Returns a single partner address if the user has access

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
api_instance = beanie.PartnerAddressApi(beanie.ApiClient(configuration))
id = 789 # int | ID of partner address to fetch

try:
    # Find Partner address by ID
    api_response = api_instance.find_partner_address_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartnerAddressApi->find_partner_address_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of partner address to fetch | 

### Return type

[**PartnerAddress**](PartnerAddress.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_partner_addresses**
> list[PartnerAddress] find_partner_addresses(tags=tags, limit=limit)

All partner address

Returns all partner address from the system that the user has access to

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
api_instance = beanie.PartnerAddressApi(beanie.ApiClient(configuration))
tags = ['tags_example'] # list[str] | tags to filter by (optional)
limit = 56 # int | Maximum number of results to return (optional)

try:
    # All partner address
    api_response = api_instance.find_partner_addresses(tags=tags, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartnerAddressApi->find_partner_addresses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tags** | [**list[str]**](str.md)| tags to filter by | [optional] 
 **limit** | **int**| Maximum number of results to return | [optional] 

### Return type

[**list[PartnerAddress]**](PartnerAddress.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

