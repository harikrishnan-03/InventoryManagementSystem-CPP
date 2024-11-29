import boto3

sqs=boto3.client('sqs')

responseSqs=sqs.create_queue(QueueName='LowStockWarningQueue')
queueUrl=responseSqs['QueueUrl']
arn=sqs.get_queue_attributes(QueueUrl=queueUrl, AttributeNames=['QueueArn'])['Attributes']['QueueArn']
print(arn)