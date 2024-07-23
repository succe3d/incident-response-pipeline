pipeline {
    agent any

    environment {
        AWS_DEFAULT_REGION = 'us-west-2'
    }

    stages {
        stage('Checkout SCM') {
            steps {
                git branch: 'main', url: 'https://github.com/succe3d/incident-response-pipeline.git', credentialsId: 'github-credentials'
            }
        }
        stage('Deploy Infrastructure') {
            steps {
                sh 'cd terraform && terraform init && terraform apply -auto-approve'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install boto3'
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
