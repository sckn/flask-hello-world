pipeline {
    agent any
    stages {
        stage('Initialize'){
            steps {
                script {
                def dockerHome = tool 'mydocker'
                env.PATH = "${dockerHome}/bin:${env.PATH}"
                }
            }
        }
        stage('Image Build') {
            imageBuild("SEC","Latest")
        }
    }
}
