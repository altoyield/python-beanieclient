# beanie.PurchaseInvoicesApi

All URIs are relative to *https://bean.ie*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_purchase_invoice**](PurchaseInvoicesApi.md#add_purchase_invoice) | **POST** /purchase_invoices | 
[**find_purchase_invoice_by_id**](PurchaseInvoicesApi.md#find_purchase_invoice_by_id) | **GET** /purchase_invoices/{id} | Find Purchase invoice by ID


# **add_purchase_invoice**
> PurchaseInvoice add_purchase_invoice(purchase_invoices)



Creates a new purchase invoice in the system

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
api_instance = beanie.PurchaseInvoicesApi(beanie.ApiClient(configuration))
purchase_invoices = beanie.PurchaseInvoiceInput() # PurchaseInvoiceInput | Purchase invoice to add to the system

try:
    api_response = api_instance.add_purchase_invoice(purchase_invoices)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurchaseInvoicesApi->add_purchase_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purchase_invoices** | [**PurchaseInvoiceInput**](PurchaseInvoiceInput.md)| Purchase invoice to add to the system | 

### Return type

[**PurchaseInvoice**](PurchaseInvoice.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_purchase_invoice_by_id**
> PurchaseInvoice find_purchase_invoice_by_id(id)

Find Purchase invoice by ID

Returns a single purchase invoice if the user has access

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
api_instance = beanie.PurchaseInvoicesApi(beanie.ApiClient(configuration))
id = 789 # int | ID of purchase invoice to fetch

try:
    # Find Purchase invoice by ID
    api_response = api_instance.find_purchase_invoice_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurchaseInvoicesApi->find_purchase_invoice_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of purchase invoice to fetch | 

### Return type

[**PurchaseInvoice**](PurchaseInvoice.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

