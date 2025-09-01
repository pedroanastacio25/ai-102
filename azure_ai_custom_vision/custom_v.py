from msrest.authentication import ApiKeyCredentials
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import utils

endpoint=utils.AZURE_CUSTOM_VISION_ENDPOINT
key=utils.AZURE_CUSTOM_VISION_KEY

credentials = ApiKeyCredentials(in_headers={"Prediction-key": key})
prediction_client = CustomVisionPredictionClient(endpoint=endpoint, credentials=credentials)

image_data=open("img/customv/img-dog.jpg", mode="rb").read()

project_id="41ce5a3c-1773-4387-bdf2-364f69017aad"
published_name="custom-vision-model1"

response=prediction_client.classify_image(project_id, published_name, image_data)

for prediction in response.predictions:
    print(prediction)
