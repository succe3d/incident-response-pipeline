pipeline {
    agent any

    environment {
        AWS_DEFAULT_REGION = 'us-west-2'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/yourusername/incident-response-pipeline.git'
            }
        }
        stage('Deploy Infrastructure') {
            steps {
                sh 'terraform init'
                sh 'terraform apply -auto-approve'
            }
        }
        stage('Run Incident Detection') {
            steps {
                script {
                    // Simulate incident detection
                    def incidentDetected = true
                    if (incidentDetected) {
                        // Invoke Lambda function for incident response
                        sh 'aws lambda invoke --function-name incidentHandler output.txt'
                    }
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
