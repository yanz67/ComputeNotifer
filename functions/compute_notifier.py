import boto3
import os

region = os.getenv('AWS_REGION', 'us-east-1')
topic_arn = os.getenv('COMPUTE_NOTIFIER_TOPIC_ARN')
env = os.getenv('ENVIRONMENT_NAME', 'ENV')
ec2 = boto3.client('ec2')
sns = boto3.client('sns')


def handler(event, context):
    running_instances = number_of_running_instances()

    if running_instances > 0:
        try:
            sns.publish(TopicArn=topic_arn,
                        Message=f"""There are {running_instances} instances running in {env}""")
        except Exception as e:
            return {
                'statusCode': 500,
                'body': f'{e}'
            }
        return {
            'statusCode': 200,
            'body': 'Posted Message successfully'
        }


def number_of_running_instances():
    num_instances = ec2.describe_instances(Filters=[
        {
            'Name': 'instance-state-name',
            'Values': ['running']
        }
    ])['Reservations']
    return len(num_instances) if num_instances else 0
