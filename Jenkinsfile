pipeline {
  agent any
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
        sh 'docker-compose -f appModule/docker-compose.test_item.yaml down'
      }
    }
    stage('Tear down') {
      steps {
        sh 'docker-compose -f docker-compose.test_bench.yaml down'
        sh 'docker network rm docker-network'
      }
    }
  }
  post {
        unstable {
            echo 'I am unstable :/'
        }
        failure {
            sh 'docker-compose -f docker-compose.test_bench.yaml down --remove-orphans'
            sh 'docker-compose -f appModule/docker-compose.test_item.yaml down --remove-orphans'
            sh 'sh docker network rm docker-network'
        }
        changed {
            echo 'Things were different before...'
        }
    }
  environment {
    DOCKER_NETWORK = 'docker-network'
  }
}