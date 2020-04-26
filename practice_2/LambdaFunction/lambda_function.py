import json
import boto3

def lambda_handler(event, context):
    client = boto3.client('ecs')
    
    filename = event['Records'][0]['s3']['object']['key']
    
    if "_mini" in filename:
        return {
            'statusCode': 500,
            'body': json.dumps('Image already mini')
        }
    
    response = client.run_task(
        cluster='ImageResizeCluster',
        launchType = 'FARGATE',
        taskDefinition='ImageResizeTaskDefinition',
        count = 1,
        platformVersion='LATEST',
        networkConfiguration={
            'awsvpcConfiguration': {
                'subnets': [
                    'subnet-210d1046',
                    'subnet-2992b317',
                    'subnet-5d01d653',
                    'subnet-6c238e21',
                    'subnet-9aacb4b4',
                    'subnet-bb9688e7'
                ],
                'assignPublicIp': 'ENABLED'
            }
        },
        overrides={
            'containerOverrides': [
                {
                    'name': 'imageresize',
                    'command': [
                        '/app/resize.sh',
                        filename,
                        filename.split('.')[0] + '_mini.' + filename.split('.')[1]
                    ]
                }
            ],
            'taskRoleArn': 'arn:aws:iam::333041817134:role/S3_EC2ContainerService_FullAccessRol'
        },
    )
    
    return {
        'statusCode': 200,
        'body': str(response)
    }

