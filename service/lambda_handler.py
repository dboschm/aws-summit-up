import json
import boto3

# Annahme, der Tischname heißt MyTable
table = boto3.resource('dynamodb').Table('MyTable')

def handler(event, context):
    # Beispiel, wie man Daten in DynamoDB schreibt
    response = table.put_item(
       Item={
            'id': event['pathParameters']['id'],
            'data': event['body']
        }
    )
    return {
        'statusCode': 200,
        'body': json.dumps('Eintrag erfolgreich hinzugefügt')
    }