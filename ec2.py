import boto3

ec2_client= boto3.client('ec2')
def describe_instance():
    try:
        response = ec2_client.describe_instances()
        return response
    except Exception as e:
        return {"error": str(e)}

def start_instance(instance_id):
    try:
        response= ec2_client.start_instances(InstanceIds=[instance_id])
        return response
    except Exception as e:
        return {"error": str(e)}
