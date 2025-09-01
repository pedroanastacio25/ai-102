from azure.ai.translation.text import TextTranslationClient, TranslatorCredential
from azure.ai.translation.text.models import InputTextItem
from azure.core.credentials import AzureKeyCredential
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import utils

endpoint=utils.AZURE_TRANSLATOR_ENDPOINT_TXT_TRANSLATION
key=utils.AZURE_TRANSLATOR_KEY
region=utils.AZURE_TRANSLATOR_REGION

## Text Translation

credential=TranslatorCredential(key, region)
client=TextTranslationClient(endpoint=endpoint,credential=credential)

source_lang="en"
target_lang=["it"]

input_text="I like to learn new languages."

documents=[
    InputTextItem(text=input_text)
]

response=client.translate(content=documents, to=target_lang, from_parameter=source_lang)

print(f"Translated text:{response[0].translations}")
