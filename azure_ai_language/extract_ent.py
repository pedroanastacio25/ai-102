from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import utils

endpoint=utils.AZURE_LANGUAGE_ENDPOINT
key=utils.AZURE_LANGUAGE_KEY

## Extract Entities

client=TextAnalyticsClient(endpoint=endpoint,credential=AzureKeyCredential(key))

documents=[
    "Satya Nadella annouced at Microsoft's headquarters in Redmond that the company's revenue for the fourth quarter was 46$ billion."
]

response=client.recognize_entities(documents=documents)[0]

for entity in response.entities:
    print(f"Category: {entity.category} - Text: {entity.text}")
