pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out FreelanceHub source code...'
                checkout scm
            }
        }

        stage('Build / Validate') {
            steps {
                echo 'Validating project files...'
                sh 'python3 --version'
                sh 'test -f backend/app.py'
                sh 'test -f backend/requirements.txt'
                sh 'test -f tests/test_backend.py'
            }
        }

        stage('Automated Tests') {
            steps {
                echo 'Running Python syntax validation...'
                sh 'python3 -m py_compile backend/app.py tests/test_backend.py'
                sh 'python3 -m unittest discover -s tests -v'
            }
        }

        stage('Docker Build') {
            steps {
                echo 'Building uniquely tagged Docker images...'
                sh 'docker build -t freelancehub-backend:build-${BUILD_NUMBER} -t mprasanthi123/freelancehub-backend:build-${BUILD_NUMBER} ./backend'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKERHUB_USERNAME',
                    passwordVariable: 'DOCKERHUB_TOKEN'
                )]) {
                    sh '''
                        set +x
                        printf '%s' "$DOCKERHUB_TOKEN" | docker login -u "$DOCKERHUB_USERNAME" --password-stdin
                        docker push mprasanthi123/freelancehub-backend:build-${BUILD_NUMBER}
                        docker logout
                    '''
                }
            }
        }

        stage('Deploy Test Container') {
            steps {
                echo 'Deploying to isolated test port 8003...'
                sh '''
                    docker rm -f freelancehub-backend-sprint9 || true
                    docker run -d \
                        --name freelancehub-backend-sprint9 \
                        --restart unless-stopped \
                        -p 8003:8000 \
                        mprasanthi123/freelancehub-backend:build-${BUILD_NUMBER}
                '''
            }
        }

        stage('Deployment Health Check') {
            steps {
                echo 'Checking deployed application on port 8003...'
                sh '''
                    for attempt in $(seq 1 12); do
                        if curl --fail --silent http://localhost:8003/ > /dev/null; then
                            echo "Health check passed!"
                            curl --fail --silent http://localhost:8003/
                            exit 0
                        fi
                        echo "Waiting for application... attempt ${attempt}/12"
                        sleep 5
                    done

                    echo "Health check failed."
                    docker logs freelancehub-backend-sprint9
                    exit 1
                '''
            }
        }
    }

    post {
        success {
            echo 'FreelanceHub CI/CD pipeline completed successfully!'
        }
        failure {
            echo 'FreelanceHub CI/CD pipeline failed. Check the console output.'
        }
    }
}
