import time
import ddhub_gateway_client
from ddhub_gateway_client.api import topics_api
from ddhub_gateway_client.model.update_topic_body_dto import UpdateTopicBodyDto
from ddhub_gateway_client.model.post_topic_dto import PostTopicDto
from pprint import pprint
import os
from py_dotenv import read_dotenv
import json

#these variables need to be set

TOPIC_ID = "6284f112a41e530eb7ccfda1" # 62545547fe37f174d7715ff3
TOPIC_TAGS = ["dso"]

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
    update_topic_body_dto = UpdateTopicBodyDto(
        tags=TOPIC_TAGS,
    ) # UpdateTopicBodyDto | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.topics_controller_update_topics(TOPIC_ID, update_topic_body_dto)
        pprint(api_response)
    except ddhub_gateway_client.ApiException as e:
        print("Exception when calling TopicsApi->topics_controller_update_topics: %s\n" % e)