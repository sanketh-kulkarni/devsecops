pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code from Git...'
                checkout scm
            }
        }

        stage('SAST - SonarQube') {
            steps {
                echo 'Running Static Application Security Testing (SAST)...'
                // We will add the actual SonarQube scanner command next
            }
        }

        stage('Build') {
            steps {
                echo 'Building application...'
                // Maven / Node.js build command
            }
        }

        stage('Container Image Scan - Trivy') {
            steps {
                echo 'Scanning container image with Trivy...'
                // Trivy CLI scan command
            }
        }

        stage('Deploy - Kubernetes') {
            steps {
                echo 'Deploying to Kubernetes cluster...'
                // kubectl apply command
            }
        }

        stage('DAST - OWASP ZAP') {
            steps {
                echo 'Running Dynamic Application Security Testing (DAST)...'
                // OWASP ZAP scan command
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution complete.'
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check stage logs for security gate violations.'
        }
    }
}
