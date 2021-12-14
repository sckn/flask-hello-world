node {
    stage("Initalize") {
        def dockerHome = tool 'mydocker'
        env.PATH = "${dockerHome}/bin:${env.PATH}"
    }
}

def imageBuild(containerName, tag, dockerUser){
    sh "sudo docker build -t $dockerUser/$containerName:$tag ."
    echo "Image build complete"
}


pipeline {
    agent any
    stages {

        stage('Image Build') {
            steps {
                imageBuild("SEC","Latest","sckn")
            }
        }
    }
}
