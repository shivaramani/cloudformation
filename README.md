##AWS Template Format Version

#Description
#Resources - MANDATORY #Section
#Metadata
#Parameters
#Mappings
#Conditions
#Outputs

# To run a cloud formation template to create a stack

# create a stack for S3 with a basic template
$ aws cloudformation create-stack --stack-name codeandtechsimples3 --template-body file://S3Basic.template

# create a stack for S3 with a Public Website policy, access control options 
$ aws cloudformation create-stack --stack-name codeandtechs3websitestack --template-body file://S3Publicwebsite.template

$ aws cloudformation create-stack --stack-name clickloggerstack --template-body file://APIBasic.template

# to update an existing stack - use "update-stack"
$ aws cloudformation update-stack --stack-name codeandtechs3websitestack --template-body file://S3Publicwebsite.template

# delete cloudformation stack for the provided stack name
$ aws cloudformation delete-stack --stack-name codeandtechsimples3 
$ aws cloudformation delete-stack --stack-name codeandtechs3websitestack 

ex: json

{
    "Resources":{
        "S3Bucket":{
            "Type": "AWS::S3::Bucket"
            "Properties":{
                "BucketName": "codeandtechcf"
            }
            
        }
    }
}

ex: with yaml

Resources:
  S3Bucket:
    Type: AWS::S3::Bucket
    Properties:
        Name: codeandtechcf