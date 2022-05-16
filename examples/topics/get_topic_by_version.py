import time
import ddhub_gateway_client
from ddhub_gateway_client.api import topics_api
from ddhub_gateway_client.model.post_topic_dto import PostTopicDto
from pprint import pprint
import os
from py_dotenv import read_dotenv

#these variables need to be set

TOPIC_ID = "626afc7f8f3d9d41e4056af3"
TOPIC_VERSION = "1.0.0"
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
        api_response = api_instance.topics_controller_get_topic_history_by_id_and_version(TOPIC_ID, TOPIC_VERSION)
        pprint(api_response)
    except ddhub_gateway_client.ApiException as e:
        print("Exception when calling TopicsApi->topics_controller_get_topic_history_by_id_and_version: %s\n" % e)