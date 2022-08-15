"""
    DDHub Client Gateway

    Example file for uploading files.
"""

from pprint import pprint

import ddhub_gateway_client
from ddhub_gateway_client.api.messaging_api import MessagingApi
from ddhub_gateway_client.model.send_messagel_response_dto import SendMessagelResponseDto

FILE_LOCATION = './examples/files/'
FILE_NAME = 'upload.csv'

SERVER_HOST:str = 'https://ddhub-gateway-dev.energyweb.org'

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ddhub_gateway_client.Configuration(
    host = SERVER_HOST
)


# Enter a context with an instance of the API client
with ddhub_gateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    messaging_api = MessagingApi(api_client)
    file = open(FILE_LOCATION+FILE_NAME, 'rb') # file_type | File uploaded

    # example passing only required values which don't have defaults set
    try:
        api_response:SendMessagelResponseDto = messaging_api.message_controlller_upload_file(
            file=file,
            fqcn='example.lib.upload.channel',
            topic_name='example_file_topic',
            topic_version='0.0.1',
            topic_owner='libtesting.apps.aresguerre.iam.ewc'
        )
        pprint(api_response)
    except ddhub_gateway_client.ApiException as e:
        print("Exception when calling MessagingApi->message_controlller_upload_file: %s\n" % e)