"""
    DDHub Client Gateway

    DDHub Client Gateway  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import sys
from this import s
from unicodedata import name
import unittest

import ddhub_gateway_client
from ddhub_gateway_client.model.topic_dto import TopicDto
globals()['TopicDto'] = TopicDto
from ddhub_gateway_client.model.channel_conditions_dto import ChannelConditionsDto


class TestChannelConditionsDto(unittest.TestCase):
    """ChannelConditionsDto unit test stubs"""

    def setUp(self):
        self.topic_dto = TopicDto(
            topic_name="Topic_JSON_test_py",
            owner="testing01.apps.aemotest.iam.ewc",
        )
        pass

    def tearDown(self):
        pass

    def testChannelConditionsDto(self):
        with self.assertRaises(TypeError):
            model = ChannelConditionsDto(
                dids = [
                    "did:ethr:volta:0x552761011ea5b332605Bc1Cc2020A4a4f8C738CD"
                ],
                # roles=[
                #     "topiccreator",
                #     "user"
                # ],
                topics=[
                    self.topic_dto
                ]
                )  # noqa: E501


if __name__ == '__main__':
    unittest.main()