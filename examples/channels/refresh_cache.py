import time
import ddhub_gateway_client
from ddhub_gateway_client.api import channels_api
from pprint import pprint
import os
from py_dotenv import read_dotenv

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

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.channel_controller_refresh_did()
    except ddhub_gateway_client.ApiException as e:
        print("Exception when calling ChannelsApi->channel_controller_refresh_did: %s\n" % e)