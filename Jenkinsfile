pipeline {
  agent any
  stages {
    stage('build test bench') {
      steps {
        sh 'cd Testing/CI'
        sh 'docker-compose -f docker-compose.tangobase.yaml up'
      }
    }
  }
}