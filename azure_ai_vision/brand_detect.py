from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import utils
import json

# COMPUTER VISION

endpoint=utils.AZURE_COMPUTER_VISION_ENDPOINT
key=utils.AZURE_COMPUTER_VISION_KEY

test_image_brand="img/brand-microsoft.png"

computer_vision_client=ComputerVisionClient(endpoint, CognitiveServicesCredentials(key))
features = [VisualFeatureTypes.brands]

## Brand Detection
with open(test_image_brand, "rb") as image_brand:
    response_brand= computer_vision_client.analyze_image_in_stream(image_brand, visual_features=features)

for brand in response_brand.brands:
    print(f"- {brand.name} (confidence: {brand.confidence:.2f}) at {brand.rectangle}")
