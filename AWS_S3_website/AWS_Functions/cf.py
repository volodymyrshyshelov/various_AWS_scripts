# cf.py
import boto3
import time

def create_cloudfront_distribution(bucket_name):
    cf = boto3.client('cloudfront')
    origin_id = 'S3-' + bucket_name
    distribution_config = {
        'Comment': 'My Calculator Distribution',
        'CallerReference': bucket_name,
        'DefaultRootObject': 'app/index.html',
        'Origins': {
            'Quantity': 1,
            'Items': [{
                'Id': origin_id,
                'DomainName': '{}.s3.amazonaws.com'.format(bucket_name),
                'S3OriginConfig': {
                    'OriginAccessIdentity': ''
                }
            }]
        },
        'DefaultCacheBehavior': {
            'TargetOriginId': origin_id,
            'ViewerProtocolPolicy': 'redirect-to-https',  # Измененное значение
            'MinTTL': 0,
            'ForwardedValues': {
                'QueryString': False,
                'Cookies': {
                    'Forward': 'none'
                }
            }
        },
        'Enabled': True
    }

    response = cf.create_distribution(DistributionConfig=distribution_config)
    distribution_id = response['Distribution']['Id']

    print('CloudFront distribution created:', distribution_id)

    # Ожидание завершения деплоя дистрибутива
    print('Waiting for CloudFront deployment...')
    while True:
        response = cf.get_distribution(Id=distribution_id)
        status = response['Distribution']['Status']
        if status == 'Deployed':
            break
        time.sleep(10)

    # Получение общедоступного URL дистрибутива
    domain_name = response['Distribution']['DomainName']
    url = 'https://' + domain_name

    print('CloudFront distribution deployed successfully.')
    print('URL:', url)

    return url
