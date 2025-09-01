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

test_image="img/images.jpg"

client=ImageAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))

# Image TAGS and Captions
with open(test_image, "rb") as image_file:
    image_details=image_file.read()

response=client.analyze(
    image_data=image_details,
    visual_features=[VisualFeatures.TAGS, VisualFeatures.CAPTION]
)

print(json.dumps(response.as_dict(), indent=4))
