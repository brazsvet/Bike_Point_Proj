from dotenv import load_dotenv
import boto3
import os
import logging
from datetime import datetime

# create a folder for log files if it doesn't exist already
timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
log_dir = 'log'
os.makedirs(log_dir, exist_ok = True)
log_filename = f'{log_dir}/load_{timestamp}.log'

# configure logging so messages are written to the log file
logging.basicConfig(
    filename = log_filename,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    level = logging.INFO
)

# create the logger and confirm that it has been successfully set up
logger = logging.getLogger()
logger.info('Logger successfully initialised')

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
logger.info(f'Files in the data forlder: {len(files_to_upload)}')

# uploading all the files from data folder to s3 bucket
for file in files_to_upload:
    filename_s3 = file
    file_to_upload = f'data/{file}'
    try:
        s3_client.upload_file(file_to_upload, AWS_BUCKET_NAME, filename_s3)
        print(f'File uploaded successfully: {file}')
        logger.info(f'File uploaded successfully: {file}')
        os.remove(file_to_upload)
        logger.info(f'File removed locally: {file}')
    except Exception as e:
        print(f'An error occurred: {e}')
        logger.error(f'An error occurred: {e}')

