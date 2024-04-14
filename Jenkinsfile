pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/SatvikJangra/Detect-Tree-Deployment'
            }
        }
        stage('Build') {
            steps {
                script {
                    def imageName = 'satvikjangra/dockertry:latest'
                    sh 'docker build -t ' + imageNew + ' .'
                }
            }
        }
        stage('Push') {
            steps {
                script {
                    def imageName = 'satvikjangra/dockertry:latest'
                    sh 'docker push ' + imageNew
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    sh 'kubectl apply -f Deployment.yaml'
                    sh 'kubectl apply -f Service.yaml'
                }
            }
        }
    }
}
