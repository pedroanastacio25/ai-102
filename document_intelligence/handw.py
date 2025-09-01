from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from azure.ai.documentintelligence.models import AnalyzeResult
from azure.core.credentials import AzureKeyCredential
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import utils

endpoint=utils.AZURE_DOC_INTEL_ENDPOINT
key=utils.AZURE_DOC_INTEL_KEY
document_url=utils.AZURE_DOC_INTEL_HANDW_URL

client=DocumentIntelligenceClient(endpoint=endpoint, credential=AzureKeyCredential(key))

response=client.begin_classify_document("prebuilt-read", AnalyzeDocumentRequest(url_source=document_url))

result: AnalyzeResult = response.result()

for style in result.styles:
    if style.is_handwritten==True:
        print(f"Handwritten text, Confidence: {style.confidence}")

for index,para in enumerate(result.paragraphs):
    print(f"Paragraph {index+1}: {para.content}")
