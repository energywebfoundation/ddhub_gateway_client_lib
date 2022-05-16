import time
import ddhub_gateway_client
from ddhub_gateway_client.api import channels_api
from ddhub_gateway_client.model.create_channel_dto import CreateChannelDto
from ddhub_gateway_client.model.topic_dto import TopicDto
from ddhub_gateway_client.model.channel_conditions_dto import ChannelConditionsDto
from pprint import pprint
import os
from py_dotenv import read_dotenv

#these variables need to be set

TOPIC_NAME = "name"
TOPIC_OWNER = "owner"
FQCN = "aresguerre.fqcn"
CHANNEL_TYPE = "sub"

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
    api_instance = channels_api.ChannelsApi(api_client)
    topic_dto = TopicDto(
        topic_name=TOPIC_NAME,
        owner=TOPIC_OWNER,
    )
    channel_condition_dto = ChannelConditionsDto(
        topics=[topic_dto],
    )
    create_channel_dto = CreateChannelDto(
        fqcn=FQCN,
        type=CHANNEL_TYPE,
        conditions=channel_condition_dto,
    ) # CreateChannelDto | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.channel_controller_create(create_channel_dto)
        pprint(api_response)
    except ddhub_gateway_client.ApiException as e:
        print("Exception when calling ChannelsApi->channel_controller_create: %s\n" % e)
