# GetMessagesResponseDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | message id | 
**topic_name** | **str** | topic Name | 
**topic_owner** | **str** | application namespace | 
**topic_version** | **str** | Topic Version | 
**topic_schema_type** | **str** | schema type of the topic | 
**payload** | **str** | Payload sent to message | 
**signature** | **str** | signature sent to message | 
**sender** | **str** | message sender | 
**timestamp_nanos** | **float** | timestamp in nano seconds | 
**transaction_id** | **str** | transactionId sent to message for idempotency | 
**signature_valid** | **str** | Encryption status for a message | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


