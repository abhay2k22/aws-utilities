import re
import json
import traceback
import boto3

#s3_resource = boto3.resource('s3')
s3_client = boto3.client('s3')
dynamodb_client = boto3.client('dynamodb')
dynamodb_resource = boto3.resource('dynamodb')
table_name = 's3_lambda_test'

def lambda_handler(event, context):
    print(str(event))
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_name = event['Records'][0]['s3']['object']['key']
    print("bucket_name=%s, object_name=%s" %(bucket_name,object_name))

    json_object = s3_client.get_object(Bucket=bucket_name,Key=object_name)
    json_file_reader = json_object['Body'].read()
    jsonDict = json.loads(json_file_reader)
    print(jsonDict)

    dynamodb_table = dynamodb_resource.Table(table_name)
    #dynamodb_client.put_item(TableName=table_name, Item=jsonDict)
    dynamodb_table.put_item(Item=jsonDict)
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Lambda Test completed!')
    }
