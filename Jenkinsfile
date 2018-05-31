pipeline {
  agent {
    docker {
      image 'node:7-alpine'
    }

  }
  stages {
    stage('Test') {
      steps {
        sh 'node --version'
        sh 'cd Testing/CI'
        sh 'docker-compose up'
      }
    }
  }
}