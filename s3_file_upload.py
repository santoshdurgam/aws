import logging
import boto3
from botocore.exceptions import ClientError
import datetime
import base64
import ConfigParser


def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

file_name = "sample_txt_file.txt"
s3_bucket_name = "s3_dev_bucket"

from pyjavaproperties import Properties
p = Properties()
p.load(open('key.properties'))

print p['aws_access_key_id']
print p['aws_secret_access_key']

aws_access_key_id = base64.b64decode(p['aws_access_key_id'])
aws_secret_access_key = base64.b64decode(p['aws_secret_access_key'])



# s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
s3 = boto3.client('s3')

with open(file_name, "rb") as f:
    new_file_name = file_name + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    s3.upload_fileobj(f, s3_bucket_name, new_file_name)
print "file moved successfully "+ new_file_name




