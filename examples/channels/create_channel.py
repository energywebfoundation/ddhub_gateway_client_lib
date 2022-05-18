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

FQCN = "aresguerre.fqcn"
CHANNEL_TYPE = "sub"
PAYLOAD_ENCRYPTION = True

CHANNEL_CONDITION_DIDS = ["did:ethr:volta:0x552761011ea5b332605Bc1Cc2020A4a4f8C738CD",]
CHANNEL_CONDITION_ROLES = ["channelcreation.roles.dsb.apps.energyweb.iam.ewc",]

TOPIC_NAME = "Topic_JSON_VV51"
TOPIC_OWNER = "mini.apps.sliced.carrot.vege.iam.ewc"
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
        dids=CHANNEL_CONDITION_DIDS,
        topics=[topic_dto],
        roles=CHANNEL_CONDITION_ROLES,
    )
    create_channel_dto = CreateChannelDto(
        fqcn=FQCN,
        payload_encryption=PAYLOAD_ENCRYPTION,
        type=CHANNEL_TYPE,
        conditions=channel_condition_dto,
    ) # CreateChannelDto | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.channel_controller_create(create_channel_dto)
        pprint(api_response)
    except ddhub_gateway_client.ApiException as e:
        print("Exception when calling ChannelsApi->channel_controller_create: %s\n" % e)
