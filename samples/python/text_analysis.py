from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

credential = AzureKeyCredential("<sua-chave>")
client = TextAnalyticsClient(endpoint="<seu-endpoint>", credential=credential)

documents = ["O serviço foi excelente, mas o quarto estava sujo."]
response = client.analyze_sentiment(documents=documents)

for doc in response:
    print(f"Sentimento geral: {doc.sentiment}")
    print(f"Pontuação: Positivo={doc.confidence_scores.positive:.2f}")
