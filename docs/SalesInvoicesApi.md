# beanie.SalesInvoicesApi

All URIs are relative to *https://bean.ie*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_sales_invoice**](SalesInvoicesApi.md#add_sales_invoice) | **POST** /sales_invoices | 
[**find_sales_invoice_by_id**](SalesInvoicesApi.md#find_sales_invoice_by_id) | **GET** /sales_invoices/{id} | Find Sales invoice by ID


# **add_sales_invoice**
> SalesInvoice add_sales_invoice(sales_invoices)



Creates a new sales invoice in the system

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
api_instance = beanie.SalesInvoicesApi(beanie.ApiClient(configuration))
sales_invoices = beanie.SalesInvoiceInput() # SalesInvoiceInput | Sales invoice to add to the system

try:
    api_response = api_instance.add_sales_invoice(sales_invoices)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesInvoicesApi->add_sales_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sales_invoices** | [**SalesInvoiceInput**](SalesInvoiceInput.md)| Sales invoice to add to the system | 

### Return type

[**SalesInvoice**](SalesInvoice.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_sales_invoice_by_id**
> SalesInvoice find_sales_invoice_by_id(id)

Find Sales invoice by ID

Returns a single sales invoice if the user has access

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
api_instance = beanie.SalesInvoicesApi(beanie.ApiClient(configuration))
id = 789 # int | ID of sales invoice to fetch

try:
    # Find Sales invoice by ID
    api_response = api_instance.find_sales_invoice_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesInvoicesApi->find_sales_invoice_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of sales invoice to fetch | 

### Return type

[**SalesInvoice**](SalesInvoice.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

