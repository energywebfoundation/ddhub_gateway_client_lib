"""
This file contains different settings needed for test scenarios.

"""

did_01 = "did:ethr:volta:0x552761011ea5b332605Bc1Cc2020A4a4f8C738CD"
did_02 = "did:ethr:volta:0x0071B74b13601d0cbA9191cbA97DA7fb6A1DbDdC"
did_03 = "did:ethr:volta:0xaCE22e57dc9aCD1E21Bc2C746D76ad6F7c137088"
did_04 = "did:ethr:volta:0x08d911877D3C24f343f4b2346C1C2cF8bFfE6E4D"
did_05 = "did:ethr:volta:0x3dDDB5aF30d72695a53ec230E7F53dAc1C18a657"


topic_1 = {
            "name": "topic.nf.test.jsd7",
            "schemaType": "JSD7",
            "schema": "{\"type\":\"object\",\"properties\":{\"data\":{\"type\":\"number\"}}}",
            "version": "1.0.0",
            "owner": "ddhub.apps.energyweb.iam.ewc",
            "tags": [
                "nonfunctionalTesting", "jsd7"
            ]
        }

topic_2 = {
            "name": "topic.nf.test.csv",
            "schemaType": "CSV",
            "schema": "{\"type\":\"object\",\"properties\":{\"data\":{\"type\":\"number\"}}}",
            "version": "1.0.0",
            "owner": "ddhub.apps.energyweb.iam.ewc",
            "tags": [
                "nonfunctionalTesting", "csv"
            ]
        }

channel_1 = {
                "fqcn": "channel.pub.nf.test.001",
                "payloadEncryption": True,
                "type": "pub",
                "conditions": {
                    "dids": [
                    "did:ethr:volta:0x0071B74b13601d0cbA9191cbA97DA7fb6A1DbDdC",
                "did:ethr:volta:0xaCE22e57dc9aCD1E21Bc2C746D76ad6F7c137088",
                "did:ethr:volta:0x08d911877D3C24f343f4b2346C1C2cF8bFfE6E4D",
                "did:ethr:volta:0x3dDDB5aF30d72695a53ec230E7F53dAc1C18a657"
                    ],
                    "topics": [
                    {
                        "topicName": "topic.nonfunctional.testing.jsd7",
                        "owner": "ddhub.apps.energyweb.iam.ewc"
                    }
                    ]
                }
            }

channel_2 = {
                "fqcn": "channel.pub.nf.test.002",
                "payloadEncryption": True,
                "type": "pub",
                "conditions": {
                    "dids": [
                    "did:ethr:volta:0x0071B74b13601d0cbA9191cbA97DA7fb6A1DbDdC",
                "did:ethr:volta:0xaCE22e57dc9aCD1E21Bc2C746D76ad6F7c137088",
                "did:ethr:volta:0x08d911877D3C24f343f4b2346C1C2cF8bFfE6E4D",
                "did:ethr:volta:0x3dDDB5aF30d72695a53ec230E7F53dAc1C18a657"
                    ],
                    "topics": [
                    {
                        "topicName": "topic.nonfunctional.testing.jsd7",
                        "owner": "ddhub.apps.energyweb.iam.ewc"
                    }
                    ]
                }
            }

sub_channel = {
                "fqcn": "channel.sub.nftesting.001",
                "payloadEncryption": true,
                "type": "sub",
                "conditions": {
                    "dids": [
                    "did:ethr:volta:0x552761011ea5b332605Bc1Cc2020A4a4f8C738CD"
                    ],
                    "topics": [
                    {
                        "topicName": "topic.nonfunctional.testing.jsd7",
                        "owner": "ddhub.apps.energyweb.iam.ewc"
                    }
                    ]
                }
            }
