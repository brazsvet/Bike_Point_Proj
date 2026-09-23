# import packages
import os
import json
import requests
from datetime import datetime

# API we want to extract data frpm
url = 'https://api.tfl.gov.uk/BikePoint/'

# create a forlder for the extracted data
data_dir = 'data'
os.makedirs(data_dir, exist_ok = True)

# create a timestamp so each extract gets a unique filename
timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
filename = f'{data_dir}/{timestamp}.json'

# send a GET request to the API
response = requests.get(url)

# get status
status = response.status_code

# 

# convert the json response into python variable
data = response.json()

# open the output file and write the API data to it as json
with open(filename, 'w') as file:
    json.dump(data, file)