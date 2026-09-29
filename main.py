from modules.log_initialise import setup_logging
from modules.extract_function import extract_json
from datetime import datetime
import os

timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')

logger = setup_logging('log', timestamp)
logger.info('Logger successfully initialised')

# set up a retry settings in case if API fails
max_retry = 5
delay = 10

# create a forlder for the extracted data
data_dir = 'data'
os.makedirs(data_dir, exist_ok = True)

# API we want to extract data frpm
url = 'https://api.tfl.gov.uk/BikePoint/'

extract_json(url, data_dir, timestamp, max_retry, delay)