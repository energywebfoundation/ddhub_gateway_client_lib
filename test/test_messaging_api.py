"""
    DDHub Client Gateway

    DDHub Client Gateway  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import ddhub_gateway_client
from ddhub_gateway_client.api.messaging_api import MessagingApi  # noqa: E501


class TestMessagingApi(unittest.TestCase):
    """MessagingApi unit test stubs"""

    def setUp(self):
        self.api = MessagingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_message_controlller_create(self):
        """Test case for message_controlller_create

        """
        pass

    def test_message_controlller_download_message(self):
        """Test case for message_controlller_download_message

        """
        pass

    def test_message_controlller_get_message(self):
        """Test case for message_controlller_get_message

        """
        pass

    def test_message_controlller_upload_file(self):
        """Test case for message_controlller_upload_file

        """
        pass


if __name__ == '__main__':
    unittest.main()