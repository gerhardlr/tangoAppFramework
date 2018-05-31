pipeline {
  agent any
  stages {
    stage('build test bench') {
      steps {
        sh 'cd Testing/CI'
        sh 'docker-compose up -f Testing/CI/ docker-compose.tangobase.yaml up'
      }
    }
  }
}