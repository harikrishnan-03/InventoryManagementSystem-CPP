import boto3
from botocore.exceptions import ClientError

def create_s3_bucket(bucket_name, region):
    try:
        s3_client = boto3.client('s3', region_name=region)
        
        # Use CreateBucketConfiguration only for regions other than 'us-east-1'
        if region == 'us-east-1':
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint': region}
            )
        
        print(f"Bucket '{bucket_name}' created successfully.")
        return True
    except ClientError as e:
        print(f"Error: {e}")
        return False

bucket_name = "imsharibucket"
region = 'us-east-1'
create_s3_bucket(bucket_name, region)
