import time
import ddhub_gateway_client
from ddhub_gateway_client.api import messaging_api
from ddhub_gateway_client.model.send_messagel_response_dto import SendMessagelResponseDto
from pprint import pprint
import os
from py_dotenv import read_dotenv

FQCN = "aresguerre.upload" # str | Channel Name
TOPIC_NAME = "Topic_JSON_VV51" # str | Topic name
TOPIC_VERSION = "1.0.0" # str | Topic Version
TOPIC_OWNER = "mini.apps.sliced.carrot.vege.iam.ewc" # str | Topic Owner
FILE_LOCATION = './examples/messaging/files/'
FILE_NAME = 'upload.csv' 


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
    api_instance = messaging_api.MessagingApi(api_client)
    file = open(FILE_LOCATION+FILE_NAME, 'rb') # file_type | File uploaded

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.message_controlller_upload_file(file, FQCN, TOPIC_NAME, TOPIC_VERSION, TOPIC_OWNER)
        pprint(api_response)
    except ddhub_gateway_client.ApiException as e:
        print("Exception when calling MessagingApi->message_controlller_upload_file: %s\n" % e)