# aws
operations on aws through boto3

awskeygenerator.py - create a new key for any given if its in speicified limit of 2. It also encrypts the keys and store it in a file.

awskeysinactive.py - disables the keys based on its age. if its created before 90 days, it inactivates the key of any specified account

awsinactivekeysdelete.py - disables the keys which are inactive and older than 90 days. 

s3_file_upload.py - sample application to use the encrypted key file and upload a sample file to S3 bucket. 
