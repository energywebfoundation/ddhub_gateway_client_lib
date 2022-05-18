import time
import ddhub_gateway_client
from ddhub_gateway_client.api import topics_api
from ddhub_gateway_client.model.paginated_search_topic_response import PaginatedSearchTopicResponse
from pprint import pprint
import os
from py_dotenv import read_dotenv

#TODO check error 500 when optional are passed

#these variables need to be set
SEARCH_KEYWORD = "Topic_JSON_V12" # str | 
SEARCH_LIMIT = 1 # float |  (optional) if omitted the server will use the default value of 0
SEARCH_PAGE = 1 # float |  (optional) if omitted the server will use the default value of 1

# Read dotenv
dotenv_path = os.path.join(os.path.abspath('./examples/'), '.env')
read_dotenv(dotenv_path)

SERVER_HOST:str = os.getenv('SERVER_HOST')

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ddhub_gateway_client.Configuration(
    host = SERVER_HOST
)


# Enter a context with an instance of the API client
with ddhub_gateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = topics_api.TopicsApi(api_client)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.topics_controller_get_topics_by_search(SEARCH_KEYWORD)
        pprint(api_response)
    except ddhub_gateway_client.ApiException as e:
        print("Exception when calling TopicsApi->topics_controller_get_topics_by_search: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.topics_controller_get_topics_by_search(SEARCH_KEYWORD, limit=SEARCH_LIMIT, page=SEARCH_LIMIT)
        pprint(api_response)
    except ddhub_gateway_client.ApiException as e:
        print("Exception when calling TopicsApi->topics_controller_get_topics_by_search: %s\n" % e)