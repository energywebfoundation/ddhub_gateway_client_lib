# ddhub_gateway_client.IdentityApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**identity_controller_get**](IdentityApi.md#identity_controller_get) | **GET** /api/v2/identity | 
[**identity_controller_get_claims**](IdentityApi.md#identity_controller_get_claims) | **GET** /api/v2/identity/claims | 
[**identity_controller_post**](IdentityApi.md#identity_controller_post) | **POST** /api/v2/identity | 


# **identity_controller_get**
> IdentityResponseDto identity_controller_get()



### Example


```python
import time
import ddhub_gateway_client
from ddhub_gateway_client.api import identity_api
from ddhub_gateway_client.model.identity_response_dto import IdentityResponseDto
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ddhub_gateway_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ddhub_gateway_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = identity_api.IdentityApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.identity_controller_get()
        pprint(api_response)
    except ddhub_gateway_client.ApiException as e:
        print("Exception when calling IdentityApi->identity_controller_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**IdentityResponseDto**](IdentityResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Identity data |  -  |
**400** | Validation failed or some requirements were not fully satisfied |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **identity_controller_get_claims**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} identity_controller_get_claims()



### Example


```python
import time
import ddhub_gateway_client
from ddhub_gateway_client.api import identity_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ddhub_gateway_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ddhub_gateway_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = identity_api.IdentityApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.identity_controller_get_claims()
        pprint(api_response)
    except ddhub_gateway_client.ApiException as e:
        print("Exception when calling IdentityApi->identity_controller_get_claims: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Claims data |  -  |
**400** | Validation failed or some requirements were not fully satisfied |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **identity_controller_post**
> IdentityResponseDto identity_controller_post(create_identity_dto)



### Example


```python
import time
import ddhub_gateway_client
from ddhub_gateway_client.api import identity_api
from ddhub_gateway_client.model.create_identity_dto import CreateIdentityDto
from ddhub_gateway_client.model.identity_response_dto import IdentityResponseDto
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ddhub_gateway_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ddhub_gateway_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = identity_api.IdentityApi(api_client)
    create_identity_dto = CreateIdentityDto(
        private_key="private_key_example",
    ) # CreateIdentityDto | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.identity_controller_post(create_identity_dto)
        pprint(api_response)
    except ddhub_gateway_client.ApiException as e:
        print("Exception when calling IdentityApi->identity_controller_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_identity_dto** | [**CreateIdentityDto**](CreateIdentityDto.md)|  |

### Return type

[**IdentityResponseDto**](IdentityResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Identity successfully created |  -  |
**400** | Validation failed or some requirements were not fully satisfied |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

