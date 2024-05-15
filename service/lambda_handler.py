import json
import boto3

# Annahme, der Tischname heißt MyTable
table = boto3.resource('dynamodb').Table('MyTable')

def handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Eintrag erfolgreich hinzugefügt')
    }