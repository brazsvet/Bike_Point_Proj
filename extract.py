# import packages
import os
import json
import requests
from datetime import datetime
import time
import logging

# API we want to extract data frpm
url = 'https://api.tfl.gov.uk/BikePoint/'

# create a forlder for the extracted data
data_dir = 'data'
os.makedirs(data_dir, exist_ok = True)

# create a timestamp so each extract gets a unique filename
timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
filename = f'{data_dir}/{timestamp}.json'

# create a folder for log files if it doesn't exist already
log_dir = 'log'
os.makedirs(log_dir, exist_ok = True)
log_filename = f'{log_dir}/{timestamp}.json'

# configure logging so messages are written to the log file
logging.basicConfig(
    filename = log_filename,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    level = logging.INFO
)

# create the logger and confirm that it has been successfully set up
logger = logging.getLogger()
logger.info('Logger successfully initialised')

# set up a retry settings in case if API fails
max_retry = 5
attempt = 0
delay = 10

# keep trying until the maximum number of attempts or the succesfull extraction
while attempt < max_retry:

    # send a GET request to the API
    response = requests.get(url)

    # get status
    status = response.status_code

    # if statement based on the status code
    if 200 <= status < 300:
        # convert the json response into python variable
        data = response.json()

        # check if the API returned the data
        if len(data) > 0:
            try:
                # open the output file and write the API data to it as json
                with open(filename, 'w') as file:
                    json.dump(data, file)

                # print the success comment and break the loop
                print(f'File {filename} was successfully saved')
                logger.info(f'File {filename} was successfully saved')
                
            except Exception as e:
                print(f'An error has occured: {e}')
                logger.error(f'An error has occured: {e}')
        # API request was succesfull, but no data recieved
        else:
            print('No data returned')
            logger.warning('No data returned')
        break

    # elif statement for the errors
    elif status < 200 or status >= 500:
        time.sleep(delay)
        attempt += 1
        print(f'Status code: {status}. Retrying. Attempt number {attempt}')
        logger.info(f'Status code: {status}. Retrying. Attempt number {attempt}')

    # all other errors
    else:
        print(f'Error. Status code: {status}')
        logger.critical(f'Error. Status code: {status}')
        break

    

