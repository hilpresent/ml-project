# sys allows user to manipulate different parts of the python environment
# sys library helps handle exceptions
import sys
from src.logger import logging # this allows us to properly import logger so it WILL have __name__ == __main__ and the logs will be saved

# tells us error_detail information comes from the sys library
def error_message_detail(error, error_detail:sys):
    # gives us information on execution of most recent exception
    # we don't care about the first two parts of the info (hence "_, _,")
    # third part gives us info on which file and line number the exception occurred
    _, _, exc_tb = error_detail.exc_info()

    # get file name, line number, and error message
    # we know this from the python custom exception handling documentation
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = str(error)

    # format the error message
    error_message = f'Error occured in python script name [{file_name}] line number [{line_number}] error message [{error_message}]'

    return error_message

# creating custom exception class
# whenever we raise this custom exception, it is first inheriting the parent exception Exception
class CustomException(Exception):
    # constructor
    def __init__(self, error_message, error_detail:sys):
        # calls the parent class's __init__ method to initialize our Exception class
        # calls constructor of the parent class (`Exception`)
        # passes `error_message` to the `Exception` class to initialize the base exception with this message
        # allows custom exception to have all the standard properties and behavior of a normal Python exception, including storing the message
        super().__init__(error_message) # comes from self.error_message below
        
        # add additional properties to our custom exception class
        # calling the function above to get our custom formatted message
        # store detailed error message with file name and line number
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
        self.error_detail = error_detail

    # defines string representation of the custom exception
    # means when print() or str() is called on the exception, this method will be used to provide a human-readable string representation of the error object
    def __str__(self):
        return self.error_message
    
# check to ensure everything is working properly between custom exception handling and logging those errors
if __name__ == "__main__":
    # will only be executed if running directly, meaning not imported elsewhere
    try:
        a = 1/0 # will error out duh
    except Exception as e:
        logging.info('Divided by zero error')
        raise CustomException(e, sys)