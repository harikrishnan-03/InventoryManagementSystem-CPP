import boto3

sns_client = boto3.client('sns', region_name='us-east-1')  
sqs_client = boto3.client('sqs', region_name='us-east-1')

sns_topic_name = 'CommunityNotification'
sns_response = sns_client.create_topic(Name=sns_topic_name)
sns_topic_arn = sns_response['TopicArn']
print(f"topic arn: {sns_topic_arn}")

sqs_queue_name = 'CommunityNotificationQueue'
sqs_response = sqs_client.create_queue(QueueName=sqs_queue_name)
queue_url = sqs_response['QueueUrl']
print(f"sqs queue URL: {queue_url}")

sqs_attributes = sqs_client.get_queue_attributes(
    QueueUrl=queue_url,
    AttributeNames=['QueueArn']
)
sqs_queue_arn = sqs_attributes['Attributes']['QueueArn']
print(f"SQS Queue ARN: {sqs_queue_arn}")



sns_client.subscribe(
    TopicArn=sns_topic_arn,
    Protocol='sqs',
    Endpoint=sqs_queue_arn
)

print(f"SQS Queue {sqs_queue_name} is subscribed to SNS Topic {sns_topic_name}.")
