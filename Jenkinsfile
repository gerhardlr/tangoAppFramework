pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'docker-compose -f Testing/CI/docker-compose.test_bench.yaml up -d'
        sh 'docker-compose -f Testing/CI/docker-compose.test_item.yaml up -d'
      }
    }
    stage('Test') {
      steps {
        sh 'echo "testing testing"'
      }
    }
    stage('Tear down') {
      steps {
        sh 'docker-compose -f Testing/CI/docker-compose.test_item.yaml down'
        sh 'docker-compose -f Testing/CI/docker-compose.test_bench.yaml down'
        cleanWs(cleanWhenAborted: true, cleanWhenFailure: true, cleanWhenNotBuilt: true, cleanWhenSuccess: true, cleanWhenUnstable: true, cleanupMatrixParent: true, deleteDirs: true)
      }
    }
  }
}