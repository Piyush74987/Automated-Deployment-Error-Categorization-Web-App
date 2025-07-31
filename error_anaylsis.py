import nltk
import re
import difflib
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# NLTK downloads
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess(text):
    tokens = word_tokenize(text.lower())
    return set(
        lemmatizer.lemmatize(word)
        for word in tokens
        if word.isalnum() and word not in stop_words
    )

def fuzzy_score(set1, set2):
    score = 0
    for token in set1:
        matches = difflib.get_close_matches(token, set2, cutoff=0.8)
        if matches:
            score += 1
    return score

def analyze_error_with_nlp(error_text):
    failure_categories = {
        "3rd party error": {
            "keywords": ["3rd party"],
            "reason": "Error caused by third-party dependency.",
            "resolution": "Check compatibility with third-party dependencies. Update or replace as necessary.",
            "prevention": "Regularly update third-party dependencies and ensure compatibility with your system."
        },
        "Automated test failure": {
            "keywords": ["Automated test", "test job", "archives", "flowxstream", "archives"],
            "reason": "Automated test failure occurred.",
            "resolution": "Investigate failing test cases, debug issues, and make necessary code changes.",
            "prevention": "Improve test coverage, maintain test suites, and ensure test environment consistency."
        },
        "code issue": {
            "keywords": ["code issue", "exception occurred during task"],
            "reason": "Error caused by issues in the codebase.",
            "resolution": "Review and debug code, fix any syntax or logical errors.",
            "prevention": "Adopt coding best practices, perform code reviews, and use static code analysis tools."
        },
        "detached head": {
            "keywords": ["detached head"],
            "reason": "Error due to detached head in version control.",
            "resolution": "Reattach the HEAD to a branch or commit changes to a branch.",
            "prevention": "Avoid detaching the HEAD unintentionally. Commit changes to branches regularly."
        },
        "disk space": {
            "keywords": ["disk space", "low disk space"],
            "reason": "Error caused by insufficient disk space.",
            "resolution": "Free up disk space by deleting unnecessary files or expanding storage capacity.",
            "prevention": "Regularly monitor disk space usage and clean up unnecessary files."
        },
        "existing version": {
            "keywords": ["existing version", "version dashboard", "wrong version", "version already exists", "stopping the build", "commit as only an update"],
            "reason": "Error due to conflicting or incorrect version.",
            "resolution": "Ensure the correct version is used or resolve version conflicts.",
            "prevention": "Maintain version consistency and verify versions before deployment."
        },
        "failed build": {
            "keywords": ["failed build", "failed to deploy instance", "unreachable"],
            "reason": "Error occurred during the build process or deployment.",
            "resolution": "Investigate build or deployment failures, fix issues, and retry.",
            "prevention": "Maintain a stable build and deployment process, perform regular tests."
        },
        "Gradle concurrency error": {
            "keywords": ["Gradle concurrency"],
            "reason": "Error caused by concurrency issues in Gradle.",
            "resolution": "Review Gradle configuration, dependencies, and parallel execution settings.",
            "prevention": "Avoid complex dependency graphs, manage concurrency effectively."
        },
        "incorrect packer version": {
            "keywords": ["incorrect packer version"],
            "reason": "Error due to incorrect Packer version.",
            "resolution": "Install or update Packer to the correct version.",
            "prevention": "Ensure correct Packer version is used and manage versions carefully."
        },
        "jenkins error": {
            "keywords": ["jenkins error"],
            "reason": "Error occurred in Jenkins.",
            "resolution": "Investigate Jenkins logs, configuration, and dependencies.",
            "prevention": "Regularly monitor Jenkins, update plugins, and maintain system stability."
        },
        "jenkins plugin issue": {
            "keywords": ["jenkins plugin issue", "jenkinsci", "plugins", "end of pipelinek8s", "error when executing success post", "completed with status unstable"],
            "reason": "Error caused by issues with Jenkins plugins.",
            "resolution": "Review plugin configuration, update or replace problematic plugins.",
            "prevention": "Regularly update Jenkins plugins, test compatibility before deployment."
        },
        "low disk space issue in jenkins": {
            "keywords": ["low disk space in jenkins"],
            "reason": "Error due to low disk space in Jenkins environment.",
            "resolution": "Free up disk space, optimize Jenkins workspace usage.",
            "prevention": "Regularly monitor disk space in Jenkins, clean up old builds and artifacts."
        },
        "missing ansible variable": {
            "keywords": ["missing ansible variable"],
            "reason": "Error due to missing variable in Ansible playbook.",
            "resolution": "Define the missing variable or handle missing variable gracefully.",
            "prevention": "Ensure all required variables are defined in Ansible playbooks."
        },
        "race condition": {
            "keywords": ["race condition", "concurrent access", "synchronization issue"],
            "reason": "Error caused by a race condition.",
            "resolution": "Analyze and synchronize concurrent access to shared resources.",
            "prevention": "Use proper synchronization mechanisms, avoid shared state where possible."
        },
        "script not available": {
            "keywords": ["script not available"],
            "reason": "Error occurred because the script is not available.",
            "resolution": "Ensure the script is present and accessible.",
            "prevention": "Maintain script availability and ensure proper permissions."
        },
        "user error": {
            "keywords": ["verify", "correct cluster", "search criteria", "remove ocr lock", "has an invalid value", "remote repo origin"],
            "reason": "Error caused by user action or input.",
            "resolution": "Provide clear instructions, and implement validation checks.",
            "prevention": "Provide user training, implement user-friendly interfaces, and validate input."
        },
        "missing failure category": {
            "keywords": ["missing failure category"],
            "reason": "Error category not specified.",
            "resolution": "Identify and categorize the error.",
            "prevention": "Ensure errors are properly categorized for effective analysis and resolution."
        },
        "incorrect sql query": {
            "keywords": ["SQL syntax", "table", "unknown column", "foreign key constraint", "incorrect number of arguments for procedure", "unknown column"],
            "reason": "Error caused by incorrect SQL syntax.",
            "resolution": "Review and correct the SQL query syntax.",
            "prevention": "Adopt coding standards, use parameterized queries to avoid SQL injection."
        }
    
    }

    if "sql syntax" in error_text.lower():
        return "incorrect sql query", failure_categories["incorrect sql query"]["reason"], failure_categories["incorrect sql query"]["resolution"], failure_categories["incorrect sql query"]["prevention"]

    doc_keywords = preprocess(error_text)

    best_match = "missing failure category"
    best_score = 0

    for category, data in failure_categories.items():
        keyword_set = set()
        for kw in data["keywords"]:
            keyword_set.update(preprocess(kw))

        # Score: direct match + fuzzy bonus
        exact_match_score = len(keyword_set.intersection(doc_keywords))
        fuzzy_bonus = fuzzy_score(doc_keywords, keyword_set)
        total_score = exact_match_score + 0.5 * fuzzy_bonus

        if total_score > best_score:
            best_score = total_score
            best_match = category

    result = failure_categories[best_match]
    return best_match, result["reason"], result["resolution"], result["prevention"]