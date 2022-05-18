import time
import ddhub_gateway_client
from ddhub_gateway_client.api import messaging_api
from pprint import pprint
import os
from py_dotenv import read_dotenv

FILE_ID = "bb2686d2-97be-436b-8869"

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

    # example passing only required values which don't have defaults set
    try:
        api_instance.message_controlller_download_message(FILE_ID)
    except ddhub_gateway_client.ApiException as e:
        print("Exception when calling MessagingApi->message_controlller_download_message: %s\n" % e)