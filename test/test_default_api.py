"""
    DDHub Client Gateway

    DDHub Client Gateway  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import ddhub_gateway_client
from ddhub_gateway_client.api.default_api import DefaultApi
from ddhub_gateway_client.model.cron_response_dto import CronResponseDto  # noqa: E501


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""
    configuration = ddhub_gateway_client.Configuration(
        host = "https://ddhub-gateway-dev.energyweb.org"
    )

    def setUp(self):
        self.api_client = ddhub_gateway_client.ApiClient(self.configuration)
        self.api_instance =  DefaultApi(self.api_client)

    def tearDown(self):
        self.api_client.close()

    def test_cron_controller_get_jobs_results(self):
        """Test case for cron_controller_get_jobs_results

        """
        api_response_body, api_response_status, api_response_headers = \
            self.api_instance.cron_controller_get_jobs_results(
                _return_http_data_only=False
            )
        
        self.assertEqual(200,api_response_status)

        self.assertIsInstance(api_response_body, (list,CronResponseDto))


if __name__ == '__main__':
    unittest.main()
