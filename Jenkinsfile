pipeline {
  agent any
  environment {
    DOCKER_NETWORK = 'docker-network'
  }
  stages {
    stage('Build') {
      steps {
        sh 'docker network create docker-network'
        sh 'docker-compose -f docker-compose.test_bench.yaml up -d'
      }
    }
    stage('Test') {
      steps {
        sh 'docker-compose -f appModule/docker-compose.test_item.yaml up -d'
        sh 'docker-compose -f appModule/docker-compose.test_item.yaml down -d'
      }
    }
    stage('Tear down') {
      steps {
        sh 'docker-compose -f docker-compose.test_bench.yaml down'
        sh 'docker network create docker-network'
        cleanWs(cleanWhenAborted: true, cleanWhenFailure: true, cleanWhenNotBuilt: true, cleanWhenSuccess: true, cleanWhenUnstable: true, cleanupMatrixParent: true, deleteDirs: true)
      }
    }
  }
}