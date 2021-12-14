pipeline {
    agent { docker { image 'python:3.10.1-alpine' } }
    stages {
        stage('Initialize'){
            steps {
                echo 'Initialize'
            }
        }
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}
