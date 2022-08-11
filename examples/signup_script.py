"""
    DDHub Client Gateway

    Example file for registring a new private key.
"""

from pprint import pprint

import ddhub_gateway_client
from ddhub_gateway_client.api.identity_api import IdentityApi
from ddhub_gateway_client.api.enrolment_api import EnrolmentApi
from ddhub_gateway_client.model.create_identity_dto import CreateIdentityDto
from ddhub_gateway_client.model.identity_response_dto import IdentityResponseDto


PRIVATE_KEY = 'df7d3867fcb24b19aa3fb596e097d8f3de3c1bd92d36f08d43bdbdc803dbd025'

SERVER_HOST:str = "https://ddhub-gateway-dev.energyweb.org"

# Defining the host is optional and defaults to http://localhost
configuration = ddhub_gateway_client.Configuration(
    host = SERVER_HOST
)

# Enter a context with an instance of the API client
with ddhub_gateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    identity_api = IdentityApi(api_client)
    enrolment_api = EnrolmentApi(api_client)

    create_identity_dto = CreateIdentityDto(
        private_key=PRIVATE_KEY,
    )

    # example registring a new private key to DDHub Client Gateway
    try:
        api_response:IdentityResponseDto = identity_api.identity_controller_post(create_identity_dto)
        pprint(api_response)
    except ddhub_gateway_client.ApiException as e:
        print("Exception when calling IdentityApi->identity_controller_post: %s\n" % e)

    try:
        enrolment_api.enrolment_controller_init()
        print("Enrolment to default role has been requested!")
    except ddhub_gateway_client.ApiException as e:
        print("Exception when calling EnrolmentApi->enrolment_controller_init: %s\n" % e)
