import os
import logging

def setup_logging(log_dir: str, timestamp:str):
    """This will initialise the logger.

    Args:
        log_dir (str): _description_
        timestamp (str): _description_
    """

    # create a folder for log files if it doesn't exist already
    os.makedirs(log_dir, exist_ok = True)

    log_filename = f'{log_dir}/{timestamp}.log'

    # configure logging so messages are written to the log file
    logging.basicConfig(
        filename = log_filename,
        format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level = logging.INFO
    )

    # create the logger and confirm that it has been successfully set up
    return logging.getLogger()
