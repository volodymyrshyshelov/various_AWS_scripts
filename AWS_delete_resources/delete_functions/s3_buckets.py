import boto3

def get():
    s3_client = boto3.client('s3')                                           #Create a client for the s3 service
    response = s3_client.list_buckets()                                      #Get all the S3 Buckets
    buckets = response['Buckets']                                               
    bucket_names = [bucket['Name'] for bucket in buckets]                    #Get the S3 Buckets names
    return bucket_names                                                      #Return the S3 Buckets names list

def delete():
    print("Removing S3 Buckets...")
    s3_client = boto3.client('s3')                                           #Create a client for the s3 service
    buckets = get()                                                          #Get all the S3 Buckets
    for bucket_name in buckets:                                              #Delete all the S3 Buckets
        response = s3_client.list_objects_v2(Bucket=bucket_name)             #Get all the S3 Buckets objects
        objects = response.get('Contents', [])                               #Get the S3 Buckets objects list
        for obj in objects:                                                  #Delete all the S3 Buckets objects
            s3_client.delete_object(Bucket=bucket_name, Key=obj['Key'])      #Delete all the S3 Buckets objects
        s3_client.delete_bucket(Bucket=bucket_name)                          #Delete the S3 Bucket by name
    print("S3 Buckets have been successfully deleted.")