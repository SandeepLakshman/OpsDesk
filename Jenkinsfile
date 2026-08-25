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
                sh 'python3 -m pip install -r requirements.txt --break-system-packages'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m pytest -v'
            }
        }

        stage('Validation') {
            steps {
                sh 'python3 -c "from app import create_app; app = create_app(); print(\\\"Application validation passed\\\")"'
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