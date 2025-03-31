import boto3
import time
from datetime import datetime,timedelta
import sys

#Get CloudFronts id function
def get():
    cloudfront_client = boto3.client('cloudfront')                              #Create a client for the cloudfront service
    response = cloudfront_client.list_distributions()                           #Get all the CloudFronts
    distributions = response.get('DistributionList', {}).get('Items', [])       #Get the CloudFronts list
    distribution_ids = [distribution['Id'] for distribution in distributions]   #Get the CloudFronts ids
    return distribution_ids                                                     #Return the CloudFronts ids list

#Delete CloudFronts by id function
def delete():
    client = boto3.client('cloudfront')                                         #Create a client for the cloudfront service
    distributions = client.list_distributions()                                 #Get all the CloudFronts
        
    if distributions['DistributionList']['Quantity'] == 0:                      #If there are no CloudFronts
        print("There are no CloudFront distributions available. Exit.")     
        sys.exit(1) 
    print("Uninstalling CloudFront...") 
    
    distribution = distributions['DistributionList']['Items'][0]              
    dist_id = distribution['Id']                                                #Get the CloudFront id
    current_conf = client.get_distribution_config(Id=dist_id)                   #Get the CloudFront configuration
    disabledConf = current_conf['DistributionConfig']   
    disabledConf['Enabled'] = False                                             #Disable the CloudFront
    client.update_distribution(                                                             
        DistributionConfig=disabledConf,                                        #Update the CloudFront configuration                                          
        Id=dist_id,                                                             #Update the CloudFront id
        IfMatch=current_conf['ETag']                                            #Update the CloudFront ETag
    )    
    print("Waiting for distribution shutdown... This may take some time....")
    timeout_mins = 60                                                           #Set the timeout to 60 minutes
    wait_until = datetime.now() + timedelta(minutes=timeout_mins)               #Set the time to wait until
    notFinished = True                                                          #Set the notFinished flag to True
    eTag = ""                                                                   #Set the ETag to empty

    while notFinished:  

        if wait_until < datetime.now():                                         #If the time to wait until is less than the current time
            print("Distribution shutdown is to long. Exit.")
            sys.exit(1)     
        status = client.get_distribution(Id=dist_id)                            #Get the CloudFront status

        if (
            status['Distribution']['DistributionConfig']['Enabled'] == False    #If the CloudFront is disabled
            and status['Distribution']['Status'] == 'Deployed'                  #If the CloudFront is deployed
        ):
            eTag = status['ETag']                                               #Set the ETag
            notFinished = False                                                 #Set the notFinished flag to False
        print("The process has not been completed. Waiting 60 seconds....")
        time.sleep(60)                                                          #Wait 60 seconds
    client.delete_distribution(Id=dist_id, IfMatch=eTag)                        #Delete the CloudFront by id
    print("CloudFront was successfully uninstalled.")                           #Print the success message