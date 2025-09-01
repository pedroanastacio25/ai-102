import azure.cognitiveservices.speech as speechsdk
from azure.core.credentials import AzureKeyCredential
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import utils

endpoint=utils.AZURE_AI_SERVICES_ENDPOINT
key=utils.AZURE_AI_SERVICES_KEY

config=speechsdk.SpeechConfig(subscription=key, endpoint=endpoint)

output_file="transcribed.txt"
audio_filename="speech01.wav"
config.speech_recognition_language="en-US"

## From audio file
#audio_input=speechsdk.AudioConfig(filename=audio_filename)

## From microphone
audio_input=speechsdk.audio.AudioConfig(use_default_microphone=True)

txt_generator=speechsdk.SpeechRecognizer(speech_config=config, audio_config=audio_input)

result=txt_generator.recognize_once_async().get()
if result.reason== speechsdk.ResultReason.RecognizedSpeech:
    print("Successfully generated text")
else:
    print("Generating text failed")

with open(output_file, "w", encoding="utf-8") as file:
    file.write(result.text)
