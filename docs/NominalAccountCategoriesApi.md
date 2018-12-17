# beanie.NominalAccountCategoriesApi

All URIs are relative to *https://bean.ie*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_nominal_account_category**](NominalAccountCategoriesApi.md#add_nominal_account_category) | **POST** /nominal_account_categories | 
[**find_nominal_account_category_by_id**](NominalAccountCategoriesApi.md#find_nominal_account_category_by_id) | **GET** /nominal_account_categories/{id} | Find Nominal account category by ID


# **add_nominal_account_category**
> NominalAccountCategory add_nominal_account_category(nominal_account_categories)



Creates a new nominal account category in the system

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
api_instance = beanie.NominalAccountCategoriesApi(beanie.ApiClient(configuration))
nominal_account_categories = beanie.NominalAccountCategoryInput() # NominalAccountCategoryInput | Nominal account category to add to the system

try:
    api_response = api_instance.add_nominal_account_category(nominal_account_categories)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NominalAccountCategoriesApi->add_nominal_account_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nominal_account_categories** | [**NominalAccountCategoryInput**](NominalAccountCategoryInput.md)| Nominal account category to add to the system | 

### Return type

[**NominalAccountCategory**](NominalAccountCategory.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_nominal_account_category_by_id**
> NominalAccountCategory find_nominal_account_category_by_id(id)

Find Nominal account category by ID

Returns a single nominal account category if the user has access

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
api_instance = beanie.NominalAccountCategoriesApi(beanie.ApiClient(configuration))
id = 789 # int | ID of nominal account category to fetch

try:
    # Find Nominal account category by ID
    api_response = api_instance.find_nominal_account_category_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NominalAccountCategoriesApi->find_nominal_account_category_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of nominal account category to fetch | 

### Return type

[**NominalAccountCategory**](NominalAccountCategory.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

