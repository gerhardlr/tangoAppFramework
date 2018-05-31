pipeline {
  agent any
  stages {
    stage('build test bench') {
      steps {
        sh 'cd Testing/CI'
        sh 'docker-compose -f Testing/CI/docker-compose.tangobase.yaml up -d'
      }
    }
    stage('tear down test bench') {
      steps {
        sh 'docker-compose -f Testing/CI/docker-compose.tangobase.yaml down --remove-orphans'
      }
    }
  }
}