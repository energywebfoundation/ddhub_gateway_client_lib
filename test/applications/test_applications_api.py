"""
    DDHub Client Gateway

    DDHub Client Gateway  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import ddhub_gateway_client
from ddhub_gateway_client.api.applications_api import ApplicationsApi
from ddhub_gateway_client.exceptions import ApiException
from ddhub_gateway_client.model.application_dto import ApplicationDTO  # noqa: E501


class TestApplicationsApi(unittest.TestCase):
    """ApplicationsApi unit test stubs"""
    configuration = ddhub_gateway_client.Configuration(
        host = "https://ddhub-gateway-dev.energyweb.org"
    )
    owner = "libtesting.apps.aresguerre.iam.ewc"
    role = "topiccreator"

    def setUp(self):
        self.api_client = ddhub_gateway_client.ApiClient(self.configuration)
        self.api_instance = ApplicationsApi(self.api_client)  # noqa: E501

    def tearDown(self):
        self.api_client.close()


    def test_applications_controller_get_applications_invalid(self):
        """Test case for applications_controller_get_applications

        """
        with self.assertRaises(TypeError):
            api_response = \
                self.api_instance.applications_controller_get_applications()

    def test_applications_controller_get_applications_empty_role(self):
        """Test case for applications_controller_get_applications

        """
        with self.assertRaises(ApiException):
            api_response = \
                self.api_instance.applications_controller_get_applications("")

    def test_applications_controller_get_applications(self):
        """Test case for applications_controller_get_applications

        """
        api_response_body, api_response_status, api_response_headers = \
            self.api_instance.applications_controller_get_applications(
                self.role,
                _return_http_data_only=False)

        self.assertEqual(200,api_response_status)

        self.assertIsInstance(api_response_body, (list,ApplicationDTO))
        

    def test_applications_controller_get_applications_by_namespace_invalid(self):
        """Test case for applications_controller_get_applications

        """
        with self.assertRaises(TypeError):
            api_response = \
                self.api_instance.applications_controller_get_applications_by_namespace()

    def test_applications_controller_get_applications_by_namespace_empty_role(self):
        """Test case for applications_controller_get_applications

        """
        with self.assertRaises(ApiException):
            api_response = \
                self.api_instance.applications_controller_get_applications_by_namespace("")

    def test_applications_controller_get_applications_by_namespace(self):
        """Test case for applications_controller_get_applications_by_namespace

        """
        api_response_body, api_response_status, api_response_headers = \
            self.api_instance.applications_controller_get_applications_by_namespace(
                self.owner,
                _return_http_data_only=False)
        

        self.assertEqual(200,api_response_status)

        self.assertIsInstance(api_response_body, (list,ApplicationDTO))


if __name__ == '__main__':
    unittest.main()