import time
import ddhub_gateway_client
from ddhub_gateway_client.api import health_api
from ddhub_gateway_client.model.inline_response503 import InlineResponse503
from ddhub_gateway_client.model.inline_response200 import InlineResponse200
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
    api_instance = health_api.HealthApi(api_client)

    try:
        api_response = api_instance.health_controller_check()
        pprint(api_response)
    except ddhub_gateway_client.ApiException as e:
        print("Exception when calling HealthApi->health_controller_check: %s\n" % e)