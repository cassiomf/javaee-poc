import os
import requests
from openai import AzureOpenAI
import sys

# Required environment variables
required_envs = [
    "GITHUB_TOKEN", "PR_DIFF", "PR_NUMBER", "GITHUB_REPOSITORY",
    "AZURE_OPENAI_KEY", "AZURE_OPENAI_ENDPOINT", "AZURE_OPENAI_DEPLOYMENT"
]

missing_envs = [env for env in required_envs if not os.getenv(env)]
if missing_envs:
    print(f"Error: Missing environment variables: {', '.join(missing_envs)}", file=sys.stderr)
    sys.exit(1)

# Read environment variables
github_token = os.getenv("GITHUB_TOKEN")
pr_diff = os.getenv("PR_DIFF")
pr_number = os.getenv("PR_NUMBER")
repo = os.getenv("GITHUB_REPOSITORY")

# Azure OpenAI configuration
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version="2025-01-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

try:
    # Send diff to the model
    response = client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        messages=[
            {
                "role": "system",
                "content": "You are a code review expert. Suggest improvements for the following code."
            },
            {
                "role": "user",
                "content": f"Here is the PR diff:\n{pr_diff}"
            }
        ],
        temperature=0.3
    )
    review = response.choices[0].message.content.strip()
except Exception as e:
    print(f"Error generating suggestions with Azure OpenAI: {e}", file=sys.stderr)
    sys.exit(1)

# Post comment on the PR
comment_url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"
headers = {
    "Authorization": f"Bearer {github_token}",
    "Accept": "application/vnd.github.v3+json"
}
response = requests.post(comment_url, headers=headers, json={"body": review})

if response.status_code != 201:
    print(f"Error posting comment on PR: {response.status_code} - {response.text}", file=sys.stderr)
    sys.exit(1)

print("✅ Review posted successfully!")
