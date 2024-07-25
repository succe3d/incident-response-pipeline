import boto3

def log_incident():
    # Specify the region
    client = boto3.client('logs', region_name='us-west-2')
    
    # Your existing logic here
    log_group_name = '/aws/lambda/incident_logs'
    log_stream_name = 'incident_log_stream'

    response = client.create_log_stream(
        logGroupName=log_group_name,
        logStreamName=log_stream_name
    )

    print(response)

if __name__ == "__main__":
    log_incident()
