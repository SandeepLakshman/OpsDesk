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
            environment {
                DOCKER_IMAGE = 'sandeep3005/opsdesk:latest'
            }

            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub',
                    usernameVariable: 'DOCKER_USERNAME',
                    passwordVariable: 'DOCKER_PASSWORD'
                )]) {
                    sh 'echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin'
                    sh 'docker build -t "$DOCKER_IMAGE" .'
                    sh 'docker push "$DOCKER_IMAGE"'
                    sh 'docker logout'
                }
            }
        }
    }
}
