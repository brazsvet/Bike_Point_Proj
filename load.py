from dotenv import load_dotenv
import boto3
import os

# access .env variables
load_dotenv()

AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')

# connect to AWS user
s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

# list all files in the data folder
files_to_upload = os.listdir('data')

# uploading all the files from data folder to s3 bucket
for file in files_to_upload:
    filename_s3 = file
    file_to_upload = f'data/{file}'
    try:
        s3_client.upload_file(file_to_upload, AWS_BUCKET_NAME, filename_s3)
        print(f'File uploaded successfully: {file}')
        os.remove(file_to_upload)
    except Exception as e:
        print(f'An error occurred: {e}')

