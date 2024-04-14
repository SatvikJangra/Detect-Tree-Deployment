pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/your-repo/your-flask-app.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t your-docker-repo:your-tag .'
            }
        }
        stage('Push Docker Image') {
            steps {
                sh 'docker push your-docker-repo:your-tag'
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f deployment.yaml'
                sh 'kubectl apply -f service.yaml'
            }
        }
    }
}
