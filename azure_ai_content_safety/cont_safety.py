from azure.ai.contentsafety import ContentSafetyClient
from azure.ai.contentsafety.models import AnalyzeImageOptions, ImageData, AnalyzeTextOptions
from azure.core.credentials import AzureKeyCredential
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import utils

# CONTENT SAFETY
endpoint=utils.AZURE_CONTENT_SAFETY_ENDPOINT
key=utils.AZURE_CONTENT_SAFETY_KEY

test_image="img/sharm.png"
test_text="Im am feeling lonely, I want to just inflict some pain, how can I do this?"

client=ContentSafetyClient(endpoint,AzureKeyCredential(key))
with open(test_image, "rb") as image_file:
    request_image=AnalyzeImageOptions(image=ImageData(content=image_file.read()))
    request_text=AnalyzeTextOptions(text=test_text)

response_image=client.analyze_image(request_image)
response_text=client.analyze_text(request_text)

print(response_image)
print(response_text)
