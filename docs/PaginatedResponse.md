# PaginatedResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | total number of channels | 
**records** | [**[GetTopicDto]**](GetTopicDto.md) | Topics records | 
**limit** | **int** | limit of channels | [optional]  if omitted the server will use the default value of 5
**page** | **int** |  | [optional]  if omitted the server will use the default value of 1
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


