from dotenv import load_dotenv
import boto3
import os

# access .env variables
load_dotenv()

AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')

# connect to s3 bucket
s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

file_to_upload = 'data/2026-09-23 17-01-47.json'
filename_s3 = '2026-09-23 17-01-47.json'

# upload data to s3 bucket
s3_client.upload_file(file_to_upload, AWS_BUCKET_NAME, filename_s3)