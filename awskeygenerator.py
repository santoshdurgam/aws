import boto3
import base64

account = "dev_s3_account"

# credentails for admin account
# aws_access_key_id = ""
# aws_secret_access_key = ""

# iam = boto3.client('iam', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
iam = boto3.client('iam')

response = iam.create_access_key(UserName=account)
print response
print "Key created for the account"
print response['AccessKey']['AccessKeyId']

str_aws_access_key_id = response['AccessKey']['AccessKeyId']
str_aws_secret_access_key = response['AccessKey']['SecretAccessKey']
f = open("key.properties", "w")
f.write("aws_access_key_id = " + str_aws_access_key_id.encode('base64'))
f.write("aws_secret_access_key = " + str_aws_secret_access_key.encode('base64'))
f.close()





