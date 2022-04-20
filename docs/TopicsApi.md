# openapi_client.TopicsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**topics_controller_delete_topics**](TopicsApi.md#topics_controller_delete_topics) | **DELETE** /api/v2/topics/{id} | 
[**topics_controller_delete_topics_by_version**](TopicsApi.md#topics_controller_delete_topics_by_version) | **DELETE** /api/v2/topics/{id}/versions/{version} | 
[**topics_controller_get_topic_history_by_id_and_version**](TopicsApi.md#topics_controller_get_topic_history_by_id_and_version) | **GET** /api/v2/topics/{id}/versions/{versionNumber} | 
[**topics_controller_get_topics**](TopicsApi.md#topics_controller_get_topics) | **GET** /api/v2/topics | 
[**topics_controller_get_topics_by_search**](TopicsApi.md#topics_controller_get_topics_by_search) | **GET** /api/v2/topics/search | 
[**topics_controller_get_topics_count_by_owner**](TopicsApi.md#topics_controller_get_topics_count_by_owner) | **GET** /api/v2/topics/count | 
[**topics_controller_get_topics_history_by_id**](TopicsApi.md#topics_controller_get_topics_history_by_id) | **GET** /api/v2/topics/{id}/versions | 
[**topics_controller_post_topics**](TopicsApi.md#topics_controller_post_topics) | **POST** /api/v2/topics | 
[**topics_controller_update_topics**](TopicsApi.md#topics_controller_update_topics) | **PUT** /api/v2/topics/{id} | 
[**topics_controller_update_topics_by_id_and_version**](TopicsApi.md#topics_controller_update_topics_by_id_and_version) | **PUT** /api/v2/topics/{id}/versions/{versionNumber} | 


# **topics_controller_delete_topics**
> DeleteTopic topics_controller_delete_topics(id)



### Example


```python
import time
import openapi_client
from openapi_client.api import topics_api
from openapi_client.model.delete_topic import DeleteTopic
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = topics_api.TopicsApi(api_client)
    id = "62545547fe37f174d7715ff3" # str | id of the topic

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.topics_controller_delete_topics(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TopicsApi->topics_controller_delete_topics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id of the topic |

### Return type

[**DeleteTopic**](DeleteTopic.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Topic deleted successfully |  -  |
**400** | Validation failed or some requirements were not fully satisfied |  -  |
**401** | Unauthorized |  -  |
**404** | Topic not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **topics_controller_delete_topics_by_version**
> DeleteTopic topics_controller_delete_topics_by_version(id, version)



### Example


```python
import time
import openapi_client
from openapi_client.api import topics_api
from openapi_client.model.delete_topic import DeleteTopic
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = topics_api.TopicsApi(api_client)
    id = "62545547fe37f174d7715ff3" # str | id of the topic
    version = "1.0.9" # str | version of the topic

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.topics_controller_delete_topics_by_version(id, version)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TopicsApi->topics_controller_delete_topics_by_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id of the topic |
 **version** | **str**| version of the topic |

### Return type

[**DeleteTopic**](DeleteTopic.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Topic deleted successfully |  -  |
**400** | Validation failed or some requirements were not fully satisfied |  -  |
**401** | Unauthorized |  -  |
**404** | Topic not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **topics_controller_get_topic_history_by_id_and_version**
> PostTopicDto topics_controller_get_topic_history_by_id_and_version(id, version_number)



### Example


```python
import time
import openapi_client
from openapi_client.api import topics_api
from openapi_client.model.post_topic_dto import PostTopicDto
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = topics_api.TopicsApi(api_client)
    id = "62545547fe37f174d7715ff3" # str | id of the topic
    version_number = "1.0.9" # str | version of the topic

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.topics_controller_get_topic_history_by_id_and_version(id, version_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TopicsApi->topics_controller_get_topic_history_by_id_and_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id of the topic |
 **version_number** | **str**| version of the topic |

### Return type

[**PostTopicDto**](PostTopicDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Topics History by Id and version |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **topics_controller_get_topics**
> PaginatedResponse topics_controller_get_topics(owner)



### Example


```python
import time
import openapi_client
from openapi_client.api import topics_api
from openapi_client.model.paginated_response import PaginatedResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = topics_api.TopicsApi(api_client)
    owner = "ddhub.apps.energyweb.iam.ewc" # str | 
    limit = 1 # float |  (optional) if omitted the server will use the default value of 0
    name = "topic name" # str |  (optional) if omitted the server will use the default value of ""
    page = 1 # float |  (optional) if omitted the server will use the default value of 1
    tags = ["aggregator"] # [str] |  (optional) if omitted the server will use the default value of []

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.topics_controller_get_topics(owner)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TopicsApi->topics_controller_get_topics: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.topics_controller_get_topics(owner, limit=limit, name=name, page=page, tags=tags)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TopicsApi->topics_controller_get_topics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  |
 **limit** | **float**|  | [optional] if omitted the server will use the default value of 0
 **name** | **str**|  | [optional] if omitted the server will use the default value of ""
 **page** | **float**|  | [optional] if omitted the server will use the default value of 1
 **tags** | **[str]**|  | [optional] if omitted the server will use the default value of []

### Return type

[**PaginatedResponse**](PaginatedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Topics List |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **topics_controller_get_topics_by_search**
> PaginatedSearchTopicResponse topics_controller_get_topics_by_search(keyword)



### Example


```python
import time
import openapi_client
from openapi_client.api import topics_api
from openapi_client.model.paginated_search_topic_response import PaginatedSearchTopicResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = topics_api.TopicsApi(api_client)
    keyword = "Topic_JSON_V12" # str | 
    limit = 1 # float |  (optional) if omitted the server will use the default value of 0
    page = 1 # float |  (optional) if omitted the server will use the default value of 1

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.topics_controller_get_topics_by_search(keyword)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TopicsApi->topics_controller_get_topics_by_search: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.topics_controller_get_topics_by_search(keyword, limit=limit, page=page)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TopicsApi->topics_controller_get_topics_by_search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyword** | **str**|  |
 **limit** | **float**|  | [optional] if omitted the server will use the default value of 0
 **page** | **float**|  | [optional] if omitted the server will use the default value of 1

### Return type

[**PaginatedSearchTopicResponse**](PaginatedSearchTopicResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Topics by Search |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **topics_controller_get_topics_count_by_owner**
> TopicsCountResponse topics_controller_get_topics_count_by_owner(owner)



### Example


```python
import time
import openapi_client
from openapi_client.api import topics_api
from openapi_client.model.topics_count_response import TopicsCountResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = topics_api.TopicsApi(api_client)
    owner = ["torta.apps.eggplant.vege.iam.ewc","mini.apps.sliced.carrot.vege.iam.ewc"] # [str] | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.topics_controller_get_topics_count_by_owner(owner)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TopicsApi->topics_controller_get_topics_count_by_owner: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **[str]**|  |

### Return type

[**TopicsCountResponse**](TopicsCountResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Topics Count by Owner |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **topics_controller_get_topics_history_by_id**
> PaginatedSearchTopicResponse topics_controller_get_topics_history_by_id(id)



### Example


```python
import time
import openapi_client
from openapi_client.api import topics_api
from openapi_client.model.paginated_search_topic_response import PaginatedSearchTopicResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = topics_api.TopicsApi(api_client)
    id = "62545547fe37f174d7715ff3" # str | id of the topic

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.topics_controller_get_topics_history_by_id(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TopicsApi->topics_controller_get_topics_history_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id of the topic |

### Return type

[**PaginatedSearchTopicResponse**](PaginatedSearchTopicResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Topics List with same Id and different versions |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **topics_controller_post_topics**
> PostTopicDto topics_controller_post_topics(post_topic_body_dto)



### Example


```python
import time
import openapi_client
from openapi_client.api import topics_api
from openapi_client.model.post_topic_body_dto import PostTopicBodyDto
from openapi_client.model.post_topic_dto import PostTopicDto
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = topics_api.TopicsApi(api_client)
    post_topic_body_dto = PostTopicBodyDto(
        name="Topic_JSON_V12",
        schema_type="JSD7",
        schema="{"type":"object","properties":{"data":{"type":"number"}}}",
        version="1.0.9",
        owner="torta.apps.eggplant.vege.iam.ewc",
        tags=[
            "["aggregator"]",
        ],
    ) # PostTopicBodyDto | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.topics_controller_post_topics(post_topic_body_dto)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TopicsApi->topics_controller_post_topics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_topic_body_dto** | [**PostTopicBodyDto**](PostTopicBodyDto.md)|  |

### Return type

[**PostTopicDto**](PostTopicDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Topic successfully created |  -  |
**400** | Validation failed or some requirements were not fully satisfied |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **topics_controller_update_topics**
> PostTopicDto topics_controller_update_topics(id, update_topic_body_dto)



### Example


```python
import time
import openapi_client
from openapi_client.api import topics_api
from openapi_client.model.update_topic_body_dto import UpdateTopicBodyDto
from openapi_client.model.post_topic_dto import PostTopicDto
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = topics_api.TopicsApi(api_client)
    id = "62545547fe37f174d7715ff3" # str | id of the topic
    update_topic_body_dto = UpdateTopicBodyDto(
        tags=[
            "["aggregator"]",
        ],
    ) # UpdateTopicBodyDto | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.topics_controller_update_topics(id, update_topic_body_dto)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TopicsApi->topics_controller_update_topics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id of the topic |
 **update_topic_body_dto** | [**UpdateTopicBodyDto**](UpdateTopicBodyDto.md)|  |

### Return type

[**PostTopicDto**](PostTopicDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Topic updated successfully |  -  |
**400** | Validation failed or some requirements were not fully satisfied |  -  |
**401** | Unauthorized |  -  |
**404** | Topic not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **topics_controller_update_topics_by_id_and_version**
> PostTopicDto topics_controller_update_topics_by_id_and_version(id, version_number, update_topic_history_body_dto)



### Example


```python
import time
import openapi_client
from openapi_client.api import topics_api
from openapi_client.model.update_topic_history_body_dto import UpdateTopicHistoryBodyDto
from openapi_client.model.post_topic_dto import PostTopicDto
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = topics_api.TopicsApi(api_client)
    id = "62545547fe37f174d7715ff3" # str | id of the topic
    version_number = "1.0.9" # str | version of the topic
    update_topic_history_body_dto = UpdateTopicHistoryBodyDto(
        schema="{"type":"object","properties":{"data":{"type":"number"}}}",
    ) # UpdateTopicHistoryBodyDto | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.topics_controller_update_topics_by_id_and_version(id, version_number, update_topic_history_body_dto)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TopicsApi->topics_controller_update_topics_by_id_and_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id of the topic |
 **version_number** | **str**| version of the topic |
 **update_topic_history_body_dto** | [**UpdateTopicHistoryBodyDto**](UpdateTopicHistoryBodyDto.md)|  |

### Return type

[**PostTopicDto**](PostTopicDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Topic updated successfully |  -  |
**400** | Validation failed or some requirements were not fully satisfied |  -  |
**401** | Unauthorized |  -  |
**404** | Topic not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

