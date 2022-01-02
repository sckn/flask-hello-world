node {
    stage("Initalize") {
        def dockerHome = tool 'mydocker'
        env.PATH = "${dockerHome}/bin:${env.PATH}"
    }
}

def imageBuild(containerName, tag, dockerUser){
    sh "docker -H 192-168-1-46.sslip.io:2375 build -t $dockerUser/$containerName:$tag ."
    echo "Image build complete"
}


pipeline {
    agent any
    triggers {
        cron('*/30 * * * *')
    }
    stages {

        stage('Image Build') {
            steps {
                imageBuild("repository","Latest","sckn")
            }
        }
    }
}
