from azure.ai.language.conversations import ConversationAnalysisClient
from azure.core.credentials import AzureKeyCredential
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import utils

endpoint=utils.AZURE_LANGUAGE_ENDPOINT
key=utils.AZURE_LANGUAGE_KEY

## Conversation Language Understanding

client=ConversationAnalysisClient(endpoint,AzureKeyCredential(key))

project_name="TrainingProject"
deployment_name="TrainedDeployment"
utterance="I need a double room for me and my family for the weekend"

response=client.analyze_conversation(
    task={
        "kind": "Conversation",
        "analysisInput": {
            "conversationItem": {
                "participantId": "1",
                "id": "1",
                "modality": "text",
                "language": "en",
                "text": utterance
            },
            "isLoggingEnabled": False
        },
        "parameters": {
            "projectName": project_name,
            "deploymentName": deployment_name,
            "verbose": True
        }
    }
)

print(response)

# with client:
#     query = "Send an email to Carol about the tomorrow's demo"
#     result = client.analyze_conversation(
#         task={
#             "kind": "Conversation",
#             "analysisInput": {
#                 "conversationItem": {
#                     "participantId": "1",
#                     "id": "1",
#                     "modality": "text",
#                     "language": "en",
#                     "text": query
#                 },
#                 "isLoggingEnabled": False
#             },
#             "parameters": {
#                 "projectName": project_name,
#                 "deploymentName": deployment_name,
#                 "verbose": True
#             }
#         }
#     )

# # view result
# print("query: {}".format(result["result"]["query"]))
# print("project kind: {}\n".format(result["result"]["prediction"]["projectKind"]))

# print("top intent: {}".format(result["result"]["prediction"]["topIntent"]))
# print("category: {}".format(result["result"]["prediction"]["intents"][0]["category"]))
# print("confidence score: {}\n".format(result["result"]["prediction"]["intents"][0]["confidenceScore"]))

# print("entities:")
# for entity in result["result"]["prediction"]["entities"]:
#     print("\ncategory: {}".format(entity["category"]))
#     print("text: {}".format(entity["text"]))
#     print("confidence score: {}".format(entity["confidenceScore"]))
#     if "resolutions" in entity:
#         print("resolutions")
#         for resolution in entity["resolutions"]:
#             print("kind: {}".format(resolution["resolutionKind"]))
#             print("value: {}".format(resolution["value"]))
#     if "extraInformation" in entity:
#         print("extra info")
#         for data in entity["extraInformation"]:
#             print("kind: {}".format(data["extraInformationKind"]))
#             if data["extraInformationKind"] == "ListKey":
#                 print("key: {}".format(data["key"]))
#             if data["extraInformationKind"] == "EntitySubtype":
#                 print("value: {}".format(data["value"]))

