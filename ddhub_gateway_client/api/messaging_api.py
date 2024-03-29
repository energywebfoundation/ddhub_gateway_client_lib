"""
    DDHub Client Gateway

    DDHub Client Gateway  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from ddhub_gateway_client.api_client import ApiClient, Endpoint as _Endpoint
from ddhub_gateway_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from ddhub_gateway_client.model.get_messages_response_dto import GetMessagesResponseDto
from ddhub_gateway_client.model.send_message_dto import SendMessageDto
from ddhub_gateway_client.model.send_messagel_response_dto import SendMessagelResponseDto


class MessagingApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.message_controlller_create_endpoint = _Endpoint(
            settings={
                'response_type': (SendMessagelResponseDto,),
                'auth': [],
                'endpoint_path': '/api/v2/messages',
                'operation_id': 'message_controlller_create',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'send_message_dto',
                ],
                'required': [
                    'send_message_dto',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'send_message_dto':
                        (SendMessageDto,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'send_message_dto': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.message_controlller_download_message_endpoint = _Endpoint(
            settings={
                'response_type': (file_type,),
                'auth': [],
                'endpoint_path': '/api/v2/messages/download',
                'operation_id': 'message_controlller_download_message',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'file_id',
                ],
                'required': [
                    'file_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'file_id':
                        (str,),
                },
                'attribute_map': {
                    'file_id': 'fileId',
                },
                'location_map': {
                    'file_id': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'multipart/form-data'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.message_controlller_get_message_endpoint = _Endpoint(
            settings={
                'response_type': ([GetMessagesResponseDto],),
                'auth': [],
                'endpoint_path': '/api/v2/messages',
                'operation_id': 'message_controlller_get_message',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'fqcn',
                    '_from',
                    'amount',
                    'topic_name',
                    'topic_owner',
                    'client_id',
                ],
                'required': [
                    'fqcn',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'fqcn':
                        (str,),
                    '_from':
                        (str,),
                    'amount':
                        (int,),
                    'topic_name':
                        (str,),
                    'topic_owner':
                        (str,),
                    'client_id':
                        (str,),
                },
                'attribute_map': {
                    'fqcn': 'fqcn',
                    '_from': 'from',
                    'amount': 'amount',
                    'topic_name': 'topicName',
                    'topic_owner': 'topicOwner',
                    'client_id': 'clientId',
                },
                'location_map': {
                    'fqcn': 'query',
                    '_from': 'query',
                    'amount': 'query',
                    'topic_name': 'query',
                    'topic_owner': 'query',
                    'client_id': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.message_controlller_upload_file_endpoint = _Endpoint(
            settings={
                'response_type': (SendMessagelResponseDto,),
                'auth': [],
                'endpoint_path': '/api/v2/messages/upload',
                'operation_id': 'message_controlller_upload_file',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'file',
                    'fqcn',
                    'topic_name',
                    'topic_version',
                    'topic_owner',
                    'transaction_id',
                ],
                'required': [
                    'file',
                    'fqcn',
                    'topic_name',
                    'topic_version',
                    'topic_owner',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'file':
                        (file_type,),
                    'fqcn':
                        (str,),
                    'topic_name':
                        (str,),
                    'topic_version':
                        (str,),
                    'topic_owner':
                        (str,),
                    'transaction_id':
                        (str,),
                },
                'attribute_map': {
                    'file': 'file',
                    'fqcn': 'fqcn',
                    'topic_name': 'topicName',
                    'topic_version': 'topicVersion',
                    'topic_owner': 'topicOwner',
                    'transaction_id': 'transactionId',
                },
                'location_map': {
                    'file': 'form',
                    'fqcn': 'form',
                    'topic_name': 'form',
                    'topic_version': 'form',
                    'topic_owner': 'form',
                    'transaction_id': 'form',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'multipart/form-data'
                ]
            },
            api_client=api_client
        )

    def message_controlller_create(
        self,
        send_message_dto,
        **kwargs
    ):
        """message_controlller_create  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.message_controlller_create(send_message_dto, async_req=True)
        >>> result = thread.get()

        Args:
            send_message_dto (SendMessageDto):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            SendMessagelResponseDto
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['send_message_dto'] = \
            send_message_dto
        return self.message_controlller_create_endpoint.call_with_http_info(**kwargs)

    def message_controlller_download_message(
        self,
        file_id,
        **kwargs
    ):
        """message_controlller_download_message  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.message_controlller_download_message(file_id, async_req=True)
        >>> result = thread.get()

        Args:
            file_id (str): file Id for which file will be downloaded

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            file_type
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['file_id'] = \
            file_id
        return self.message_controlller_download_message_endpoint.call_with_http_info(**kwargs)

    def message_controlller_get_message(
        self,
        fqcn,
        **kwargs
    ):
        """message_controlller_get_message  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.message_controlller_get_message(fqcn, async_req=True)
        >>> result = thread.get()

        Args:
            fqcn (str): channel name

        Keyword Args:
            _from (str): date from which messages to be fetched. [optional]
            amount (int): Latest amount of messages to be fetched. [optional]
            topic_name (str): topic name. [optional]
            topic_owner (str): application namespace. [optional]
            client_id (str): cursor for pointing to messages. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            [GetMessagesResponseDto]
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['fqcn'] = \
            fqcn
        return self.message_controlller_get_message_endpoint.call_with_http_info(**kwargs)

    def message_controlller_upload_file(
        self,
        file,
        fqcn,
        topic_name,
        topic_version,
        topic_owner,
        **kwargs
    ):
        """message_controlller_upload_file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.message_controlller_upload_file(file, fqcn, topic_name, topic_version, topic_owner, async_req=True)
        >>> result = thread.get()

        Args:
            file (file_type): File uploaded
            fqcn (str): Channel Name
            topic_name (str): Topic name
            topic_version (str): Topic Version
            topic_owner (str): Topic Owner

        Keyword Args:
            transaction_id (str): Transaction Id used to check Idempotency. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            SendMessagelResponseDto
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['file'] = \
            file
        kwargs['fqcn'] = \
            fqcn
        kwargs['topic_name'] = \
            topic_name
        kwargs['topic_version'] = \
            topic_version
        kwargs['topic_owner'] = \
            topic_owner
        return self.message_controlller_upload_file_endpoint.call_with_http_info(**kwargs)

