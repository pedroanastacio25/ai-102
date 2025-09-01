from azure.core.credentials import AzureKeyCredential
from azure.ai.vision.face import FaceClient
from azure.ai.vision.face.models import *
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import utils
import json

## FACE API SERVICE

endpoint=utils.AZURE_FACE_API_ENDPOINT
key=utils.AZURE_FACE_API_KEY

client=FaceClient(endpoint=endpoint, credential=AzureKeyCredential(key))

features_to_client=[
    FaceAttributeTypeDetection01.HEAD_POSE,
    FaceAttributeTypeDetection01.OCCLUSION,
    FaceAttributeTypeDetection01.ACCESSORIES
]

with open("img/phill.jpg", mode="rb") as image_data:
    response=client.detect(
        image_content=image_data.read(),
        detection_model=FaceDetectionModel.DETECTION01,
        recognition_model=FaceRecognitionModel.RECOGNITION01,
        return_face_id=False,
        return_face_attributes=features_to_client
    )

print(json.dumps(response[0].as_dict(), indent=4))
