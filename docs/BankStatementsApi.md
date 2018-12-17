# beanie.BankStatementsApi

All URIs are relative to *https://bean.ie*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_bank_statement**](BankStatementsApi.md#add_bank_statement) | **POST** /bank_statements | 
[**find_bank_statement_by_id**](BankStatementsApi.md#find_bank_statement_by_id) | **GET** /bank_statements/{id} | Find Bank statement by ID


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
api_instance = beanie.BankStatementsApi(beanie.ApiClient(configuration))
bank_statements = beanie.BankStatementInput() # BankStatementInput | Bank statement to add to the system

try:
    api_response = api_instance.add_bank_statement(bank_statements)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankStatementsApi->add_bank_statement: %s\n" % e)
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
api_instance = beanie.BankStatementsApi(beanie.ApiClient(configuration))
id = 789 # int | ID of bank statement to fetch

try:
    # Find Bank statement by ID
    api_response = api_instance.find_bank_statement_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankStatementsApi->find_bank_statement_by_id: %s\n" % e)
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

