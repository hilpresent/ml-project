import logging
import os
from datetime import datetime

# allows us to log and see information on all of the code we are executing
# helps with debugging and tracking errors
LOG_FILE = f'{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log'

# name will first get current working directory
# name will then get the string "logs"
# finally name will end with the naming convention to indicate the time of the log
logs_path = os.path.join(os.getcwd(), 'logs', LOG_FILE)

# create directory
# `exist_ok` means if directory already exists, keep appending new files to it
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)


# configure the logging module
# `filename` tells us the file to log messages to (our LOG_FILE_PATH)
# `format` sets the format for log messages
# `level` sets the logging level (INFO in this case)
logging.basicConfig(
    filename=LOG_FILE_PATH, # log messages saved to this file
    format="[ %(acstime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s", # this is considered best practice
    level=logging.INFO, # will log messages with level INFO and higher (INFO, WARNING, ERROR, CRITICAL)
)