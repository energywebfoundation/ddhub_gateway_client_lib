# ddhub_gateway_client.MessagingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**message_controlller_create**](MessagingApi.md#message_controlller_create) | **POST** /api/v2/messages | 
[**message_controlller_download_message**](MessagingApi.md#message_controlller_download_message) | **GET** /api/v2/messages/download | 
[**message_controlller_get_message**](MessagingApi.md#message_controlller_get_message) | **GET** /api/v2/messages | 
[**message_controlller_upload_file**](MessagingApi.md#message_controlller_upload_file) | **POST** /api/v2/messages/upload | 


# **message_controlller_create**
> SendMessagelResponseDto message_controlller_create(send_message_dto)



### Example


```python
import time
import ddhub_gateway_client
from ddhub_gateway_client.api import messaging_api
from ddhub_gateway_client.model.send_message_dto import SendMessageDto
from ddhub_gateway_client.model.send_messagel_response_dto import SendMessagelResponseDto
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ddhub_gateway_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ddhub_gateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = messaging_api.MessagingApi(api_client)
    send_message_dto = SendMessageDto(
        fqcn="channel.name",
        topic_name="topic_name_example",
        topic_version="1.0.0",
        topic_owner="aemo.edge",
        transaction_id="transaction_id_example",
        payload="{ data: 49 }",
    ) # SendMessageDto | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.message_controlller_create(send_message_dto)
        pprint(api_response)
    except ddhub_gateway_client.ApiException as e:
        print("Exception when calling MessagingApi->message_controlller_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_message_dto** | [**SendMessageDto**](SendMessageDto.md)|  |

### Return type

[**SendMessagelResponseDto**](SendMessagelResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Message sent successfully |  -  |
**400** | Validation failed or some requirements were not fully satisfied |  -  |
**401** | Unauthorized |  -  |
**404** | Channel not found or Topic not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_controlller_download_message**
> file_type message_controlller_download_message(file_id)



### Example


```python
import time
import ddhub_gateway_client
from ddhub_gateway_client.api import messaging_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ddhub_gateway_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ddhub_gateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = messaging_api.MessagingApi(api_client)
    file_id = "bb2686d2-97be-436b-8869" # str | file Id for which file will be downloaded

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.message_controlller_download_message(file_id)
        with open(file_id+".csv", "wb") as file:
            file.write(api_response.read())
    except ddhub_gateway_client.ApiException as e:
        print("Exception when calling MessagingApi->message_controlller_download_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| file Id for which file will be downloaded |

### Return type

**file_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: multipart/form-data


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Message Dwonloaded successfully |  -  |
**400** | Validation failed or some requirements were not fully satisfied |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_controlller_get_message**
> [GetMessagesResponseDto] message_controlller_get_message(fqcn)



### Example


```python
import time
import ddhub_gateway_client
from ddhub_gateway_client.api import messaging_api
from ddhub_gateway_client.model.get_messages_response_dto import GetMessagesResponseDto
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ddhub_gateway_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ddhub_gateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = messaging_api.MessagingApi(api_client)
    fqcn = "channel.name" # str | channel name
    _from = "2022-03-31T09:48:44.357Z" # str | date from which messages to be fetched (optional)
    amount = 1 # float | Latest amount of messages to be fetched (optional)
    topic_name = "getOperatingEnvelope" # str | topic name (optional)
    topic_owner = "torta.apps.eggplant.vege.iam.ewc" # str | application namespace (optional)
    client_id = "test2" # str | cursor for pointing to messages (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.message_controlller_get_message(fqcn)
        pprint(api_response)
    except ddhub_gateway_client.ApiException as e:
        print("Exception when calling MessagingApi->message_controlller_get_message: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.message_controlller_get_message(fqcn, _from=_from, amount=amount, topic_name=topic_name, topic_owner=topic_owner, client_id=client_id)
        pprint(api_response)
    except ddhub_gateway_client.ApiException as e:
        print("Exception when calling MessagingApi->message_controlller_get_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fqcn** | **str**| channel name |
 **_from** | **str**| date from which messages to be fetched | [optional]
 **amount** | **float**| Latest amount of messages to be fetched | [optional]
 **topic_name** | **str**| topic name | [optional]
 **topic_owner** | **str**| application namespace | [optional]
 **client_id** | **str**| cursor for pointing to messages | [optional]

### Return type

[**[GetMessagesResponseDto]**](GetMessagesResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Message recieved successfully |  -  |
**400** | Validation failed or some requirements were not fully satisfied |  -  |
**401** | Unauthorized |  -  |
**404** | Messages Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_controlller_upload_file**
> SendMessagelResponseDto message_controlller_upload_file(file, fqcn, topic_name, topic_version, topic_owner)



### Example


```python
import time
import ddhub_gateway_client
from ddhub_gateway_client.api import messaging_api
from ddhub_gateway_client.model.send_messagel_response_dto import SendMessagelResponseDto
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ddhub_gateway_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ddhub_gateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = messaging_api.MessagingApi(api_client)
    file = open('/path/to/file', 'rb') # file_type | File uploaded
    fqcn = "channel.name" # str | Channel Name
    topic_name = "topic_name_example" # str | Topic name
    topic_version = "1.0.0" # str | Topic Version
    topic_owner = "aemo.edge" # str | Topic Owner
    transaction_id = "transaction_id_example" # str | Transaction Id used to check Idempotency (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.message_controlller_upload_file(file, fqcn, topic_name, topic_version, topic_owner)
        pprint(api_response)
    except ddhub_gateway_client.ApiException as e:
        print("Exception when calling MessagingApi->message_controlller_upload_file: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.message_controlller_upload_file(file, fqcn, topic_name, topic_version, topic_owner, transaction_id=transaction_id)
        pprint(api_response)
    except ddhub_gateway_client.ApiException as e:
        print("Exception when calling MessagingApi->message_controlller_upload_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file_type**| File uploaded |
 **fqcn** | **str**| Channel Name |
 **topic_name** | **str**| Topic name |
 **topic_version** | **str**| Topic Version |
 **topic_owner** | **str**| Topic Owner |
 **transaction_id** | **str**| Transaction Id used to check Idempotency | [optional]

### Return type

[**SendMessagelResponseDto**](SendMessagelResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | File Upload Successfully |  -  |
**400** | Validation failed or some requirements were not fully satisfied |  -  |
**401** | Unauthorized |  -  |
**404** | Channel not found or Topic not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

