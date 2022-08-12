## Usage Examples

  These scripts showcase some of the functionality the Library offers.

### New private key sign up.

  In order to use the DDHub client gateway, the user must provide a private key and enroll to the default role.
[signup_script.py](examples/signup_script.py) is an example of a private key sign up.

  _Note: the role enrollment should be approved to be able to use DDHub._

### Topic creation

  To create a Topic the DID used must enroll to the `topiccreator` role of the owner app.
  The Topic's fields are described [here](docs/PostTopicBodyDto.md).

  ```python
  import json
  import ddhub_gateway_client
  from ddhub_gateway_client.model.post_topic_body_dto import PostTopicBodyDto

  example_topic:PostTopicBodyDto = PostTopicBodyDto(
    name="topic_name",
    schema_type="JSD7",
    schema=json.dumps({
        'type': 'object',
        'properties': {
            'data': {
                'type': 'integer'
            },
        },
        'required':['data',]
    }),
    version="0.0.1",
    owner="owner.apps.energyweb.iam.ewc",
    tags=['test_tag']
  )

  with ddhub_gateway_client.ApiClient(configuration) as api_client:
  
    topics_api = ddhub_gateway_client.api.topics_api.TopicsApi(api_client)
  
    topics_api.topics_controller_post_topics(example_topic)
  ```

### Channel creation

  To publish or subscribe to the channel channel conditions must be set

  ```python
  channel_conditions:ChannelConditionsDto = ChannelConditionsDto(
    dids=["did:ethr:volta:0x552761011ea5b332605Bc1Cc2020A4a4f8C738CD"],
    roles=['role.roles.owner.apps.energyweb.iam.ewc'],
    topics=[TopicDto("topic_name", "owner.apps.energyweb.iam.ewc")]
  )
  ```

  Channel fields are described [here](docs/CreateChannelDto.md).

  ```python
  example_publisher_channel:CreateChannelDto=CreateChannelDto(
    fqcn='example.lib.pub.channel',
    payload_encryption=True,
    type='pub',
    conditions=channel_conditions
  )
  with ddhub_gateway_client.ApiClient(configuration) as api_client:
    
    channel_api = ChannelsApi(api_client)
    
    channel_api.channel_controller_create(example_publisher_channel)
  ```
  _Note: topics in Channel Conditions should be registered topics_

  [Create_channel.py](examples/create_channel.py) creates Topic and a Channel.

  ### Messaging

  To send and receive messages, `pub` and `sub` channels are required. Both channels should implement the same Topic.
  
  * Sending messages:
  
  ```python
  message:SendMessageDto = SendMessageDto(
    fqcn='example.lib.pub.channel',
    topic_name='topic_name',
    topic_version='0.0.1',
    topic_owner='owner.apps.energyweb.iam.ewc',
    transaction_id='unique_string',
    payload=json.dumps({'data':1})
  )
  with ddhub_gateway_client.ApiClient(configuration) as api_client:
    
    messaging_api = MessagingApi(api_client)
    
    messaging_api.message_controlller_create(message)
  ```
  
  * Reading messages:
  ```python
  with ddhub_gateway_client.ApiClient(configuration) as api_client:
    
    messaging_api = MessagingApi(api_client)
    
    messages = []
    messages = messaging_api.message_controlller_get_message("example.lib.sub.channel")
  ```

  To upload or a download a file, channels must be of type `upload` and `download`, schema type of Topic must be `CSV` and `schema='{}'`.

  * Upload a file:
  ```python
  with ddhub_gateway_client.ApiClient(configuration) as api_client:
    
    messaging_api = MessagingApi(api_client)
    
    file = open('path/to/file.csv', 'rb') 
    messaging_api.message_controlller_upload_file(
            file=file,
            fqcn='example.lib.upload.channel',
            topic_name='example_file_topic',
            topic_version='0.0.1',
            topic_owner='owner.apps.energyweb.iam.ewc'
    )
  ```

  * Download a file

  Downloading a file requires the file ID. It is contained in the message payload.
  ```python
  with ddhub_gateway_client.ApiClient(configuration) as api_client:

    messaging_api = MessagingApi(api_client)

    messages=messaging_api.message_controlller_get_message('example.lib.download.channel')
    last_message:GetMessagesResponseDto = messages[0]
    file_id = json.loads(last_message.payload)['fileId']

    messaging_api.message_controlller_download_message(file_id)
  ```
