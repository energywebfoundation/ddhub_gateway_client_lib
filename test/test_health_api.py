"""
    DDHub Client Gateway

    DDHub Client Gateway  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import ddhub_gateway_client
from ddhub_gateway_client.api.health_api import HealthApi  # noqa: E501


class TestHealthApi(unittest.TestCase):
    """HealthApi unit test stubs"""

    def setUp(self):
        self.api = HealthApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_health_controller_check(self):
        """Test case for health_controller_check

        """
        pass


if __name__ == '__main__':
    unittest.main()
