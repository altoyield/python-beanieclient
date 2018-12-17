# beanie.NominalAccountApi

All URIs are relative to *https://bean.ie*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_nominal_account**](NominalAccountApi.md#add_nominal_account) | **POST** /nominal_accounts | 
[**find_nominal_account_by_id**](NominalAccountApi.md#find_nominal_account_by_id) | **GET** /nominal_accounts/{id} | Find Nominal account by ID
[**find_nominal_accounts**](NominalAccountApi.md#find_nominal_accounts) | **GET** /nominal_accounts | All nominal account


# **add_nominal_account**
> NominalAccount add_nominal_account(nominal_accounts)



Creates a new nominal account in the system

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
api_instance = beanie.NominalAccountApi(beanie.ApiClient(configuration))
nominal_accounts = beanie.NominalAccountInput() # NominalAccountInput | Nominal account to add to the system

try:
    api_response = api_instance.add_nominal_account(nominal_accounts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NominalAccountApi->add_nominal_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nominal_accounts** | [**NominalAccountInput**](NominalAccountInput.md)| Nominal account to add to the system | 

### Return type

[**NominalAccount**](NominalAccount.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_nominal_account_by_id**
> NominalAccount find_nominal_account_by_id(id)

Find Nominal account by ID

Returns a single nominal account if the user has access

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
api_instance = beanie.NominalAccountApi(beanie.ApiClient(configuration))
id = 789 # int | ID of nominal account to fetch

try:
    # Find Nominal account by ID
    api_response = api_instance.find_nominal_account_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NominalAccountApi->find_nominal_account_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of nominal account to fetch | 

### Return type

[**NominalAccount**](NominalAccount.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_nominal_accounts**
> list[NominalAccount] find_nominal_accounts(tags=tags, limit=limit)

All nominal account

Returns all nominal account from the system that the user has access to

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
api_instance = beanie.NominalAccountApi(beanie.ApiClient(configuration))
tags = ['tags_example'] # list[str] | tags to filter by (optional)
limit = 56 # int | Maximum number of results to return (optional)

try:
    # All nominal account
    api_response = api_instance.find_nominal_accounts(tags=tags, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NominalAccountApi->find_nominal_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tags** | [**list[str]**](str.md)| tags to filter by | [optional] 
 **limit** | **int**| Maximum number of results to return | [optional] 

### Return type

[**list[NominalAccount]**](NominalAccount.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

