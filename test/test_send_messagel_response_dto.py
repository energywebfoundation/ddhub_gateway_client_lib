"""
    DDHub Client Gateway

    DDHub Client Gateway  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ddhub_gateway_client
from ddhub_gateway_client.model.recipients import Recipients
from ddhub_gateway_client.model.status import Status
globals()['Recipients'] = Recipients
globals()['Status'] = Status
from ddhub_gateway_client.model.send_messagel_response_dto import SendMessagelResponseDto


class TestSendMessagelResponseDto(unittest.TestCase):
    """SendMessagelResponseDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSendMessagelResponseDto(self):
        """Test SendMessagelResponseDto"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SendMessagelResponseDto()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()