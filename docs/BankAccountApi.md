# beanie.BankAccountApi

All URIs are relative to *https://bean.ie*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_bank_account**](BankAccountApi.md#add_bank_account) | **POST** /bank_accounts | 
[**find_bank_account_by_id**](BankAccountApi.md#find_bank_account_by_id) | **GET** /bank_accounts/{id} | Find Bank Account by ID
[**find_bank_accounts**](BankAccountApi.md#find_bank_accounts) | **GET** /bank_accounts | All bank accounts


# **add_bank_account**
> BankAccount add_bank_account(bank_account)



Creates a new bank account in the system

### Example
```python
from __future__ import print_function
import time
import beanie
from beanie.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = beanie.BankAccountApi()
bank_account = beanie.BankAccountInput() # BankAccountInput | Bank account to add to the system

try:
    api_response = api_instance.add_bank_account(bank_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankAccountApi->add_bank_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account** | [**BankAccountInput**](BankAccountInput.md)| Bank account to add to the system | 

### Return type

[**BankAccount**](BankAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_bank_account_by_id**
> BankAccount find_bank_account_by_id(id)

Find Bank Account by ID

Returns a single bank account if the user has access

### Example
```python
from __future__ import print_function
import time
import beanie
from beanie.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = beanie.BankAccountApi()
id = 789 # int | ID of bank account to fetch

try:
    # Find Bank Account by ID
    api_response = api_instance.find_bank_account_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankAccountApi->find_bank_account_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of bank account to fetch | 

### Return type

[**BankAccount**](BankAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_bank_accounts**
> list[BankAccount] find_bank_accounts(tags=tags, limit=limit)

All bank accounts

Returns all bank accounts from the system that the user has access to

### Example
```python
from __future__ import print_function
import time
import beanie
from beanie.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = beanie.BankAccountApi()
tags = ['tags_example'] # list[str] | tags to filter by (optional)
limit = 56 # int | maximum number of results to return (optional)

try:
    # All bank accounts
    api_response = api_instance.find_bank_accounts(tags=tags, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankAccountApi->find_bank_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tags** | [**list[str]**](str.md)| tags to filter by | [optional] 
 **limit** | **int**| maximum number of results to return | [optional] 

### Return type

[**list[BankAccount]**](BankAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

