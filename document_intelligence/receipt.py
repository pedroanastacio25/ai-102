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
receipt_url=utils.AZURE_DOC_INTEL_RCT_URL

client=DocumentIntelligenceClient(endpoint=endpoint, credential=AzureKeyCredential(key))

response=client.begin_analyze_document("prebuilt-receipt", AnalyzeDocumentRequest(url_source=receipt_url))

result = response.result()

for index,receipt in enumerate(result.documents):
    print(f"Customer Name: {receipt.fields.get("MerchantName").get("valueString")}")
    print(f"Subtotal: {receipt.fields.get("Subtotal").get("content")}")
