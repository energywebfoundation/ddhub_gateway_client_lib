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
from ddhub_gateway_client.api.messaging_api import MessagingApi
from ddhub_gateway_client.model.send_message_dto import SendMessageDto

def random_string(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

# raw_input returns the empty string for "enter"
yes = {'yes','y', 'ye', ''}
no = {'no','n'}

pp = pprint.PrettyPrinter(indent=4)

class DHNf002(unittest.TestCase):
    """DefaultApi unit test stubs"""
    configuration_sender = ddhub_gateway_client.Configuration(
        host = "https://ddhub-gateway-dev.energyweb.org"
    )
    
    configuration_receiver = ddhub_gateway_client.Configuration(
        host = "https://ddhub-gateway-dev-1.energyweb.org"
    )

    def setUp(self):
        print("Are you connected to Client-Gateway-01 with ID DID:ether:volta:************************738CD\n and Client-Gateway-02 with ID DID:ether:volta:************************bDdC [Y/n]?")
        answered = False
        
        while not answered:
            choice = input().lower()
            if choice in yes:
                print("*\n*\n*\n\nStarting test")
                answered = True
            elif choice in no:
                answered = True
                print("Please connect to Client-Gateway-01 with ID DID:ether:volta:************************738CD\n and Client-Gateway-02 with ID DID:ether:volta:************************bDdC and try again")
                sleep(5)
                raise SystemExit
            else:
                sys.stdout.write("Please respond with 'yes' or 'no' \n")
        
        self.api_sender = MessagingApi(ddhub_gateway_client.ApiClient(self.configuration_sender))
        self.api_sender_client = ddhub_gateway_client.ApiClient(self.configuration_sender)
        self.api_sender_instance = MessagingApi(self.api_sender_client)  # noqa: E501
        print("Connecting to: " + self.configuration_sender.host)

        self.api_receiver = MessagingApi(ddhub_gateway_client.ApiClient(self.configuration_receiver))
        self.api_receiver_client = ddhub_gateway_client.ApiClient(self.configuration_receiver)
        self.api_receiver_instance = MessagingApi(self.api_receiver_client)  # noqa: E501
        print("Connecting to: " + self.configuration_receiver.host)

    def tearDown(self):
        self.api_sender_client.close()  
        self.api_receiver_client.close()      

    def test_nf_001(self):
        """Test case for nf_001
        """

        for i in range(1,31):
            sleep(0.2)
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
            self.api_sender_instance.message_controlller_create(
                send_message_dto=send_message_dto,
                _return_http_data_only=False
            )

        sleep_time = 1
        received_messages = []

        for j in range(1,15):
            try: 
                sleep(sleep_time)
                print("Receiving message {}".format(j))
                api_response_body, api_response_status, api_response_headers = \
                self.api_receiver_instance.message_controlller_get_message(
                    fqcn="channel.sub.nf.test.001",
                    amount=2,
                    client_id="1234",
                    _return_http_data_only=False
                )
                print("Received message: ")
                pp.pprint(api_response_body)
                received_messages.append(api_response_body)
                
                if j >= 4 :
                    sleep_time = 5
                    print("************************************\n*  Disconnect the receiver client  *\n************************************")
                    
            except Exception as e:
                if j >= 4 :
                    print("Exception: " + str(e))
                    self.assertTrue(True)
                    self.assertGreaterEqual(len(received_messages), 4)
                    self.assertLessEqual(len(received_messages), 15)
                    return
                else:
                    raise e
                
        self.assertTrue(False, "Test failed or receiver client not disconnected")

if __name__ == '__main__':
    unittest.main()

