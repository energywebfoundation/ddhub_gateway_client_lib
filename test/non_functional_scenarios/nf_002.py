"""
    DDHub Client Gateway

    DDHub Client Gateway  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


from http import client
import unittest
import json

import ddhub_gateway_client
from ddhub_gateway_client.api.identity_api import IdentityApi
from ddhub_gateway_client.model.create_identity_dto import CreateIdentityDto
from ddhub_gateway_client.api.messaging_api import MessagingApi
from ddhub_gateway_client.model.send_message_dto import SendMessageDto

class Nf002(unittest.TestCase):
    """DefaultApi unit test stubs"""
    configuration = ddhub_gateway_client.Configuration(
        host = "https://ddhub-gateway-dev.energyweb.org"
    )
    private_key_for_test = "private_key_for_did_1"
    original_private_key = "private_key_for_did_original"
    
    send_message_dto = SendMessageDto(
        fqcn="channel.pub.nftesting.001",
        topic_name= "topic.nonfunctional.testing.jsd7",
        topic_version= "1.0.0",
        topic_owner= "ddhub.apps.energyweb.iam.ewc",
        transaction_id= "1234",
        payload=json.dumps({"data": 101}),
    )

    def setUp(self):
        self.api_client = ddhub_gateway_client.ApiClient(self.configuration)
        self.api_instance = MessagingApi(self.api_client)  # noqa: E501
        self.identity_api_instance = IdentityApi(self.api_client)  # noqa: E501
        self.identity_api_instance.identity_controller_post(
            create_identity_dto=CreateIdentityDto(
                private_key=self.private_key_for_test,
            )
        )

    def tearDown(self):
        self.identity_api_instance.identity_controller_post(
            create_identity_dto=CreateIdentityDto(
                private_key=self.original_private_key,
            )
        )
        self.api_client.close()        

    def test_nf_002(self):
        """Test case for nf_001
        """
        received_messages = []
        
        for i in range(1,30):
            print("Sending message {}".format(i))
            self.api_instance.message_controlller_create(
                self.send_message_dto,
                _return_http_data_only=False
            )
        
        for j in range(1,15):
            print("Receiving message {}".format(i))
            api_response_body, api_response_status, api_response_headers = \
            self.api_instance.message_controlller_get_message(
                fqcn="test.lib.sub.channel",
                amount=2,
                client_id="1234",
                _return_http_data_only=False
            )
            received_messages.append(api_response_body)
        
            if j == 4 :
                # break connection
                pass
            
            
            
        self.assertEqual(len(received_messages),6)
            
        


if __name__ == '__main__':
    unittest.main()