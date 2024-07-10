# import because we will be using the custom exception we built
import os
import sys

# import custom packages
from src.exception import CustomException
from src.logger import logging

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass # used to create class variables

# data ingestion configuration
# this config will be used to set up paths for the data ingestion component
@dataclass # we will use this decorator here
class DataIngestionConfig:
    # paths to save output data in artifacts folder
    train_data_path:str = os.path.join('artifacts', 'train.csv')
    eval_data_path:str = os.path.join('atrifacts', 'eval.csv')
    test_data_path:str = os.path.join('artifacts', 'test.csv')
    raw_data_path:str = os.path.join('artifacts', 'data.csv')

    # note: @dataclass decorator auto generates the __init__() method,
    # so we don't have to manually define it or use `self` to assign params to instance variables

# if you're only defining vars, can use @dataclass decorator
# if adding additional functions, it's good practice to add the __init__() method and use `self` to assign params to instance variables
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig() # when this gets initiated, 3 paths above get saved in "ingestion_config" variable

    # if your data is stored in databases, this is where you would write the code to read that in
    def initiate_data_ingestion(self):
        logging.info('Entered the data injection method or component')
        try:
            df = pd.read_csv('project_ml-project/notebook/data/student_performance.csv')
            logging.info('Read the dataset as a dataframe')

            # make artifact directory for the paths above
            # os.path.dirname gets the directory name from `self.ingestion_config.train_data_path`, so in this case (as of when I write this) it will be "artifacts"
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True) # exist_ok = True means if it already exists, we won't overwrite and start fresh

            # save data to a csv file for the raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info('Train test split initiated')
            train_set, placeholder_set = train_test_split(df, test_size=0.3, random_state=42)
            test_set, eval_set = train_test_split(placeholder_set, test_size=0.5, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            eval_set.to_csv(self.ingestion_config.eval_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info('Ingestion of the data is complete')

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.eval_data_path,
                self.ingestion_config.test_data_path,
            )
        except Exception as e:
            raise CustomException(e, sys)