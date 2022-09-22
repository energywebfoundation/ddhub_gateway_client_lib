"""
    DDHub Client Gateway

    DDHub Client Gateway  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""

import re
import sys
from time import time, sleep
import unittest
import json
import pprint 
import random, string

import ddhub_gateway_client
from ddhub_gateway_client.api.identity_api import IdentityApi
from ddhub_gateway_client.model.create_identity_dto import CreateIdentityDto
from ddhub_gateway_client.api.messaging_api import MessagingApi
from ddhub_gateway_client.model.send_message_dto import SendMessageDto

def random_string(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

# raw_input returns the empty string for "enter"
yes = {'yes','y', 'ye', ''}
no = {'no','n'}

pp = pprint.PrettyPrinter(indent=4)

class DHNf001(unittest.TestCase):
    """DefaultApi unit test stubs"""
    configuration = ddhub_gateway_client.Configuration(
        host = "https://ddhub-gateway-dev.energyweb.org"
    )

    def setUp(self):
        print("Are you connected to Client Gateway with ID DID:ether:volta:************************738CD [Y/n]?")
        answered = False
        
        while not answered:
            choice = input().lower()
            if choice in yes:
                print("*\n*\n*\n\nStarting test")
                answered = True
            elif choice in no:
                answered = True
                print("Please connect to Client Gateway with ID DID:ether:volta:************************738CD and try again")
                return
            else:
                sys.stdout.write("Please respond with 'yes' or 'no' \n")
        
        self.api = MessagingApi(ddhub_gateway_client.ApiClient(self.configuration))
        self.api2 = IdentityApi(ddhub_gateway_client.ApiClient(self.configuration))
        self.api_client = ddhub_gateway_client.ApiClient(self.configuration)
        self.api_instance = MessagingApi(self.api_client)  # noqa: E501
        print("Connecting to: " + self.configuration.host)

    def tearDown(self):
        self.api_client.close()        

    def test_nf_001(self):
        """Test case for nf_001
        """

        for i in range(1,120):
            try:
                sleep(5)
                send_message_dto = SendMessageDto(
                                        fqcn="channel.pub.nf.test.001",
                                        topic_name= "topic.nf.test.jsd7",
                                        topic_version= "1.0.0",
                                        topic_owner= "ddhub.apps.energyweb.iam.ewc",
                                        transaction_id= random_string(10),
                                        payload=json.dumps({"data": i}),
                )
                print ("Posting message: ")
                pp.pprint(send_message_dto.to_dict())
                api_response_body, api_response_status, api_response_headers = \
                self.api_instance.message_controlller_create(
                    send_message_dto=send_message_dto,
                    _return_http_data_only=False
                )
                if i >= 12:
                    print("***************************\n*  Disconnect the client  *\n***************************")

            except Exception as e:
                print(e)
                if i > 12 and i < 120:
                    print("Exception:", e)
                    self.assertTrue(True)
                    return

        self.assertTrue(False, "Test failed or client not disconnected")
        

if __name__ == '__main__':
    unittest.main()
