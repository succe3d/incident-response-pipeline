import boto3
import time
import random

def create_log_group_and_stream(client, log_group_name, log_stream_name):
    try:
        client.create_log_group(logGroupName=log_group_name)
    except client.exceptions.ResourceAlreadyExistsException:
        pass

    try:
        client.create_log_stream(logGroupName=log_group_name, logStreamName=log_stream_name)
    except client.exceptions.ResourceAlreadyExistsException:
        pass

def detect_incident():
    # Simulate an incident detection logic
    incident_types = ["Unauthorized access attempt", "Data breach", "Service outage", "Malware detected"]
    detected = random.choice([True, False])
    if detected:
        incident_type = random.choice(incident_types)
        details = f"{incident_type} detected at {time.ctime()}"
        return details
    return None
import boto3
import time
import random

def create_log_group_and_stream(client, log_group_name, log_stream_name):
    try:
        client.create_log_group(logGroupName=log_group_name)
    except client.exceptions.ResourceAlreadyExistsException:
        pass

    try:
        client.create_log_stream(logGroupName=log_group_name, logStreamName=log_stream_name)
    except client.exceptions.ResourceAlreadyExistsException:
        pass

def detect_incident():
    # Simulate an incident detection logic
    incident_types = ["Unauthorized access attempt", "Data breach", "Service outage", "Malware detected"]
    detected = random.choice([True, False])
    if detected:
        incident_type = random.choice(incident_types)
        details = f"{incident_type} detected at {time.ctime()}"
        return details
    return None

def log_incident():
    log_group_name = "incident-response-log-group"
    log_stream_name = "incident-response-log-stream"
    client = boto3.client('logs', region_name='us-east-2')

    create_log_group_and_stream(client, log_group_name, log_stream_name)

    incident_details = detect_incident()
    if incident_details:
        timestamp = int(round(time.time() * 1000))
        message = incident_details

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
        print(f"Logged incident: {message}")
    else:
        print("No incident detected")

log_incident()

def log_incident():
    log_group_name = "incident-response-log-group"
    log_stream_name = "incident-response-log-stream"
    client = boto3.client('logs', region_name='us-east-2')

    create_log_group_and_stream(client, log_group_name, log_stream_name)

    incident_details = detect_incident()
    if incident_details:
        timestamp = int(round(time.time() * 1000))
        message = incident_details

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
        print(f"Logged incident: {message}")
    else:
        print("No incident detected")

log_incident()
