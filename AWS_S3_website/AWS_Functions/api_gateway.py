import boto3

def create_api_gateway(api_name, lambda_arn):
    apigateway = boto3.client('apigateway')
    
    # Создание API Gateway
    response = apigateway.create_rest_api(
        name=api_name,
        description='Calculator API'
    )
    
    api_id = response['id']
    
    # Создание ресурса "/" (корневой путь)
    response = apigateway.get_resources(
        restApiId=api_id
    )
    root_resource_id = response['items'][0]['id']
    
    # Создание метода GET
    response = apigateway.put_method(
        restApiId=api_id,
        resourceId=root_resource_id,
        httpMethod='GET',
        authorizationType='NONE'
    )
    
    # Настройка интеграции метода GET с Lambda функцией
    response = apigateway.put_integration(
        restApiId=api_id,
        resourceId=root_resource_id,
        httpMethod='GET',
        type='AWS',
        integrationHttpMethod='POST',
        uri=lambda_arn
    )
    
    # Создание ресурса "/calculate"
    response = apigateway.create_resource(
        restApiId=api_id,
        parentId=root_resource_id,
        pathPart='calculate'
    )
    
    calculate_resource_id = response['id']
    
    # Создание метода POST
    response = apigateway.put_method(
        restApiId=api_id,
        resourceId=calculate_resource_id,
        httpMethod='POST',
        authorizationType='NONE'
    )
    
    # Настройка интеграции метода POST с Lambda функцией
    response = apigateway.put_integration(
        restApiId=api_id,
        resourceId=calculate_resource_id,
        httpMethod='POST',
        type='AWS',
        integrationHttpMethod='POST',
        uri=lambda_arn
    )
    
    # Публикация API Gateway
    response = apigateway.create_deployment(
        restApiId=api_id,
        stageName='prod'
    )
    
    
    # Получение общедоступного URL для доступа к API
    response = apigateway.get_stage(
        restApiId=api_id,
        stageName='prod'
    )
    
    url = response['invokeUrl']
    
    print('API Gateway URL:', url)

