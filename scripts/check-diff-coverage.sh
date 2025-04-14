#!/bin/bash
set -e

# Default branch to compare against
BRANCH_NAME=${1:-develop}
BASE_BRANCH="origin/$BRANCH_NAME"
COVERAGE_FILE="target/site/jacoco/jacoco.xml"

echo "🔍 Checking test coverage against $BASE_BRANCH..."

# Check if diff-cover is installed
if ! command -v diff-cover &> /dev/null; then
  echo "❌ Error: 'diff-cover' is not installed."
  echo "👉 You can install it with: pip3 install diff-cover --break-system-packages"
  exit 1
fi

# Run Maven tests and generate JaCoCo report
echo "🚧 Running tests and generating coverage report..."
mvn clean verify -q

# Run diff-cover with the specified base branch
echo "📊 Running diff-cover..."
diff-cover "$COVERAGE_FILE" --compare-branch "$BASE_BRANCH" --fail-under=70

echo "✅ Diff coverage check completed successfully."
