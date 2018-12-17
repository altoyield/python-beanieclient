# beanie.WorkCentreGroupsApi

All URIs are relative to *https://bean.ie*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_work_centre_group**](WorkCentreGroupsApi.md#add_work_centre_group) | **POST** /work_centre_groups | 
[**find_work_centre_group_by_id**](WorkCentreGroupsApi.md#find_work_centre_group_by_id) | **GET** /work_centre_groups/{id} | Find Work centre group by ID


# **add_work_centre_group**
> WorkCentreGroup add_work_centre_group(work_centre_groups)



Creates a new work centre group in the system

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
api_instance = beanie.WorkCentreGroupsApi(beanie.ApiClient(configuration))
work_centre_groups = beanie.WorkCentreGroupInput() # WorkCentreGroupInput | Work centre group to add to the system

try:
    api_response = api_instance.add_work_centre_group(work_centre_groups)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkCentreGroupsApi->add_work_centre_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_centre_groups** | [**WorkCentreGroupInput**](WorkCentreGroupInput.md)| Work centre group to add to the system | 

### Return type

[**WorkCentreGroup**](WorkCentreGroup.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_work_centre_group_by_id**
> WorkCentreGroup find_work_centre_group_by_id(id)

Find Work centre group by ID

Returns a single work centre group if the user has access

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
api_instance = beanie.WorkCentreGroupsApi(beanie.ApiClient(configuration))
id = 789 # int | ID of work centre group to fetch

try:
    # Find Work centre group by ID
    api_response = api_instance.find_work_centre_group_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkCentreGroupsApi->find_work_centre_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of work centre group to fetch | 

### Return type

[**WorkCentreGroup**](WorkCentreGroup.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

