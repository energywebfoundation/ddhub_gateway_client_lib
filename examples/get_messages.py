"""
    DDHub Client Gateway

    Example file for reading messages.
"""

from pprint import pprint

import ddhub_gateway_client
from ddhub_gateway_client.api.messaging_api import MessagingApi
from ddhub_gateway_client.exceptions import ApiException
from ddhub_gateway_client.model.get_messages_response_dto import GetMessagesResponseDto


SERVER_HOST:str = 'https://ddhub-gateway-dev.energyweb.org'

# Defining the host is optional and defaults to http://localhost
configuration = ddhub_gateway_client.Configuration(
    host = SERVER_HOST
)

with ddhub_gateway_client.ApiClient(configuration) as api_client:

    messaging_api = MessagingApi(api_client)
    channel_fqcn = 'example.lib.sub.channel'

    try:
        api_response=messaging_api.message_controlller_get_message(channel_fqcn)
        for message in api_response:
            pprint(message)
    except ApiException as e:
        print("Exception when calling MessagingApi->message_controlller_get_message: %s\n" % e)
