import boto3
import json


# AWS Configuration
LAMBDA_FUNCTION_NAME = "GenerateStockPDFLambda"
LAMBDA_ROLE_ARN = "arn:aws:iam::058264363855:role/LabRole"
LAMBDA_RUNTIME = "python3.9"
LAMBDA_HANDLER = "lambda_function.lambda_handler"  
ZIP_FILE_PATH = "./lambda_code.zip"

# RDS Configuration
RDS_HOST = "x23297948-ims.c9206kckwag4.us-east-1.rds.amazonaws.com"
RDS_USER = "root"
RDS_PASSWORD = "kausthubham"
RDS_DB = "ims_db"

S3_BUCKET_NAME = "imsharipdfbucket"

# Initialize AWS Lambda Client
lambda_client = boto3.client('lambda', region_name="us-east-1")

# Read the ZIP file
with open(ZIP_FILE_PATH, "rb") as f:
    zip_content = f.read()

# Create the Lambda Function
response = lambda_client.create_function(
    FunctionName=LAMBDA_FUNCTION_NAME,
    Runtime=LAMBDA_RUNTIME,
    Role=LAMBDA_ROLE_ARN,
    Handler=LAMBDA_HANDLER,
    Code={'ZipFile': zip_content},
    Description="Lambda function to generate PDF from RDS data and upload to S3",
    Timeout=120,  # Timeout in seconds
    MemorySize=256,  # Memory in MB
    Environment={
        'Variables': {
            'RDS_HOST': RDS_HOST,
            'RDS_USER': RDS_USER,
            'RDS_PASSWORD': RDS_PASSWORD,
            'RDS_DB': RDS_DB,
            'S3_BUCKET_NAME': S3_BUCKET_NAME
        }
    },
    Publish=True
)

print("Lambda function created:")
print(json.dumps(response, indent=4))
