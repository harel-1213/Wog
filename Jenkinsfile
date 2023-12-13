pipeline {
    agent any

    environment {
        DOCKER_COMPOSE_VERSION = '1.26.0'
        DOCKER_IMAGE_NAME = 'harel/wog:latest'
    }

     triggers {
        pollSCM('* * * * *')
    }

    stages {
        stage('Checkout to the git repo') {
            steps {
                checkout scm
            }
        }


    stage('Build the docker compose') {
        steps {
            script {
                bat 'docker-compose build'
            }
        }
    }

    stage('Run the docker compose') {
        steps {
            script {
                bat 'docker-compose up -d'
            }
        }
    }

    stage('Test the score with selenium') {
        steps {
            script {
                bat 'pip install --no-cache-dir -r requirements.txt'
                bat 'python e2e.py'
            }
        }
    }

    }

}
