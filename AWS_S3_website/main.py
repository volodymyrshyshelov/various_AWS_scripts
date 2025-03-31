import boto3
import variables
from AWS_Functions import s3

session = boto3.Session(
    aws_access_key_id=variables.aws_access_key_id,
    aws_secret_access_key=variables.aws_secret_access_key,
    region_name=variables.region_name
)
s3u_session = session.client('s3')
lambda_client_session = session.client('lambda')

try:
    # Create S3 bucket
    if not s3.check_existing_buckets(variables.bucket_name):
        s3.create_bucket(variables.bucket_name , variables.region_name)
   
    # Set bucket policy for public read access
    s3.set_bucket_policy(variables.bucket_name, variables.user_name, variables.aws_account_id)
   
    # Upload site files to S3 bucket
    s3.upload_files_to_bucket(variables.bucket_name)
   
    # List files in S3 bucket
    s3.list_files_in_bucket(variables.bucket_name)

except Exception as e:
    # Log the exception and error message
    print("An error occurred:")
    print(str(e))
    raise