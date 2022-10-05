"""
    DDHub Client Gateway

    DDHub Client Gateway  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""

import sys
from time import time, sleep
import unittest
import json
import pprint 
import random, string

import ddhub_gateway_client
from ddhub_gateway_client.api.messaging_api import MessagingApi
from ddhub_gateway_client.api.topics_api import TopicsApi
from ddhub_gateway_client.api.channels_api import ChannelsApi  # noqa: E501

from ddhub_gateway_client.models import ChannelConditionsDto, UpdateChannelDto, TopicDto, PostTopicBodyDto, SendMessageDto

def random_string(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

# raw_input returns the empty string for "enter"
yes = {'yes','y', 'ye', ''}
no = {'no','n'}

pp = pprint.PrettyPrinter(indent=4)

class DHNf003(unittest.TestCase):
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

        self.api_client = ddhub_gateway_client.ApiClient(self.configuration)
        
        self.api = MessagingApi(ddhub_gateway_client.ApiClient(self.configuration))
        self.api_instance = MessagingApi(self.api_client)  # noqa: E501
        
        self.topics_api = TopicsApi(ddhub_gateway_client.ApiClient(self.configuration))
        self.topics_api_instance = TopicsApi(self.api_client)  # noqa: E501   
        
        self.channels_api = ChannelsApi(ddhub_gateway_client.ApiClient(self.configuration))
        self.channels_api_instance = ChannelsApi(self.api_client)  # noqa: E501
             
        print("Connecting to: " + self.configuration.host)
        
        self.post_topic_dto = PostTopicBodyDto(
            name= "topic.nf.testcase.003",
            schema_type= "JSD7",
            schema= "{\"type\":\"object\",\"properties\":{\"data\":{\"type\":\"number\"}}}",
            version= "1.0.0",
            owner= "ddhub.apps.energyweb.iam.ewc",
            tags= [
                "nonfunctionalTesting", "jsd7"
            ]
        )
        
        try:
            print("Trying to create topic " + self.post_topic_dto.name)
            api_response_body, api_response_status, api_response_headers = \
                self.topics_api_instance.topics_controller_post_topics(self.post_topic_dto,
                                                                    _return_http_data_only=False)
            self.topic_id = api_response_body.id                                              
            print("Topic created with id: " + self.topic_id)
            
        except ddhub_gateway_client.ApiException as e:
            api_response_body, api_response_status, api_response_headers = \
                self.topics_api_instance.topics_controller_get_topics_by_search( keyword=self.post_topic_dto.name,
                                                                            _return_http_data_only=False)
            
            self.topic_id = api_response_body['records'][0]['id']
            print("Topic already exists with id: " + self.topic_id)
        
        
            
        topic_dto = TopicDto(
            topic_name= "topic.nf.testcase.003",
            owner= "ddhub.apps.energyweb.iam.ewc",
        )

        ucdto = UpdateChannelDto(
            type="pub",
            payload_encryption=False,
            conditions=ChannelConditionsDto(
                dids=["did:ethr:volta:0x0071B74b13601d0cbA9191cbA97DA7fb6A1DbDdC", "did:ethr:volta:0x552761011ea5b332605Bc1Cc2020A4a4f8C738CD"],
                roles=[],
                topics=[ topic_dto ],
            )
        )

        response_body, response_status, response_headers = \
        self.channels_api_instance.channel_controller_update(
            fqcn="channel.pub.nf.test.001",
            update_channel_dto=ucdto,
            _return_http_data_only=False
        )
        print("Channel updated", response_body)

    def tearDown(self):
        self.api_client.close()        
        

    def test_nf_003(self):
        """Test case for nf_001
        """


        for i in range(1,120):
            try:
                sleep(5)
                send_message_dto = SendMessageDto(
                                        fqcn="channel.pub.nf.test.001",
                                        topic_name= "topic.nf.testcase.003",
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
                    print("***************************\n*  Deleting the topic  *\n***************************")
                    api_response_body, api_response_status, api_response_headers = \
                        self.topics_api_instance.topics_controller_delete_topics(self.topic_id,
                                                                            _return_http_data_only=False)
                    print(api_response_body)

            except Exception as e:
                print(e)
                if i > 12 and i < 120:
                    print("Exception:", str(e))
                    self.assertTrue(True)
                    return
                else:
                    raise e
                    
        self.assertTrue(False, "Test failed")
        

if __name__ == '__main__':
    unittest.main()
