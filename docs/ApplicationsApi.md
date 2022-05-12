# ddhub_gateway_client.ApplicationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**applications_controller_get_applications**](ApplicationsApi.md#applications_controller_get_applications) | **GET** /api/v2/applications | 


# **applications_controller_get_applications**
> [ApplicationDTO] applications_controller_get_applications(role_name)



Gets Applications

### Example


```python
import time
import ddhub_gateway_client
from ddhub_gateway_client.api import applications_api
from ddhub_gateway_client.model.application_dto import ApplicationDTO
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ddhub_gateway_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ddhub_gateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = applications_api.ApplicationsApi(api_client)
    role_name = "topiccreator" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.applications_controller_get_applications(role_name)
        pprint(api_response)
    except ddhub_gateway_client.ApiException as e:
        print("Exception when calling ApplicationsApi->applications_controller_get_applications: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**|  |

### Return type

[**[ApplicationDTO]**](ApplicationDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of applications |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

