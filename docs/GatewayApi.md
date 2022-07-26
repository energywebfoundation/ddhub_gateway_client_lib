# ddhub_gateway_client.GatewayApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gateway_controller_get**](GatewayApi.md#gateway_controller_get) | **GET** /api/v2/gateway | 


# **gateway_controller_get**
> GatewayResponseDto gateway_controller_get()



### Example


```python
import time
import ddhub_gateway_client
from ddhub_gateway_client.api import gateway_api
from ddhub_gateway_client.model.gateway_response_dto import GatewayResponseDto
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ddhub_gateway_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ddhub_gateway_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = gateway_api.GatewayApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.gateway_controller_get()
        pprint(api_response)
    except ddhub_gateway_client.ApiException as e:
        print("Exception when calling GatewayApi->gateway_controller_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GatewayResponseDto**](GatewayResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gateway data |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

