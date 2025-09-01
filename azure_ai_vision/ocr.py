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

endpoint=utils.AZURE_COMPUTER_VISION_ENDPOINT
key=utils.AZURE_COMPUTER_VISION_KEY

test_image_ocr="img/quote.jpg"

client=ImageAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))
computer_vision_client=ComputerVisionClient(endpoint, CognitiveServicesCredentials(key))
features = [VisualFeatureTypes.brands]

# Optical Character Recognition (OCR)
with open(test_image_ocr, "rb") as image_ocr:
    image_details_ocr=image_ocr.read()

response_ocr=client.analyze(
    image_data=image_details_ocr,
    visual_features=[VisualFeatures.READ]
)

# print(json.dumps(response_ocr.as_dict(), indent=4))
for line in response_ocr.read.blocks[0].lines:
    print(f"{line.text}")
