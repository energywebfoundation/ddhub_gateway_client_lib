"""
    DDHub Client Gateway

    Example file for creating a Topic and Channel.
"""

import json
from pprint import pprint

import ddhub_gateway_client
from ddhub_gateway_client.api.topics_api import TopicsApi
from ddhub_gateway_client.api.channels_api import ChannelsApi
from ddhub_gateway_client.exceptions import ApiException
from ddhub_gateway_client.model.post_topic_body_dto import PostTopicBodyDto
from ddhub_gateway_client.model.post_topic_dto import PostTopicDto
from ddhub_gateway_client.model.channel_conditions_dto import ChannelConditionsDto
from ddhub_gateway_client.model.create_channel_dto import CreateChannelDto
from ddhub_gateway_client.model.topic_dto import TopicDto


example_data_topic:PostTopicBodyDto = PostTopicBodyDto(
    name="example_data_topic",
    schema_type="JSD7",
    schema=json.dumps({
        'type': 'object',
        'properties': {
            'data': {
                'type': 'integer'
            },
        },
        'required':['data',]
    }),
    version="0.0.1",
    owner="libtesting.apps.aresguerre.iam.ewc",
    tags=['test_tag']
)

# example_file_topic:PostTopicBodyDto = PostTopicBodyDto(
#     name="example_file_topic",
#     schema_type="CSV",
#     schema='{}',
#     version="0.0.1",
#     owner="libtesting.apps.aresguerre.iam.ewc",
#     tags=['test_tag']
# )

channel_topic:TopicDto = TopicDto(
    topic_name=example_data_topic.name,
    owner=example_data_topic.owner,
)

channel_conditions:ChannelConditionsDto = ChannelConditionsDto(
    dids=[],
    roles=['user.roles.ddhub.apps.energyweb.iam.ewc'],
    topics=[channel_topic]
)

example_publisher_channel:CreateChannelDto=CreateChannelDto(
    fqcn='example.lib.pub.channel',
    payload_encryption=True,
    type='pub', # sub|pub|download|upload
    conditions=channel_conditions
)

# example_subscriber_channel:CreateChannelDto=CreateChannelDto(
#     fqcn='example.lib.sub.channel',
#     payload_encryption=True,
#     type='sub', # sub|pub|download|upload
#     conditions=channel_conditions
# )

SERVER_HOST:str = 'https://ddhub-gateway-dev.energyweb.org'

# Defining the host is optional and defaults to http://localhost
configuration = ddhub_gateway_client.Configuration(
    host = SERVER_HOST
)

with ddhub_gateway_client.ApiClient(configuration) as api_client:

    topics_api = TopicsApi(api_client)
    channel_api = ChannelsApi(api_client)

    try:
        api_response:PostTopicDto = topics_api.topics_controller_post_topics(example_data_topic)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TopicsApi->topics_controller_post_topics: %s\n" % e)

    try:
        api_response = channel_api.channel_controller_create(example_publisher_channel)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChannelsApi->channel_controller_create: %s\n" % e)
