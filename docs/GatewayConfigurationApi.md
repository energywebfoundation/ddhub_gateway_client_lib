# ddhub_gateway_client.GatewayConfigurationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**certificate_controller_save**](GatewayConfigurationApi.md#certificate_controller_save) | **POST** /api/v2/certificate | 
[**keys_controller_derive**](GatewayConfigurationApi.md#keys_controller_derive) | **POST** /api/v2/keys | 


# **certificate_controller_save**
> certificate_controller_save()



### Example


```python
import time
import ddhub_gateway_client
from ddhub_gateway_client.api import gateway_configuration_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ddhub_gateway_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ddhub_gateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gateway_configuration_api.GatewayConfigurationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.certificate_controller_save()
    except ddhub_gateway_client.ApiException as e:
        print("Exception when calling GatewayConfigurationApi->certificate_controller_save: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **keys_controller_derive**
> keys_controller_derive()



### Example


```python
import time
import ddhub_gateway_client
from ddhub_gateway_client.api import gateway_configuration_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ddhub_gateway_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ddhub_gateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gateway_configuration_api.GatewayConfigurationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.keys_controller_derive()
    except ddhub_gateway_client.ApiException as e:
        print("Exception when calling GatewayConfigurationApi->keys_controller_derive: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

