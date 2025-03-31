# s3.py
import boto3
import mimetypes
import json

def check_existing_buckets(bucket_name):
    s3 = boto3.client('s3')
    response = s3.list_buckets()

    for bucket in response['Buckets']:
        if bucket['Name'] == bucket_name:
            print('Bucket', bucket_name, 'already exists')
            return True

    print('Bucket', bucket_name, 'does not exist')
    return False

def create_bucket(bucket_name, region_name):
    s3 = boto3.client('s3')
    region = boto3.Session().region_name  
    if region == region_name:
        response = s3.create_bucket(
            Bucket=bucket_name
        )
    else:
        response = s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint': region
            }
        )
    print('Created S3 bucket:', bucket_name)
    print()
    
def upload_files_to_bucket(bucket_name):
    s3 = boto3.client('s3')
    files = [ 'temp/index.html', 'temp/result.js' , 'temp/styles.css']
    for file_path in files:
        content_type, _ = mimetypes.guess_type(file_path)
        with open(file_path, 'rb') as file:
            s3.upload_fileobj(file, bucket_name, file_path, ExtraArgs={'ContentType': content_type})
    print('Uploaded site files to S3 bucket:', bucket_name)
    print()

def set_bucket_policy(bucket_name, user_name , aws_account_id):
    s3 = boto3.client('s3')
    iam = boto3.client('iam')
    # Disable Block Public Access (bucket settings)
    s3.put_public_access_block(
        Bucket=bucket_name,
        PublicAccessBlockConfiguration={
            'BlockPublicAcls': False,
            'IgnorePublicAcls': False,
            'BlockPublicPolicy': False,
            'RestrictPublicBuckets': False
        }
    )
    # Create the policy IAM user JSON
    policy_for_user = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "AllowPutObject",
                "Effect": "Allow",
                "Action": [
                    "s3:PutBucketPolicy",
                    "s3:PutObject",
                    "s3:PutObjectAcl",
                    "s3:GetObject"
                ],
                "Resource": f"arn:aws:s3:::{bucket_name}/*",
            }
        ]
    }
    # Convert the policy to a string
    policy_string1 = json.dumps(policy_for_user)
    # Attach the policy to the IAM user
    response = iam.put_user_policy(
        UserName=user_name,
        PolicyName='S3BucketPolicy',
        PolicyDocument=policy_string1
    )
    print(f"Attached policy to user: {user_name}")
    print()
    # Create the bucket policy JSON
    bucket_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "AllowPutObject",
                "Effect": "Allow",
                "Principal": "*",
                "Action": [
                    "s3:PutObject",
                    "s3:PutObjectAcl",
                    "s3:GetObject"
                ],
                "Resource": f"arn:aws:s3:::{bucket_name}/*"
            }
        ]
    }
    # Convert the policy to a string
    policy_string2 = json.dumps(bucket_policy)
    # Set the bucket policy
    response = s3.put_bucket_policy(
        Bucket=bucket_name,
        Policy=policy_string2
    )
    print("Set bucket policy successfully")
    print()

def list_files_in_bucket(bucket_name):
    s3 = boto3.client('s3')
    response = s3.list_objects_v2(Bucket=bucket_name)
    if 'Contents' in response:
        for obj in response['Contents']:
            file_name = obj['Key']
            file_url = f"https://{bucket_name}.s3.amazonaws.com/{file_name}"
            print("File Name:", file_name)
            print("File URL:", file_url)
            print()
    else:
        print("No files found in the bucket")

    
