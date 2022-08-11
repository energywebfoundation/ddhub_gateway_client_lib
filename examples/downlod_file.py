"""
    DDHub Client Gateway

    Example file for downloading files.
"""

import json
from pprint import pprint

import ddhub_gateway_client
from ddhub_gateway_client.api.messaging_api import MessagingApi
from ddhub_gateway_client.exceptions import ApiException
from ddhub_gateway_client.model.get_messages_response_dto import GetMessagesResponseDto

SERVER_HOST:str = 'https://ddhub-gateway-dev.energyweb.org'

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ddhub_gateway_client.Configuration(
    host = SERVER_HOST
)


# Enter a context with an instance of the API client
with ddhub_gateway_client.ApiClient(configuration) as api_client:

    messaging_api = MessagingApi(api_client)
    FQCN = 'example.lib.download.channel'

    try:
        api_response=messaging_api.message_controlller_get_message(FQCN)
        last_message:GetMessagesResponseDto = api_response[0]
        FILE_ID = json.loads(last_message.payload)['fileId']

        try:
            messaging_api.message_controlller_download_message(FILE_ID)

        except ddhub_gateway_client.ApiException as e:
            print("Exception when calling MessagingApi->message_controlller_download_message: %s\n" % e)

    except ApiException as e:
        print("Exception when calling MessagingApi->message_controlller_get_message: %s\n" % e)
