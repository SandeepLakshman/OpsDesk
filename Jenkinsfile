pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                bat 'python -m pytest -v'
            }
        }

        stage('Validation') {
            steps {
                bat 'python -c "from app import create_app; app = create_app(); print(\\\"Application validation passed\\\")"'
            }
        }
    }

    post {
        success {
            echo 'OpsDesk CI pipeline completed successfully.'
        }

        failure {
            echo 'OpsDesk CI pipeline failed. Check the console logs.'
        }
    }
}