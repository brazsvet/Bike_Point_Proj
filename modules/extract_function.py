# import packages
import os
import json
import requests
from datetime import datetime
import time
import logging

# making a log when the script is ran
logger = logging.getLogger(__name__)

def extract_json(url:str, data_dir:str, timestamp:str, max_retry:int, delay:int):
    """Extracts .json from specified url and saves it locally in the data_dir

    Args:
        url (str): _description_
        data_dir (str): _description_
        timestamp (str): _description_
        max_retry (int): _description_
        delay (int): _description_
    """

    # create a forlder for the extracted data
    os.makedirs(data_dir, exist_ok = True)

    filename = f'{data_dir}/{timestamp}.json'

    # set up a retry settings in case if API fails
    attempt = 0

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

    

