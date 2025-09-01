from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import utils

endpoint=utils.AZURE_LANGUAGE_ENDPOINT
key=utils.AZURE_LANGUAGE_KEY

# Language Detection

client=TextAnalyticsClient(endpoint=endpoint,credential=AzureKeyCredential(key))

documents=[
    "Me gusta aprender nuevos idiomas.",
    "Comment allez-vous ce matin?"
]

response=client.detect_language(documents=documents)

print(response)
