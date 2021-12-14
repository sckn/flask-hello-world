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
            steps {
                imageBuild("SEC","Latest")
            }
        }
    }
}
def imageBuild(containerName, tag, dockerUser){
    sh "sudo docker build -t $dockerUser/$containerName:$tag ."
    echo "Image build complete"
}
