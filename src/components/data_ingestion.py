import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts','train.csv')
    test_data_path: str = os.path.join('artifacts','test.csv')
    raw_data_path: str = os.path.join('artifacts','data.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("The method got successfully executed via data ingestion function")
        try:
            df = pd.read_csv('notebook/data/stud.csv')
            logging.info("Data read sucessfully as a DataFrame")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info("Train test initiated")

            train_set, test_set = train_test_split(df, test_size=0.20, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            logging.info("Train data created sucessfully")

            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info("Test data created sucessfully")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)
        

if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()

