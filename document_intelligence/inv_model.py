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
invoice_url=utils.AZURE_DOC_INTEL_INV_URL

client=DocumentIntelligenceClient(endpoint=endpoint, credential=AzureKeyCredential(key))

response=client.begin_analyze_document("prebuilt-invoice", AnalyzeDocumentRequest(url_source=invoice_url))

result = response.result()

for index,invoice in enumerate(result.documents):
    print(f"Customer Name: {invoice.fields.get("CustomerName").get("valueString")}")
    print(f"Invoice ID: {invoice.fields.get("InvoiceId").get("valueString")}")
