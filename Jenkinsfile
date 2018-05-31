pipeline {
  agent {
    docker {
      image 'ubuntu'
    }

  }
  stages {
    stage('build testing system') {
      steps {
        sh 'cd Testing/CI/'
        sh 'docker-compose -f docker-compose.tangobase.yaml up'
      }
    }
  }
}