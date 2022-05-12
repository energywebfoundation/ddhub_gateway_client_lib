# ddhub_gateway_client.ChannelsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**channel_controller_create**](ChannelsApi.md#channel_controller_create) | **POST** /api/v2/channels | 
[**channel_controller_delete**](ChannelsApi.md#channel_controller_delete) | **DELETE** /api/v2/channels/{fqcn} | 
[**channel_controller_get**](ChannelsApi.md#channel_controller_get) | **GET** /api/v2/channels/{fqcn} | 
[**channel_controller_get_by_type**](ChannelsApi.md#channel_controller_get_by_type) | **GET** /api/v2/channels | 
[**channel_controller_get_qualified_dids**](ChannelsApi.md#channel_controller_get_qualified_dids) | **GET** /api/v2/channels/{fqcn}/qualifiedDids | 
[**channel_controller_refresh_did**](ChannelsApi.md#channel_controller_refresh_did) | **POST** /api/v2/channels/refresh | 
[**channel_controller_update**](ChannelsApi.md#channel_controller_update) | **PUT** /api/v2/channels/{fqcn} | 


# **channel_controller_create**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} channel_controller_create(create_channel_dto)



### Example


```python
import time
import ddhub_gateway_client
from ddhub_gateway_client.api import channels_api
from ddhub_gateway_client.model.create_channel_dto import CreateChannelDto
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ddhub_gateway_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ddhub_gateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = channels_api.ChannelsApi(api_client)
    create_channel_dto = CreateChannelDto(
        fqcn="channel.name",
        type="sub",
        conditions=None,
    ) # CreateChannelDto | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.channel_controller_create(create_channel_dto)
        pprint(api_response)
    except ddhub_gateway_client.ApiException as e:
        print("Exception when calling ChannelsApi->channel_controller_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_channel_dto** | [**CreateChannelDto**](CreateChannelDto.md)|  |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Channel successfully created |  -  |
**400** | Validation failed or some requirements were not fully satisfied |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channel_controller_delete**
> channel_controller_delete(fqcn)



### Example


```python
import time
import ddhub_gateway_client
from ddhub_gateway_client.api import channels_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ddhub_gateway_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ddhub_gateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = channels_api.ChannelsApi(api_client)
    fqcn = "channel.name" # str | Channel type

    # example passing only required values which don't have defaults set
    try:
        api_instance.channel_controller_delete(fqcn)
    except ddhub_gateway_client.ApiException as e:
        print("Exception when calling ChannelsApi->channel_controller_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fqcn** | **str**| Channel type |

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
**204** | Channel deleted |  -  |
**401** | Unauthorized |  -  |
**404** | Channel not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channel_controller_get**
> GetChannelResponseDto channel_controller_get(fqcn)



### Example


```python
import time
import ddhub_gateway_client
from ddhub_gateway_client.api import channels_api
from ddhub_gateway_client.model.get_channel_response_dto import GetChannelResponseDto
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ddhub_gateway_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ddhub_gateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = channels_api.ChannelsApi(api_client)
    fqcn = "channel.name" # str | Channel type

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.channel_controller_get(fqcn)
        pprint(api_response)
    except ddhub_gateway_client.ApiException as e:
        print("Exception when calling ChannelsApi->channel_controller_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fqcn** | **str**| Channel type |

### Return type

[**GetChannelResponseDto**](GetChannelResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Channel details |  -  |
**401** | Unauthorized |  -  |
**404** | Channel not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channel_controller_get_by_type**
> [GetChannelResponseDto] channel_controller_get_by_type(type)



### Example


```python
import time
import ddhub_gateway_client
from ddhub_gateway_client.api import channels_api
from ddhub_gateway_client.model.get_channel_response_dto import GetChannelResponseDto
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ddhub_gateway_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ddhub_gateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = channels_api.ChannelsApi(api_client)
    type = "sub" # str | Channel type

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.channel_controller_get_by_type(type)
        pprint(api_response)
    except ddhub_gateway_client.ApiException as e:
        print("Exception when calling ChannelsApi->channel_controller_get_by_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Channel type |

### Return type

[**[GetChannelResponseDto]**](GetChannelResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gives channels based on type from query |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channel_controller_get_qualified_dids**
> GetChannelQualifiedDidsDto channel_controller_get_qualified_dids(fqcn)



### Example


```python
import time
import ddhub_gateway_client
from ddhub_gateway_client.api import channels_api
from ddhub_gateway_client.model.get_channel_qualified_dids_dto import GetChannelQualifiedDidsDto
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ddhub_gateway_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ddhub_gateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = channels_api.ChannelsApi(api_client)
    fqcn = "channel.name" # str | Channel type

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.channel_controller_get_qualified_dids(fqcn)
        pprint(api_response)
    except ddhub_gateway_client.ApiException as e:
        print("Exception when calling ChannelsApi->channel_controller_get_qualified_dids: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fqcn** | **str**| Channel type |

### Return type

[**GetChannelQualifiedDidsDto**](GetChannelQualifiedDidsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Channel qualified dids |  -  |
**401** | Unauthorized |  -  |
**404** | Channel not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channel_controller_refresh_did**
> channel_controller_refresh_did()



### Example


```python
import time
import ddhub_gateway_client
from ddhub_gateway_client.api import channels_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ddhub_gateway_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ddhub_gateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = channels_api.ChannelsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.channel_controller_refresh_did()
    except ddhub_gateway_client.ApiException as e:
        print("Exception when calling ChannelsApi->channel_controller_refresh_did: %s\n" % e)
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
**200** | Refreshed cache |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channel_controller_update**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} channel_controller_update(fqcn, update_channel_dto)



### Example


```python
import time
import ddhub_gateway_client
from ddhub_gateway_client.api import channels_api
from ddhub_gateway_client.model.update_channel_dto import UpdateChannelDto
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ddhub_gateway_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ddhub_gateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = channels_api.ChannelsApi(api_client)
    fqcn = "channel.name" # str | Channel type
    update_channel_dto = UpdateChannelDto(
        type="sub",
        conditions=None,
    ) # UpdateChannelDto | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.channel_controller_update(fqcn, update_channel_dto)
        pprint(api_response)
    except ddhub_gateway_client.ApiException as e:
        print("Exception when calling ChannelsApi->channel_controller_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fqcn** | **str**| Channel type |
 **update_channel_dto** | [**UpdateChannelDto**](UpdateChannelDto.md)|  |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Channel successfully updated |  -  |
**400** | Validation failed or some requirements were not fully satisfied |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

