pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'docker-compose -f docker-compose.test_bench.yaml up -d'
      }
    }
    stage('Test') {
      steps {
        sh 'docker-compose -f appModule/docker-compose.test_item.yaml up -d'
      }
    }
    stage('Tear down') {
      steps {
        sh 'docker-compose -f docker-compose.test_bench.yaml down'
        cleanWs(cleanWhenAborted: true, cleanWhenFailure: true, cleanWhenNotBuilt: true, cleanWhenSuccess: true, cleanWhenUnstable: true, cleanupMatrixParent: true, deleteDirs: true)
      }
    }
  }
}