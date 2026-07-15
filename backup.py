import boto3

ec2_client= boto3.client('ec2')

def backup_instance(instance_id):
    try:
        response= ec2_client.create_image(InstanceId=instance_id, Name=f"BackupTest1-{instance_id}")
        return response
    except Exception as e:
        return {"error": str(e)}

def wait_for_backup(image_id):
    try:
        waiter = ec2_client.get_waiter('image_available')
        waiter.wait(ImageIds=[image_id], WaiterConfig={'Delay': 30, 'MaxAttempts': 40})
        return True
    except Exception as e:
        return {"error": str(e)}