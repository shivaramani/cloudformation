import json
import boto3
import datetime
import os

bucket_name = "clickstreamlogger-lambda"
table_name = "clickstreamlogger1"

def lambda_handler(event, context):

    print("Entering the lambda handler")
    responseString = ""

    now = datetime.datetime.now()
    unique_key = now.strftime("%M") + "-" + now.strftime("%D") + "-" + now.strftime("%Y") + "-" + now.strftime("%H") + "-" + now.strftime("%M") + "-" + now.strftime("%s")
    logText = "Test Message " + unique_key

    # Check S3 buckets. If not create the bucket and insert the data into the bucket
    try:
        s3 = boto3.client('s3')
        

        bucketExist  = False
        bucketList = s3.list_buckets()

        for bucket in bucketList["Buckets"]:
            if(bucket["Name"] == bucket_name):
                bucketExist = True
                print("Bucket Exist")
                break
            else:
                print("Bucket Name - " + bucket["Name"])

        if bucketExist == False:
            s3.create_bucket(Bucket=bucket_name, 
                             CreateBucketConfiguration = {'LocationConstraint': 'us-west-2'}
                            )
            print("Created bucket " + bucket_name + " Successfully !!!")

        s3.put_object(Body=logText, Bucket=bucket_name, Key=unique_key)    

        responseString = "Data into S3 Successfully"

        print(responseString)

    except Exception as e:
        print("Error occurred - " + str(e))
        responseString = "Error occured while inserting into S3"


    # Get Dynamo DB Tables and insert the insert_emoticon
    try:
        dynamodb = boto3.resource('dynamodb')
        dbTable = dynamodb.Table(table_name)
        print("Created DB instance for the table - " + table_name)

        dbTable.put_item(
            Item={
                'correlationid': unique_key,
                'message': logText,
                'dateTime': now.strftime("%C")
            }
        )
        responseString = responseString + " Data into DynamoDB Successfully"
        print(responseString)
    except Exception as e:
        print("Error Occured inserting into DynamoDB - " +str(e))
        responseString = responseString + " Error occured while inserting into DynamoDB"

    response = {
        "statusCode": "200",
         "headers": { "Access-Control-Allow-Origin": "*"},
        "body": json.dumps(responseString)
    }

    return response;


lambda_handler("", "")