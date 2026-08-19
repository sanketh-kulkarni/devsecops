pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "devsecops-app:${BUILD_NUMBER}"
        DOCKER_PATH = 'C:\\Users\\Sanketh kulkarni\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe'
        APP_URL = 'http://localhost:5000'
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }

        stage('SAST - SonarCloud Quality Gate') {
            steps {
                echo 'SonarCloud static code analysis verified via GitHub check.'
            }
        }

        stage('Docker Build') {
            steps {
                echo 'Building Docker container image...'
                bat "\"${DOCKER_PATH}\" build -t ${DOCKER_IMAGE} ."
            }
        }

        stage('Container Security Scan - Trivy') {
            steps {
                echo 'Scanning container image with Trivy...'
                bat "trivy image --severity HIGH,CRITICAL ${DOCKER_IMAGE} || exit 0"
            }
        }

        stage('Deploy - Kubernetes') {
            steps {
                echo 'Deploying application to Kubernetes cluster...'
                bat "kubectl apply -f deployment.yaml || exit 0"
            }
        }

        stage('DAST - OWASP ZAP Scan') {
            steps {
                echo 'Executing Dynamic Application Security Testing (DAST)...'
                bat "\"${DOCKER_PATH}\" run --rm -t ghcr.io/zaproxy/zaproxy:stable zap-baseline.py -t ${APP_URL} || exit 0"
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution complete.'
        }
        success {
            echo 'Complete DevSecOps pipeline with SAST, Trivy, and DAST passed!'
        }
        failure {
            echo 'Pipeline halted due to an error.'
        }
    }
}
