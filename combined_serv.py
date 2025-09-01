from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.textanalytics import TextAnalyticsClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from azure.ai.documentintelligence.models import AnalyzeResult
from azure.core.credentials import AzureKeyCredential
import utils

endpoint=utils.AZURE_DOC_INTEL_ENDPOINT
key=utils.AZURE_DOC_INTEL_KEY
document_url=utils.AZURE_DOC_INTEL_DOC_MIX_URL

lang_endpoint=utils.AZURE_LANGUAGE_ENDPOINT
lang_key=utils.AZURE_LANGUAGE_KEY

client=DocumentIntelligenceClient(endpoint=endpoint, credential=AzureKeyCredential(key))
lang_client=TextAnalyticsClient(endpoint=lang_endpoint,credential=AzureKeyCredential(lang_key))

docintel_response=client.begin_analyze_document("prebuilt-read", AnalyzeDocumentRequest(url_source=document_url))

result: AnalyzeResult = docintel_response.result()

documents=[]

for each_page in result.pages:
    for index,line in enumerate(each_page.lines):
        documents.append(line.content)

sentiment_response=lang_client.analyze_sentiment(documents=documents)

for result in sentiment_response:
    print(f"Sentiment: {result.sentences[0].sentiment} - Sentence: {result.sentences[0].text}")