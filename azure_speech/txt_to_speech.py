import azure.cognitiveservices.speech as speechsdk
from azure.core.credentials import AzureKeyCredential
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import utils

endpoint=utils.AZURE_AI_SERVICES_ENDPOINT
key=utils.AZURE_AI_SERVICES_KEY

config=speechsdk.SpeechConfig(subscription=key, endpoint=endpoint)
# config.speech_synthesis_voice_name="en-US-SteffanMultilingualNeural"

# input_text="Machine learning is a branch of artificial intelligence (AI) that focuses on building systems that can learn from data and improve over time without being explicitly programmed."

output_file="speech01.wav"
audio_output=speechsdk.audio.AudioConfig(filename=output_file)

speech_generator=speechsdk.SpeechSynthesizer(speech_config=config, audio_config=audio_output)

# from config.xml
with open("azure_speech\config.xml", "r", encoding="utf-8") as file:
    ssml_string = file.read()

# result=speech_generator.speak_text_async(input_text).get()
result=speech_generator.speak_ssml_async(ssml_string).get()
if result.reason== speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Successfully generated speech")
else:
    print("Generating speech failed")
