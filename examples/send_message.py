"""
    DDHub Client Gateway

    Example file for sending messages.
"""

import json
from pprint import pprint

import ddhub_gateway_client
from ddhub_gateway_client.api.messaging_api import MessagingApi
from ddhub_gateway_client.exceptions import ApiException
from ddhub_gateway_client.model.send_message_dto import SendMessageDto
from ddhub_gateway_client.model.send_messagel_response_dto import SendMessagelResponseDto


SERVER_HOST:str = 'https://ddhub-gateway-dev.energyweb.org'

# Defining the host is optional and defaults to http://localhost
configuration = ddhub_gateway_client.Configuration(
    host = SERVER_HOST
)

message:SendMessageDto = SendMessageDto(
    fqcn='example.lib.pub.channel',
    topic_name='example_data_topic',
    topic_version='0.0.1',
    topic_owner='libtesting.apps.aresguerre.iam.ewc',
    transaction_id='unique_string',
    payload=json.dumps({'data':1})
)

with ddhub_gateway_client.ApiClient(configuration) as api_client:

    messaging_api = MessagingApi(api_client)

    try:
        api_response=messaging_api.message_controlller_create(message)
        for message in api_response:
            pprint(message)
    except ApiException as e:
        print("Exception when calling MessagingApi->message_controlller_get_message: %s\n" % e)