import json
import aws_lambda_powertools.event_handler
import aws_lambda_powertools.shared
import aws_lambda_powertools.shared.types
import aws_lambda_powertools.utilities
from aws_lambda_powertools.utilities.data_classes import APIGatewayProxyEvent, APIGatewayProxyEventV2
from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools import Logger
import boto3
import aws_lambda_powertools

# Annahme, der Tischname heißt MyTable
table = boto3.resource('dynamodb').Table('MyTable')

logger = Logger()

@logger.inject_lambda_context
def handler(event, context):
    event = APIGatewayProxyEventV2(event)
    logger.info(event.json_body)
    logger.info("Test")
    return {
        'statusCode': 200,
        'body': json.dumps('Eintrag erfolgreich hinzugefügt')
    }