# beanie.BankStatementApi

All URIs are relative to *https://bean.ie*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_bank_statement**](BankStatementApi.md#add_bank_statement) | **POST** /bank_statements | 
[**find_bank_statement_by_id**](BankStatementApi.md#find_bank_statement_by_id) | **GET** /bank_statements/{id} | Find Bank statement by ID
[**find_bank_statements**](BankStatementApi.md#find_bank_statements) | **GET** /bank_statements | All bank statement


# **add_bank_statement**
> BankStatement add_bank_statement(bank_statements)



Creates a new bank statement in the system

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
api_instance = beanie.BankStatementApi(beanie.ApiClient(configuration))
bank_statements = beanie.BankStatementInput() # BankStatementInput | Bank statement to add to the system

try:
    api_response = api_instance.add_bank_statement(bank_statements)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankStatementApi->add_bank_statement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_statements** | [**BankStatementInput**](BankStatementInput.md)| Bank statement to add to the system | 

### Return type

[**BankStatement**](BankStatement.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_bank_statement_by_id**
> BankStatement find_bank_statement_by_id(id)

Find Bank statement by ID

Returns a single bank statement if the user has access

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
api_instance = beanie.BankStatementApi(beanie.ApiClient(configuration))
id = 789 # int | ID of bank statement to fetch

try:
    # Find Bank statement by ID
    api_response = api_instance.find_bank_statement_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankStatementApi->find_bank_statement_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of bank statement to fetch | 

### Return type

[**BankStatement**](BankStatement.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_bank_statements**
> list[BankStatement] find_bank_statements(tags=tags, limit=limit)

All bank statement

Returns all bank statement from the system that the user has access to

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
api_instance = beanie.BankStatementApi(beanie.ApiClient(configuration))
tags = ['tags_example'] # list[str] | tags to filter by (optional)
limit = 56 # int | Maximum number of results to return (optional)

try:
    # All bank statement
    api_response = api_instance.find_bank_statements(tags=tags, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankStatementApi->find_bank_statements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tags** | [**list[str]**](str.md)| tags to filter by | [optional] 
 **limit** | **int**| Maximum number of results to return | [optional] 

### Return type

[**list[BankStatement]**](BankStatement.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

