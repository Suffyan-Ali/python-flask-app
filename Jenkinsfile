pipeline {
    agent any

    environment {
        IMAGE_NAME = 'suffyanali/flask-jenkins-app'  // Replace with your Docker Hub username
    }

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/Suffyan-Ali/python-flask-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Login to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                sh 'docker push $IMAGE_NAME'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker rm -f flask_container || true'
                sh 'docker run -d --name flask_container -p 5000:5000 $IMAGE_NAME'
            }
        }
    }
}

