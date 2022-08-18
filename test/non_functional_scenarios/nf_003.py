"""
    DDHub Client Gateway

    DDHub Client Gateway  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import unittest
import json

import ddhub_gateway_client
from ddhub_gateway_client.api.identity_api import IdentityApi
from ddhub_gateway_client.model.create_identity_dto import CreateIdentityDto
from ddhub_gateway_client.api.messaging_api import MessagingApi
from ddhub_gateway_client.model.send_message_dto import SendMessageDto

class Nf003(unittest.TestCase):
    """DefaultApi unit test stubs"""
    configuration = ddhub_gateway_client.Configuration(
        host = "https://ddhub-gateway-dev.energyweb.org"
    )
    private_key_for_test = "private_key_for_did_1"
    original_private_key = "private_key_for_did_original"
    
    send_message_dto = SendMessageDto(
        fqcn="channel.pub.nf.test.001",
        topic_name= "topic.nf.test.jsd7",
        topic_version= "1.0.0",
        topic_owner= "ddhub.apps.energyweb.iam.ewc",
        transaction_id= "{{$guid}}",
        payload=json.dumps({"data": 101}),
    )

    def setUp(self):
        self.api_client = ddhub_gateway_client.ApiClient(self.configuration)
        self.api_instance = MessagingApi(self.api_client)  # noqa: E501
        self.identity_api_instance = IdentityApi(self.api_client)  # noqa: E501
        self.identity_api_instance.identity_controller_post(
            create_identity_dto=CreateIdentityDto(
                private_key=self.private_key,
            )
        )

    def tearDown(self):
        self.identity_api_instance.identity_controller_post(
            create_identity_dto=CreateIdentityDto(
                private_key=self.original_private_key,
            )
        )
        self.api_client.close()        

    def test_nf_003(self):
        """Test case for nf_001
        """
        for i in range(0,10):
            api_response_body, api_response_status, api_response_headers = \
            self.api_instance.message_controlller_create(
                self.send_message_dto,
                _return_http_data_only=False
            )
            if i == 4:
                # disconnect the client
                pass
            
            if i == 5:
                self.assertEqual(500, api_response_status)
                break

        self.assertEqual(200, api_response_status)
        

if __name__ == '__main__':
    unittest.main()
