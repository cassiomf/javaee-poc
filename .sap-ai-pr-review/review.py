import os
import sys
import requests
import re
from openai import AzureOpenAI

# Validate required env vars
required_envs = [
    "GITHUB_TOKEN", "PR_NUMBER", "GITHUB_REPOSITORY",
    "AZURE_OPENAI_KEY", "AZURE_OPENAI_ENDPOINT", "AZURE_OPENAI_DEPLOYMENT"
]
missing = [env for env in required_envs if not os.getenv(env)]
if missing:
    print(f"❌ Missing environment variables: {', '.join(missing)}", file=sys.stderr)
    sys.exit(1)

# Read env vars
token = os.getenv("GITHUB_TOKEN")
repo = os.getenv("GITHUB_REPOSITORY")
pr_number = os.getenv("PR_NUMBER")

# Azure OpenAI client
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version="2025-01-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

# Fetch PR files and their diffs
headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github.v3+json"
}
files_url = f"https://api.github.com/repos/{repo}/pulls/{pr_number}/files"
files_resp = requests.get(files_url, headers=headers)
if files_resp.status_code != 200:
    print(f"❌ Failed to fetch PR files: {files_resp.status_code} - {files_resp.text}", file=sys.stderr)
    sys.exit(1)
files = files_resp.json()

# Combine all patches
diffs = ""
for f in files:
    if "patch" in f:
        diffs += f"\nFile: {f['filename']}\n{f['patch']}\n"

if not diffs.strip():
    print("⚠️ No diffs to analyze.")
    sys.exit(0)

# Send diffs to OpenAI
try:
    response = client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a code review bot. Analyze the diff and respond only with suggestions in the following format:\n"
                    "[filename|line_number|comment text]\n"
                    "Only suggest improvements for lines that were added or changed."
                )
            },
            {
                "role": "user",
                "content": diffs
            }
        ],
        temperature=0.3
    )
    suggestions = response.choices[0].message.content.strip()
except Exception as e:
    print(f"❌ Failed to generate review: {e}", file=sys.stderr)
    sys.exit(1)

# Parse responses like [file.py|4|Something could be improved here.]
pattern = re.compile(r"\[(.+?)\|(\d+)\|(.+?)\]", re.DOTALL)
matches = pattern.findall(suggestions)

if not matches:
    print("🤖 No actionable review suggestions.")
    sys.exit(0)

# Get commit ID
pr_info = requests.get(f"https://api.github.com/repos/{repo}/pulls/{pr_number}", headers=headers).json()
commit_id = pr_info["head"]["sha"]

# Post inline comments
for filename, position, comment in matches:
    payload = {
        "body": comment.strip(),
        "commit_id": commit_id,
        "path": filename.strip(),
        "position": int(position.strip())  # position refers to line index in the diff
    }
    res = requests.post(
        f"https://api.github.com/repos/{repo}/pulls/{pr_number}/comments",
        headers=headers,
        json=payload
    )
    if res.status_code == 201:
        print(f"✅ Comment added: {filename} line {position}")
    else:
        print(f"❌ Failed to add comment: {res.status_code} - {res.text}")

print("🚀 Inline review complete.")
