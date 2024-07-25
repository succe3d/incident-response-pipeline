import boto3
import json
import datetime


def create_log_group_and_stream(client, log_group_name, log_stream_name):
    try:
        client.create_log_group(logGroupName=log_group_name)
        print(f'Log group {log_group_name} created.')
    except client.exceptions.ResourceAlreadyExistsException:
        print(f'Log group {log_group_name} already exists.')

    try:
        client.create_log_stream(logGroupName=log_group_name, logStreamName=log_stream_name)
        print(f'Log stream {log_stream_name} created.')
    except client.exceptions.ResourceAlreadyExistsException:
        print(f'Log stream {log_stream_name} already exists.')


def log_incident():
    client = boto3.client('logs', region_name='us-west-2')  # Specify the region here

    log_group_name = 'incident-response-log-group'
    log_stream_name = 'incident-response-log-stream'

    create_log_group_and_stream(client, log_group_name, log_stream_name)

    timestamp = int(datetime.datetime.now().timestamp() * 1000)
    message = {
        'incident': 'Sample incident',
        'timestamp': str(datetime.datetime.now())
    }

    response = client.put_log_events(
        logGroupName=log_group_name,
        logStreamName=log_stream_name,
        logEvents=[
            {
                'timestamp': timestamp,
                'message': json.dumps(message)
            }
        ]
    )

    print(response)


if __name__ == "__main__":
    log_incident()
