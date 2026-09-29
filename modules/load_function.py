from dotenv import load_dotenv
import boto3
import os
import logging

# create logger and confirm that it was successfully set up
logger = logging.getLogger(__name__)

def load_files_to_s3(data_dir:str, AWS_ACCESS_KEY:str, AWS_SECRET_ACCESS_KEY:str, AWS_BUCKET_NAME:str):
    """Upload all the files in the directory to the s3 bucket.

    Args:
        data_dir (str): _description_
        AWS_ACCESS_KEY (str): _description_
        AWS_SECRET_ACCESS_KEY (str): _description_
        AWS_BUCKET_NAME (str): _description_
    """

    # connect to AWS user
    s3_client = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )

    # list all files in the data folder
    files_to_upload = os.listdir(data_dir)
    logger.info(f'Files in the data forlder: {len(files_to_upload)}')

    # uploading all the files from data folder to s3 bucket
    for file in files_to_upload:
        filename_s3 = file
        file_to_upload = f'{data_dir}/{file}'
        try:
            s3_client.upload_file(file_to_upload, AWS_BUCKET_NAME, filename_s3)
            print(f'File uploaded successfully: {file}')
            logger.info(f'File uploaded successfully: {file}')
            os.remove(file_to_upload)
            logger.info(f'File removed locally: {file}')
        except Exception as e:
            print(f'An error occurred: {e}')
            logger.error(f'An error occurred: {e}')

