# .sap-ai-pr-review/review.py

import os
import requests
from openai import AzureOpenAI

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
PR_DIFF = os.getenv("PR_DIFF")
PR_NUMBER = os.getenv("PR_NUMBER")
REPO = os.getenv("GITHUB_REPOSITORY")

# Azure OpenAI config
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version="2025-01-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

# Envia o diff pro modelo
response = client.chat.completions.create(
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),  # ex: "gpt-35-turbo"
    messages=[
        {"role": "system", "content": "Você é um revisor de código especialista. Faça sugestões para melhorar o código abaixo."},
        {"role": "user", "content": f"Aqui está o diff do PR:\n{PR_DIFF}"}
    ],
    temperature=0.3
)

review = response.choices[0].message.content

# Comenta no PR
url = f"https://api.github.com/repos/{REPO}/issues/{PR_NUMBER}/comments"
headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}
requests.post(url, headers=headers, json={"body": review})
