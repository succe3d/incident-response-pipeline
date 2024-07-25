import boto3
import time

def create_log_group_and_stream(client, log_group_name, log_stream_name):
    try:
        client.create_log_group(logGroupName=log_group_name)
    except client.exceptions.ResourceAlreadyExistsException:
        pass

    try:
        client.create_log_stream(logGroupName=log_group_name, logStreamName=log_stream_name)
    except client.exceptions.ResourceAlreadyExistsException:
        pass

def log_incident():
    log_group_name = "incident-response-log-group"
    log_stream_name = "incident-response-log-stream"
    client = boto3.client('logs', region_name='us-east-2')

    create_log_group_and_stream(client, log_group_name, log_stream_name)

    timestamp = int(round(time.time() * 1000))
    message = f"Incident detected at {time.ctime()}"

    response = client.put_log_events(
        logGroupName=log_group_name,
        logStreamName=log_stream_name,
        logEvents=[
            {
                'timestamp': timestamp,
                'message': message
            },
        ]
    )

log_incident()
