import json

def lambda_handler(event, context):
    responseText = "Sample response from lambda"

    response = {
        "statusCode": "200",
        "headers": { "Access-Control-Allow-Origin": "*" },
        "body": responseText
    }

    return response