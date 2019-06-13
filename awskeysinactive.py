import boto3
import time
import datetime

account = "dev_s3_account"

# credentails for admin account
# aws_access_key_id = ""
# aws_secret_access_key = ""

# iam = boto3.client('iam', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
iam = boto3.client('iam')

# List access keys through the pagination interface.
paginator = iam.get_paginator('list_access_keys')
for response in paginator.paginate(UserName=account):
    print(response)

deactivate_accounts = []
no_of_days = 90
for d in response['AccessKeyMetadata']:
    accesskeydate = d['CreateDate']
    accesskeydate = accesskeydate.strftime("%Y-%m-%d %H:%M:%S")
    currentdate = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())

    accesskeyd = time.mktime(datetime.datetime.strptime(accesskeydate, "%Y-%m-%d %H:%M:%S").timetuple())
    currentd = time.mktime(datetime.datetime.strptime(currentdate, "%Y-%m-%d %H:%M:%S").timetuple())
    active_days = (currentd - accesskeyd) / 60 / 60 / 24  ### We get the data in seconds. converting it to days

    print d['AccessKeyId'] + " account is " + str(active_days) + " old"

    if active_days > no_of_days:
        deactivate_accounts.append(d['AccessKeyId'])

print deactivate_accounts
for keyid in deactivate_accounts:
    print(keyid)
    iactive = iam.update_access_key(UserName=account, AccessKeyId=keyid, Status='Inactive')
    print(iactive)
