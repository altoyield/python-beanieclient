# beanie.BeanieTaskApi

All URIs are relative to *https://bean.ie*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_beanie_task**](BeanieTaskApi.md#add_beanie_task) | **POST** /beanie_tasks | 
[**find_beanie_task_by_id**](BeanieTaskApi.md#find_beanie_task_by_id) | **GET** /beanie_tasks/{id} | Find Beanie task by ID
[**find_beanie_tasks**](BeanieTaskApi.md#find_beanie_tasks) | **GET** /beanie_tasks | All beanie task


# **add_beanie_task**
> BeanieTask add_beanie_task(beanie_tasks)



Creates a new beanie task in the system

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
api_instance = beanie.BeanieTaskApi(beanie.ApiClient(configuration))
beanie_tasks = beanie.BeanieTaskInput() # BeanieTaskInput | Beanie task to add to the system

try:
    api_response = api_instance.add_beanie_task(beanie_tasks)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BeanieTaskApi->add_beanie_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **beanie_tasks** | [**BeanieTaskInput**](BeanieTaskInput.md)| Beanie task to add to the system | 

### Return type

[**BeanieTask**](BeanieTask.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_beanie_task_by_id**
> BeanieTask find_beanie_task_by_id(id)

Find Beanie task by ID

Returns a single beanie task if the user has access

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
api_instance = beanie.BeanieTaskApi(beanie.ApiClient(configuration))
id = 789 # int | ID of beanie task to fetch

try:
    # Find Beanie task by ID
    api_response = api_instance.find_beanie_task_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BeanieTaskApi->find_beanie_task_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of beanie task to fetch | 

### Return type

[**BeanieTask**](BeanieTask.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_beanie_tasks**
> list[BeanieTask] find_beanie_tasks(tags=tags, limit=limit)

All beanie task

Returns all beanie task from the system that the user has access to

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
api_instance = beanie.BeanieTaskApi(beanie.ApiClient(configuration))
tags = ['tags_example'] # list[str] | tags to filter by (optional)
limit = 56 # int | Maximum number of results to return (optional)

try:
    # All beanie task
    api_response = api_instance.find_beanie_tasks(tags=tags, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BeanieTaskApi->find_beanie_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tags** | [**list[str]**](str.md)| tags to filter by | [optional] 
 **limit** | **int**| Maximum number of results to return | [optional] 

### Return type

[**list[BeanieTask]**](BeanieTask.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

