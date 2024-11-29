import boto3

sns=boto3.client('sns')

responseSns=sns.create_topic(Name='LowStockWarning')
arn=responseSns['TopicArn']
print(arn)
