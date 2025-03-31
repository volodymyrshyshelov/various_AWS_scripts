import boto3
lambda_client = boto3.client('lambda')                                      #Create a client for the lambda service

#Get Lambda Functions name function
def get():                          
    response = lambda_client.list_functions()                               #Get all the Lambda Functions
    functions = response['Functions']                                       #Get all the Lambda Functions
    function_names = [function['FunctionName'] for function in functions]   #Get the Lambda Functions names
    return function_names

#Delete Lambda Functions by name function
def delete():
    print("Removing Lambda Functions...")       
    functions = get()                                                       #Get all the Lambda Functions
    for function_name in functions:                                         #Delete all the Lambda Functions
        lambda_client.delete_function(FunctionName=function_name)           #Delete the Lambda Function by name
    print("Lambda functions removed successfully.") 