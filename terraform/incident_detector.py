import boto3
import time
import logging

logging.basicConfig(level=logging.INFO)

def create_log_group_and_stream(client, log_group_name, log_stream_name):
    try:
        client.create_log_group(logGroupName=log_group_name)
        logging.info(f"Log group {log_group_name} created.")
    except client.exceptions.ResourceAlreadyExistsException:
        logging.info(f"Log group {log_group_name} already exists.")

    try:
        client.create_log_stream(logGroupName=log_group_name, logStreamName=log_stream_name)
        logging.info(f"Log stream {log_stream_name} created.")
    except client.exceptions.ResourceAlreadyExistsException:
        logging.info(f"Log stream {log_stream_name} already exists.")

def log_incident():
    # Set the region
    client = boto3.client('logs', region_name='us-west-2')  # Make sure this matches your desired region
    log_group_name = 'incident-response-log-group'
    log_stream_name = 'incident-response-log-stream'

    create_log_group_and_stream(client, log_group_name, log_stream_name)

    response = client.put_log_events(
        logGroupName=log_group_name,
        logStreamName=log_stream_name,
        logEvents=[
            {
                'timestamp': int(round(time.time() * 1000)),
                'message': 'Sample incident detected and logged.'
            },
        ]
    )
    logging.info("Log event put to CloudWatch.")

log_incident()
