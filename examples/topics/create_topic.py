import time

import ddhub_gateway_client
from ddhub_gateway_client.api import topics_api
from ddhub_gateway_client.model.post_topic_body_dto import PostTopicBodyDto
from ddhub_gateway_client.model.post_topic_dto import PostTopicDto
from pprint import pprint
import os
from py_dotenv import read_dotenv
import json

#these variables need to be set

TOPIC_NAME = "Topic_JSON_VV51"
TOPIC_SCHEMA_TYPE = "JSD7"
TOPIC_SCHEMA = {
    '$schema': 'http://json-schema.org/draft-07/schema#',
    'type': 'object',
    'properties': {
        'rrp': {
            'type': 'integer'
        },
        'dispatchDateTime': {
            'type': 'string'
        },
        'duid': {
            'type': 'string'
        },
        'offerSubmissionDateTime': {
            'type': 'string'
        },
        'offerTradingDate': {
            'type': 'string'
        },
        'totalCleared': {
            'type': 'integer'
        }
    },
    'required': [
        'dispatchDateTime',
        'duid',
        'totalCleared',
        'offerTradingDate',
        'offerSubmissionDateTime',
        'rrp'
    ]
}
TOPIC_VERSION = "1.0.0"
TOPIC_OWNER = "mini.apps.sliced.carrot.vege.iam.ewc"
TOPIC_TAGS = ["aggregator"]

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
    post_topic_body_dto = PostTopicBodyDto(
        name=TOPIC_NAME,
        schema_type=TOPIC_SCHEMA_TYPE,
        schema=json.dumps(TOPIC_SCHEMA),
        version=TOPIC_VERSION,
        owner=TOPIC_OWNER,
        tags=TOPIC_TAGS,
    ) # PostTopicBodyDto | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.topics_controller_post_topics(post_topic_body_dto)
        pprint(api_response)
    except ddhub_gateway_client.ApiException as e:
        print("Exception when calling TopicsApi->topics_controller_post_topics: %s\n" % e)