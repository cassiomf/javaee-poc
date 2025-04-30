AI PR Review 🤖

This project is a Proof of Concept (PoC) that integrates [Azure OpenAI](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/) with GitHub Actions to automatically review Pull Requests using a language model.

## ✨ Features

- Analyzes diffs from Pull Requests.
- Sends the diff to Azure OpenAI for automated review suggestions.
- Posts comments directly in the Pull Request.
- Runs code validation checks to ensure code quality and safety.

## 🧠 How it works

1. The GitHub Actions workflow is triggered on `pull_request` events.
2. The PR diff is extracted and sent to Azure OpenAI using the Chat Completion API.
3. AI-generated suggestions are posted as comments in the PR.
4. Code quality checks are executed, including compile, unit tests, and static analysis.

## ✅ Pull Request Checks

Every PR goes through a set of automated checks:

- ✅ **PR Review by Azure OpenAI** – Posts review comments using GPT-based feedback.
- 🛠️ **Compile Project** – Verifies that the project compiles successfully.
- 🧪 **Run Unit Tests** – Executes unit tests to ensure nothing is broken.
- 🔍 **SonarCloud Analysis** – Performs static code analysis.
- 🟢 **SonarCloud Code Analysis** – Ensures the PR passes the Quality Gate on SonarCloud.

These checks help maintain high code quality and catch problems early.

## 🛠️ Project Structure

- `.github/workflows/`: GitHub Actions workflow files.
- `.sap-ai-pr-review/review.py`: Main Python script to call Azure OpenAI and comment on PRs.
- `.sap-ai-pr-review/requirements.txt`: Python dependency definitions.

## ⚙️ Requirements

You need to configure the following repository secrets:

| Secret | Description |
|--------|-------------|
| `AZURE_OPENAI_KEY` | Azure OpenAI API key |
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI endpoint URL |
| `AZURE_OPENAI_DEPLOYMENT` | Deployment name (e.g., `gpt-35-turbo`) |
| `GITHUB_TOKEN` | GitHub token (automatically provided by GitHub Actions) |

## 🚀 How to Use

1. Clone this repository or use it as a template.
2. Add the required secrets in **Settings > Secrets and variables > Actions**.
3. Push code changes and open a Pull Request.
4. GitHub Actions will run automatically and post review comments, compile the code, run tests, and perform static analysis.

## 📄 License

This project is intended for internal demonstration purposes. No license has been defined.
