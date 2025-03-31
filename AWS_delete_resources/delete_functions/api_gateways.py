import boto3

#Get Api Gateways name function
def get(): 
    api_gateway_client = boto3.client('apigateway')                 #Create a client for the apigateway service
    response = api_gateway_client.get_rest_apis()                   #Get all the Api Gateways
    apis = response['items']                                        #Get the Api Gateways list
    api_names = [api['name'] for api in apis]                       #Get the Api Gateways names
    return api_names                                                #Return the Api Gateways names list


#Delete Api Gateways by name function 
def delete(api_gateways_list): 
    print("Removing Api Gateways...") 
    api_gateway_client = boto3.client('apigateway')                #Create a client for the apigateway service
    for api_name in api_gateways_list:                             #Delete all the Api Gateways
        response = api_gateway_client.get_rest_apis()              #Get all the Api Gateways
        api_id = None                                              #Set the Api Gateway id to None
        for api in response['items']:                              #Get the Api Gateway id
            if api['name'] == api_name:                            #If the Api Gateway name is equal to the Api Gateway name in the list
                api_id = api['id']                                 #Set the Api Gateway id
                break                        
        if api_id:                                                 #If the Api Gateway id is not None
            api_gateway_client.delete_rest_api(restApiId=api_id)   #Delete the Api Gateway by id
    print("Api Gateways removed successfully.")
    