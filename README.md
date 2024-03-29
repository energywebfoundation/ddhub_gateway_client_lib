# ddhub-gateway-client-lib
DDHub Client Gateway Library

This Python library connects to [DDHub Client Gateway](https://github.com/energywebfoundation/ddhub-client-gateway).

## Requirements.

Python >=3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/energywebfoundation/ddhub_gateway_client_lib.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/energywebfoundation/ddhub_gateway_client_lib.git`)

Then import the package:
```python
import ddhub_gateway_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import ddhub_gateway_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import ddhub_gateway_client
from pprint import pprint
from ddhub_gateway_client.api import applications_api
from ddhub_gateway_client.model.application_dto import ApplicationDTO
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

    try:
        api_response = api_instance.applications_controller_get_applications(role_name)
        pprint(api_response)
    except ddhub_gateway_client.ApiException as e:
        print("Exception when calling ApplicationsApi->applications_controller_get_applications: %s\n" % e)
```

## Examples

See potential use cases in the [examples directory](examples/README.md).

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ApplicationsApi* | [**applications_controller_get_applications**](docs/ApplicationsApi.md#applications_controller_get_applications) | **GET** /api/v2/applications | 
*ApplicationsApi* | [**applications_controller_get_applications_by_namespace**](docs/ApplicationsApi.md#applications_controller_get_applications_by_namespace) | **GET** /api/v2/applications/{namespace} | 
*ChannelsApi* | [**channel_controller_create**](docs/ChannelsApi.md#channel_controller_create) | **POST** /api/v2/channels | 
*ChannelsApi* | [**channel_controller_delete**](docs/ChannelsApi.md#channel_controller_delete) | **DELETE** /api/v2/channels/{fqcn} | 
*ChannelsApi* | [**channel_controller_get**](docs/ChannelsApi.md#channel_controller_get) | **GET** /api/v2/channels/{fqcn} | 
*ChannelsApi* | [**channel_controller_get_by_type**](docs/ChannelsApi.md#channel_controller_get_by_type) | **GET** /api/v2/channels | 
*ChannelsApi* | [**channel_controller_get_qualified_dids**](docs/ChannelsApi.md#channel_controller_get_qualified_dids) | **GET** /api/v2/channels/{fqcn}/qualifiedDids | 
*ChannelsApi* | [**channel_controller_refresh_did**](docs/ChannelsApi.md#channel_controller_refresh_did) | **POST** /api/v2/channels/refresh | 
*ChannelsApi* | [**channel_controller_update**](docs/ChannelsApi.md#channel_controller_update) | **PUT** /api/v2/channels/{fqcn} | 
*EnrolmentApi* | [**enrolment_controller_get**](docs/EnrolmentApi.md#enrolment_controller_get) | **GET** /api/v2/enrol | 
*EnrolmentApi* | [**enrolment_controller_init**](docs/EnrolmentApi.md#enrolment_controller_init) | **POST** /api/v2/enrol | 
*GatewayApi* | [**gateway_controller_get**](docs/GatewayApi.md#gateway_controller_get) | **GET** /api/v2/gateway | 
*GatewayConfigurationApi* | [**certificate_controller_save**](docs/GatewayConfigurationApi.md#certificate_controller_save) | **POST** /api/v2/certificate | 
*GatewayConfigurationApi* | [**keys_controller_derive**](docs/GatewayConfigurationApi.md#keys_controller_derive) | **POST** /api/v2/keys | 
*HealthApi* | [**health_controller_check**](docs/HealthApi.md#health_controller_check) | **GET** /api/v2/health | 
*IdentityApi* | [**identity_controller_get**](docs/IdentityApi.md#identity_controller_get) | **GET** /api/v2/identity | 
*IdentityApi* | [**identity_controller_get_claims**](docs/IdentityApi.md#identity_controller_get_claims) | **GET** /api/v2/identity/claims | 
*IdentityApi* | [**identity_controller_post**](docs/IdentityApi.md#identity_controller_post) | **POST** /api/v2/identity | 
*MessagingApi* | [**message_controlller_create**](docs/MessagingApi.md#message_controlller_create) | **POST** /api/v2/messages | 
*MessagingApi* | [**message_controlller_download_message**](docs/MessagingApi.md#message_controlller_download_message) | **GET** /api/v2/messages/download | 
*MessagingApi* | [**message_controlller_get_message**](docs/MessagingApi.md#message_controlller_get_message) | **GET** /api/v2/messages | 
*MessagingApi* | [**message_controlller_upload_file**](docs/MessagingApi.md#message_controlller_upload_file) | **POST** /api/v2/messages/upload | 
*TopicsApi* | [**topics_controller_delete_topics**](docs/TopicsApi.md#topics_controller_delete_topics) | **DELETE** /api/v2/topics/{id} | 
*TopicsApi* | [**topics_controller_delete_topics_by_version**](docs/TopicsApi.md#topics_controller_delete_topics_by_version) | **DELETE** /api/v2/topics/{id}/versions/{versionNumber} | 
*TopicsApi* | [**topics_controller_get_topic_history_by_id_and_version**](docs/TopicsApi.md#topics_controller_get_topic_history_by_id_and_version) | **GET** /api/v2/topics/{id}/versions/{versionNumber} | 
*TopicsApi* | [**topics_controller_get_topics**](docs/TopicsApi.md#topics_controller_get_topics) | **GET** /api/v2/topics | 
*TopicsApi* | [**topics_controller_get_topics_by_search**](docs/TopicsApi.md#topics_controller_get_topics_by_search) | **GET** /api/v2/topics/search | 
*TopicsApi* | [**topics_controller_get_topics_count_by_owner**](docs/TopicsApi.md#topics_controller_get_topics_count_by_owner) | **GET** /api/v2/topics/count | 
*TopicsApi* | [**topics_controller_get_topics_history_by_id**](docs/TopicsApi.md#topics_controller_get_topics_history_by_id) | **GET** /api/v2/topics/{id}/versions | 
*TopicsApi* | [**topics_controller_post_topics**](docs/TopicsApi.md#topics_controller_post_topics) | **POST** /api/v2/topics | 
*TopicsApi* | [**topics_controller_update_topics**](docs/TopicsApi.md#topics_controller_update_topics) | **PUT** /api/v2/topics/{id} | 
*TopicsApi* | [**topics_controller_update_topics_by_id_and_version**](docs/TopicsApi.md#topics_controller_update_topics_by_id_and_version) | **PUT** /api/v2/topics/{id}/versions/{versionNumber} | 
*DefaultApi* | [**cron_controller_get_jobs_results**](docs/DefaultApi.md#cron_controller_get_jobs_results) | **GET** /api/v2/cron | 


## Documentation For Models

 - [ApplicationDTO](docs/ApplicationDTO.md)
 - [ChannelConditions](docs/ChannelConditions.md)
 - [ChannelConditionsDto](docs/ChannelConditionsDto.md)
 - [ChannelTopic](docs/ChannelTopic.md)
 - [CreateChannelDto](docs/CreateChannelDto.md)
 - [CreateIdentityDto](docs/CreateIdentityDto.md)
 - [CronResponseDto](docs/CronResponseDto.md)
 - [DeleteTopic](docs/DeleteTopic.md)
 - [Details](docs/Details.md)
 - [EnrolmentDto](docs/EnrolmentDto.md)
 - [GatewayResponseDto](docs/GatewayResponseDto.md)
 - [GetChannelQualifiedDidsDto](docs/GetChannelQualifiedDidsDto.md)
 - [GetChannelResponseDto](docs/GetChannelResponseDto.md)
 - [GetMessagesResponseDto](docs/GetMessagesResponseDto.md)
 - [GetTopicDto](docs/GetTopicDto.md)
 - [GetTopicSearchDto](docs/GetTopicSearchDto.md)
 - [IdentityResponseDto](docs/IdentityResponseDto.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse503](docs/InlineResponse503.md)
 - [PaginatedResponse](docs/PaginatedResponse.md)
 - [PaginatedTopicResponse](docs/PaginatedTopicResponse.md)
 - [PostTopicBodyDto](docs/PostTopicBodyDto.md)
 - [PostTopicDto](docs/PostTopicDto.md)
 - [PutTopicDto](docs/PutTopicDto.md)
 - [Recipients](docs/Recipients.md)
 - [RoleDto](docs/RoleDto.md)
 - [SendMessageDto](docs/SendMessageDto.md)
 - [SendMessagelResponseDto](docs/SendMessagelResponseDto.md)
 - [Status](docs/Status.md)
 - [TopicCountDto](docs/TopicCountDto.md)
 - [TopicDto](docs/TopicDto.md)
 - [UpdateChannelDto](docs/UpdateChannelDto.md)
 - [UpdateTopicBodyDto](docs/UpdateTopicBodyDto.md)
 - [UpdateTopicHistoryBodyDto](docs/UpdateTopicHistoryBodyDto.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## License

 This project is licensed under GNU General Public License Version 3 (GPLv3)
