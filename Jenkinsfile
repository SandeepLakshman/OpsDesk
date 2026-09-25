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
                sh 'python3 -m pip install --ignore-installed -r requirements.txt --break-system-packages'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m pytest -v'
            }
        }

        stage('Package') {
            steps {
                sh 'docker build -t opsdesk:latest .'
            }
        }
    }
}
