pipeline {
    agent any

    environment {
        STUDENT_NAME = 'Anuar'
        STUDENT_SURNAME = 'Akhmet'
        STUDENT_GROUP = 'IT2-2307'
        IMAGE_NAME = 'akhmet-anuar-devops'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh 'python3 -m compileall -q app/'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m unittest discover -s app -p "test_*.py" -v'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t ${IMAGE_NAME}:jenkins .'
            }
        }

        stage('Docker Run') {
            steps {
                sh '''
                    docker rm -f anuar-jenkins-app 2>/dev/null || true
                    docker run -d --name anuar-jenkins-app \
                      -e STUDENT_NAME="Anuar Akhmet" \
                      ${IMAGE_NAME}:jenkins
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check console output.'
        }
    }
}
