import json
import aws_lambda_powertools.event_handler
import aws_lambda_powertools.shared
import aws_lambda_powertools.shared.types
import aws_lambda_powertools.utilities
from aws_lambda_powertools.utilities.data_classes import APIGatewayProxyEvent
from aws_lambda_powertools.utilities.typing import LambdaContext
import boto3
import aws_lambda_powertools

# Annahme, der Tischname heißt MyTable
table = boto3.resource('dynamodb').Table('MyTable')

def handler(event: APIGatewayProxyEvent, context: LambdaContext):

    print(event.body)
    return {
        'statusCode': 200,
        'body': json.dumps('Eintrag erfolgreich hinzugefügt')
    }