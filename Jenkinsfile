pipeline {
    agent any

    environment {
        AWS_DEFAULT_REGION = 'us-west-2'
    }

    stages {
        stage('Checkout') {
            steps {
                git credentialsId: 'github-credentials', url: 'https://github.com/succe3d/incident-response-pipeline.git'
            }
        }
        stage('Deploy Infrastructure') {
            steps {
                sh 'cd terraform && terraform init && terraform apply -auto-approve'
            }
        }
        stage('Run Incident Detection') {
            steps {
                sh 'python3 incident_detector.py'
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
