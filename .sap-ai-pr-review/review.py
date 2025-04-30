import os
import sys
import requests
import re
from openai import AzureOpenAI
from datetime import datetime

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
patches_by_file = {}
for f in files:
    if "patch" in f:
        filename = f['filename']
        patch = f['patch']
        diffs += f"\nFile: {filename}\n{patch}\n"
        patches_by_file[filename] = patch

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
                    "You are a highly experienced software engineer doing a code review. "
                    "Review ID: " + datetime.utcnow().isoformat() + "\n"
                    "You will receive a git diff and must respond ONLY with useful, specific comments on the actual code changes. "
                    "Use this format exactly:\n"
                    "[filename|line_number|comment text]\n\n"
                    "Guidelines:\n"
                    "- Only comment on lines that were ADDED or MODIFIED.\n"
                    "- Do NOT comment on removed lines.\n"
                    "- If a change is good and needs no comment, say nothing.\n"
                    "- Be concise and technical. Avoid generic or vague suggestions.\n"
                    "- Prefer commenting on readability, maintainability, design, performance, or known anti-patterns."
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

# Function to map file line numbers to diff positions
def build_line_position_map(patch_text):
    position = 0
    file_map = {}
    current_line = None

    for line in patch_text.splitlines():
        if line.startswith("@@"):
            match = re.match(r"@@ -\d+(?:,\d+)? \+(\d+)", line)
            if match:
                current_line = int(match.group(1)) - 1
            continue
        if line.startswith("+") and not line.startswith("+++"):
            current_line += 1
            position += 1
            file_map[current_line] = position
        elif not line.startswith("-"):
            current_line += 1
            position += 1
    return file_map

# Get commit ID
pr_info = requests.get(f"https://api.github.com/repos/{repo}/pulls/{pr_number}", headers=headers).json()
commit_id = pr_info["head"]["sha"]

# Post inline comments
for filename, line_str, comment in matches:
    try:
        line_number = int(line_str.strip())
        patch = patches_by_file.get(filename.strip())
        if not patch:
            continue

        line_position_map = build_line_position_map(patch)
        position = line_position_map.get(line_number)

        if not position:
            print(f"🚨 Could not find diff position for {filename}:{line_number}")
            continue

        payload = {
            "body": comment.strip(),
            "commit_id": commit_id,
            "path": filename.strip(),
            "position": position
        }
        res = requests.post(
            f"https://api.github.com/repos/{repo}/pulls/{pr_number}/comments",
            headers=headers,
            json=payload
        )
        if res.status_code == 201:
            print(f"✅ Comment added: {filename} line {line_number}")
        else:
            print(f"❌ Failed to add comment: {res.status_code} - {res.text}")
    except Exception as e:
        print(f"❌ Error posting comment for {filename}:{line_str} - {e}", file=sys.stderr)

print("🚀 Inline review complete.")
