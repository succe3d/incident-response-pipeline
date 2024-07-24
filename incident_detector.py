import boto3
import time
import json

# Initialize a session using Amazon CloudWatch
client = boto3.client('logs')

# CloudWatch Log group name
log_group_name = '/aws/lambda/incident_logs'

# Specify your AWS region
region = 'us-east-1'

client = boto3.client('logs', region_name=region)

def log_incident():
    response = client.put_log_events(
        logGroupName='your-log-group',
        logStreamName='your-log-stream',
        logEvents=[
            {
                'timestamp': int(time.time() * 1000),
                'message': 'Incident detected!'
            },
        ],
    )
    print(response)

# Function to simulate incident detection
def log_incident():
    timestamp = int(time.time() * 1000)
    message = {
        'timestamp': timestamp,
        'message': 'ALERT: Security incident detected'
    }
    response = client.put_log_events(
        logGroupName=log_group_name,
        logStreamName='incident_stream',
        logEvents=[
            {
                'timestamp': timestamp,
                'message': json.dumps(message)
            },
        ]
    )
    print(response)

if __name__ == "__main__":
    log_incident()
