# beanie.WorkCentresApi

All URIs are relative to *https://bean.ie*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_work_centre**](WorkCentresApi.md#add_work_centre) | **POST** /work_centres | 
[**find_work_centre_by_id**](WorkCentresApi.md#find_work_centre_by_id) | **GET** /work_centres/{id} | Find Work centre by ID


# **add_work_centre**
> WorkCentre add_work_centre(work_centres)



Creates a new work centre in the system

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
api_instance = beanie.WorkCentresApi(beanie.ApiClient(configuration))
work_centres = beanie.WorkCentreInput() # WorkCentreInput | Work centre to add to the system

try:
    api_response = api_instance.add_work_centre(work_centres)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkCentresApi->add_work_centre: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_centres** | [**WorkCentreInput**](WorkCentreInput.md)| Work centre to add to the system | 

### Return type

[**WorkCentre**](WorkCentre.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_work_centre_by_id**
> WorkCentre find_work_centre_by_id(id)

Find Work centre by ID

Returns a single work centre if the user has access

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
api_instance = beanie.WorkCentresApi(beanie.ApiClient(configuration))
id = 789 # int | ID of work centre to fetch

try:
    # Find Work centre by ID
    api_response = api_instance.find_work_centre_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkCentresApi->find_work_centre_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of work centre to fetch | 

### Return type

[**WorkCentre**](WorkCentre.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

