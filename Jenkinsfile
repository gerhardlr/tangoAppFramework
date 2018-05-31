pipeline {
  agent {
    docker {
      image 'docker/compose'
    }

  }
  stages {
    stage('Test') {
      steps {
        sh 'node --version'
        sh 'cd Testing/CI'
        sh 'docker -v'
      }
    }
  }
}