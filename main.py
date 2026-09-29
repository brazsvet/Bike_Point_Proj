from modules.log_initialise import setup_logging
from modules.extract_function import extract_json
from modules.load_function import load_files_to_s3
from datetime import datetime
import os
from dotenv import load_dotenv

timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')

# set up the logger
logger = setup_logging('log', timestamp)
logger.info('Logger successfully initialised')

# API we want to extract data frpm
url = 'https://api.tfl.gov.uk/BikePoint/'

# set up a retry settings in case if API fails
max_retry = 5
delay = 10

# create a forlder for the extracted data
data_dir = 'data'
os.makedirs(data_dir, exist_ok = True)

# call the extracting function
extract_json(url, data_dir, timestamp, max_retry, delay)

# access .env variables
load_dotenv()

AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')

# call the uploading function to upload data from locally saved to s3 bucket
load_files_to_s3(data_dir, AWS_ACCESS_KEY, AWS_SECRET_ACCESS_KEY, AWS_BUCKET_NAME)