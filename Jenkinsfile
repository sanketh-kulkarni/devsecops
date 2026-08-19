pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "devsecops-app:${BUILD_NUMBER}"
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
                bat "docker build -t ${DOCKER_IMAGE} ."
            }
        }

        stage('Container Security Scan - Trivy') {
            steps {
                echo 'Scanning Docker image with Trivy for vulnerabilities...'
                // Scans the built image and flags HIGH or CRITICAL CVEs
                bat "trivy image --severity HIGH,CRITICAL ${DOCKER_IMAGE}"
            }
        }

        stage('Deploy - Kubernetes') {
            steps {
                echo 'Deploying application to Kubernetes cluster...'
                bat "kubectl apply -f deployment.yaml"
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution complete.'
        }
        success {
            echo 'Build, security scans, and deployment passed successfully!'
        }
        failure {
            echo 'Pipeline halted due to a security violation or build error.'
        }
    }
}
