from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import utils

endpoint=utils.AZURE_LANGUAGE_ENDPOINT
key=utils.AZURE_LANGUAGE_KEY

## Extract Key Phrases

client=TextAnalyticsClient(endpoint=endpoint,credential=AzureKeyCredential(key))

documents=[
    "Machine learning and artificial intelligence are transforming industries such as healthcare, "
    "finance, and education by automating tasks and providing inshgts."
]

response=client.extract_key_phrases(documents=documents)[0].key_phrases

print(response)
