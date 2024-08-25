import os
import sys  
from src.exception import  CustomException
from src.logger import logging
import pandas as pd 
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
import stat
from src.components.data_transformation import DataTransformation 
from src.components.data_transformation import DataTransformationConfig

from src.components.model_trainer import ModelTrainer



#where to save training path , train data , raw data 
## this decorater helps us to use the class variable without having to use init

@dataclass
class DataIngestionConfig:
    ## train data would be saved in a folder created called artifact by the name of train.cav
    train_data_path = os.path.join("artifact","train.csv")
    test_data_path = os.path.join("artifact","test.csv")
    raw_data_path = os.path.join("artifact", "data,csv")
    
    
## now the data ingestion component knows where to store the train test and raw files

class DataIngestion:
    ## when we have multiple functions in a class choose the init method 
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        # when executed inside this object we would have the train_Data_path and test_data_path , raw_data_path these 3 variables
        
    def initiate_data_ingestion(self):
        logging.info("initiate the data ingestion method")
        try:
            df = pd.read_csv("notebook\data\stud.csv")
            logging.info("reada dataset as dataframe")
            df.to_csv(self.ingestion_config.raw_data_path, header= True, index = False)
            
            logging.info("train test split initiated")
            train_set, test_set = train_test_split(df, test_size= 0.2, random_state=42)
            df.to_csv(self.ingestion_config.train_data_path, header= True, index = False)
            df.to_csv(self.ingestion_config.test_data_path, header= True, index = False)
            logging.info("ingestion completed")
            
            
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)
            
             
if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()
    
    data_transformation = DataTransformation()
    train_arr,test_arr,_ = data_transformation.initiate_data_transformation(train_data, test_data)
    
    modeltrainer = ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr, test_arr))
    
    
                
                
                