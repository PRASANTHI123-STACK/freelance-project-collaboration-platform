
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
                sh 'test -f tests/test_backend.py'
            }
        }

        stage('Test / Validate') {
            steps {
                echo 'Running Python syntax validation...'
                sh 'python3 -m py_compile backend/app.py tests/test_backend.py'
                sh 'python3 -m unittest discover -s tests -v'
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
