################################################
#        Script to Remove AWS Resources        #
#     https://github.com/VladimirShyshelov     #
#             v1.0.0   2023/02/01              #
################################################


import boto3
from delete_functions import api_gateways                                     
from delete_functions import cloudfronts
from delete_functions import lambda_functions
from delete_functions import s3_buckets

# Get names of all Lambda functions, Api Gateways, S3 Buckets and CloudFronts

lambda_functions_list = lambda_functions.get()   
api_gateways_list = api_gateways.get()
s3_buckets_list = s3_buckets.get()
cloudfronts_list = cloudfronts.get()

# Print names for all Lambda functions, Api Gateways, S3 Buckets, and CloudFrontsYe

print("List of available Lambda functions:\n", "\n".join(lambda_functions_list))
print("\nList of available Api Gateways:\n", "\n".join(api_gateways_list))
print("\nList of available S3 Buckets:\n", "\n".join(s3_buckets_list))
print("\nList of available CloudFronts:\n", "\n".join(cloudfronts_list))

# Request to delete all Lambda functions, Api Gateways, S3 Buckets, and CloudFronts

answer = input("\nDo you want to remove all Lambda functions, Api Gateways, S3 Buckets and CloudFronts? (Yes/No): ")
if answer.lower() == 'yes':
    # Delete all Lambda functions, Api Gateways, S3 Buckets, and CloudFronts if the user types 'yes'
    lambda_functions.delete()
    api_gateways.delete(api_gateways_list)
    s3_buckets.delete()
    cloudfronts.delete()
    print("\nAll resources have been successfully removed.")
else:
    print("\nDeletion cancelled.")

