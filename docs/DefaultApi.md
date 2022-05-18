# ddhub_gateway_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cron_controller_get_jobs_results**](DefaultApi.md#cron_controller_get_jobs_results) | **GET** /api/v2/cron | 


# **cron_controller_get_jobs_results**
> [CronResponseDto] cron_controller_get_jobs_results()



### Example


```python
import time
import ddhub_gateway_client
from ddhub_gateway_client.api import default_api
from ddhub_gateway_client.model.cron_response_dto import CronResponseDto
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ddhub_gateway_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ddhub_gateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.cron_controller_get_jobs_results()
        pprint(api_response)
    except ddhub_gateway_client.ApiException as e:
        print("Exception when calling DefaultApi->cron_controller_get_jobs_results: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[CronResponseDto]**](CronResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of CRON jobs results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

