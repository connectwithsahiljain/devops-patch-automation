import logger
import ec2
import json
import backup
import patch

count=0
backup_jobs=[]
logger.logging.info("Starting Patch Automation...")
instance_info= ec2.describe_instance()
for reservation in instance_info['Reservations']:
    for instance in reservation['Instances']:
        count += 1
logger.logging.info(f"Found {count} EC2 instances")
for reservation in instance_info['Reservations']:
    for instance in reservation['Instances']:
        if instance['State']['Name'] == 'running':
            logger.logging.info(f"Instance ID : {instance['InstanceId']} is already running.")
            logger.logging.info(f"State Name : {instance['State']['Name']}")
            logger.logging.info(f"Availability Zone : {instance['Placement']['AvailabilityZone']}")
            logger.logging.info(f"Instance Type : {instance['InstanceType']}")
            logger.logging.info('---')
            backup_response = backup.backup_instance(instance['InstanceId'])
            logger.logging.info(f"Backup response: {json.dumps(backup_response)}")
            if 'ImageId' in backup_response:
                backup_jobs.append({'InstanceId' : instance['InstanceId'], 'ImageId' : backup_response['ImageId'], 'status' : 'pending'})
                image_id = backup_response['ImageId']
                
        else:
            logger.logging.info(f"Instance ID : {instance['InstanceId']} is stopped. Starting instance...")
            response = ec2.start_instance(instance['InstanceId'])
            logger.logging.info(f"Start response: {json.dumps(response)}")
            logger.logging.info('---')

logger.logging.info(f"Checking for backup {image_id} to complete...")

for job in backup_jobs:
    result = backup.wait_for_backup(job['ImageId'])
    logger.logging.info(f"Backup Job: {job['InstanceId']} - {job['ImageId']} - {job['status']}")
    if result is True:
        job['status'] = 'completed'
        logger.logging.info(f"Backup {job['ImageId']} completed successfully.")
        if job['status'] == 'completed':
            patch_response = patch.patch_instance()
            logger.logging.info(f"Patch response: {json.dumps(patch_response)}")
    else:
        job['status'] = 'failed'
        logger.logging.error(f"Backup wait failed: {result}")

logger.logging.info("Automation Completed.")