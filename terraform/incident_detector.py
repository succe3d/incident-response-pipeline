import boto3
import time
import json

# Initialize a session using Amazon CloudWatch
client = boto3.client('logs')

# CloudWatch Log group name
log_group_name = '/aws/lambda/incident_logs'

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
