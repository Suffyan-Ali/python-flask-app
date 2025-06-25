pipeline {
    agent any

    environment {
        IMAGE_NAME = 'flask-jenkins-app'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/Suffyan-Ali/python-flask-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}")
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Stop previous container if running
                    sh 'docker rm -f flask_container || true'
                    // Run new container
                    sh 'docker run -d --name flask_container -p 5000:5000 flask-jenkins-app'
                }
            }
        }
    }
}

