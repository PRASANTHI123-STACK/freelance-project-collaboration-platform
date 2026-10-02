pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out FreelanceHub source code...'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Validating project files...'
                sh 'python3 --version'
                sh 'test -f backend/app.py'
                sh 'test -f backend/requirements.txt'
            }
        }

        stage('Test / Validate') {
            steps {
                echo 'Running Python syntax validation...'
                sh 'python3 -m py_compile backend/app.py'
            }
        }

        stage('Docker Build') {
            steps {
                echo 'Building FreelanceHub Docker image...'
                sh 'docker build -t freelancehub-backend:build-${BUILD_NUMBER} ./backend'
            }
        }
    }

    post {
        success {
            echo 'FreelanceHub CI Pipeline completed successfully!'
        }

        failure {
            echo 'FreelanceHub CI Pipeline failed. Check the console output.'
        }
    }
}