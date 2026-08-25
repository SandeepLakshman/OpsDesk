# OpsDesk

> A lightweight Flask-based incident management platform with automated CI/CD using Jenkins.

## Overview

OpsDesk is a Flask web application for managing and tracking operational incidents. The project also demonstrates a complete CI workflow using GitHub, Jenkins, Docker, and automated Pytest testing.

## Features

- Incident management dashboard
- Create and track incidents
- Flask + SQLAlchemy backend
- Automated Pytest test suite
- Jenkins CI/CD pipeline
- GitHub Webhook integration
- Dockerized Jenkins environment

## Tech Stack

- **Backend:** Python, Flask
- **Database:** SQLAlchemy
- **Testing:** Pytest
- **Version Control:** Git & GitHub
- **CI/CD:** Jenkins
- **Containerization:** Docker
- **Webhook:** GitHub Webhooks + ngrok

## CI/CD Pipeline

Every GitHub push can trigger the Jenkins pipeline automatically.

```text
GitHub Push
     ↓
GitHub Webhook
     ↓
Jenkins
     ↓
Checkout
     ↓
Build
     ↓
Test
     ↓
Validation
     ↓
SUCCESS
```

### Pipeline Stages

| Stage | Purpose |
|---|---|
| Checkout | Retrieves the latest source code |
| Build | Installs project dependencies |
| Test | Runs the Pytest test suite |
| Validation | Verifies Flask application initialization |
| Post Actions | Reports pipeline status |

## Testing

Run the tests locally:

```bash
python -m pytest -v
```

Current CI result:

```text
3 tests passed
Application validation passed
Finished: SUCCESS
```

## Running Locally

```bash
git clone https://github.com/SandeepLakshman/OpsDesk.git
cd OpsDesk

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
python app.py
```

## Jenkins

The CI pipeline is defined as code in:

```text
Jenkinsfile
```

Jenkins retrieves the repository from GitHub, installs dependencies, runs automated tests, validates the Flask application, and reports the build result.

## Project Structure

```text
OpsDesk/
├── app/
├── tests/
├── requirements.txt
├── Jenkinsfile
└── README.md
```

## Author

**Sandeep Lakshman**

[GitHub](https://github.com/SandeepLakshman)