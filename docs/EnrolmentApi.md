# ddhub_gateway_client.EnrolmentApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enrolment_controller_get**](EnrolmentApi.md#enrolment_controller_get) | **GET** /api/v2/enrol | 
[**enrolment_controller_init**](EnrolmentApi.md#enrolment_controller_init) | **POST** /api/v2/enrol | 


# **enrolment_controller_get**
> enrolment_controller_get()



### Example


```python
import time
import ddhub_gateway_client
from ddhub_gateway_client.api import enrolment_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ddhub_gateway_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ddhub_gateway_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = enrolment_api.EnrolmentApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.enrolment_controller_get()
    except ddhub_gateway_client.ApiException as e:
        print("Exception when calling EnrolmentApi->enrolment_controller_get: %s\n" % e)
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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enrolment_controller_init**
> enrolment_controller_init()



### Example


```python
import time
import ddhub_gateway_client
from ddhub_gateway_client.api import enrolment_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ddhub_gateway_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ddhub_gateway_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = enrolment_api.EnrolmentApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.enrolment_controller_init()
    except ddhub_gateway_client.ApiException as e:
        print("Exception when calling EnrolmentApi->enrolment_controller_init: %s\n" % e)
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

