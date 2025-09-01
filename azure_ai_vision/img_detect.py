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

test_image_detect="img/set-of-fruits.jpg"

client=ImageAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))

# Image Detection
with open(test_image_detect, "rb") as image_detect:
    image_details_detect=image_detect.read()

response_detect=client.analyze(
    image_data=image_details_detect,
    visual_features=[VisualFeatures.OBJECTS]
)

print(json.dumps(response_detect.as_dict(), indent=4))
