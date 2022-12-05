import pandas as pd
from sensor.config import mongo_client
from sensor.logger import logging
from sensor.exception import SensorException
import yaml
import os, sys

def get_collection_as_dataframe(database_name:str, collection_name:str ):
    """
    Description: This function return collection as DataFrame
    ========================================================================
    Params
    database_name: 
    collection_name:
    =========================================================================
    return Pandas DataFrame of collection 
    """

    try:
        logging.info(f'Reading data from the database {database_name} and collection is {collection_name}')
        df = pd.DataFrame(list(mongo_client[database_name][collection_name].find()))
        logging.info(f"Found column: {df.columns}")
        if '_id' in df.columns:
            logging.info('Droppig the column: _id')
            df = df.drop('_id' , axis = 1)
        logging.info(f'Row and column in df: {df.shape}')
        return df
        
    except Exveption as e:
        raise SensorException(e, sys)

def write_ymal_file(file_path , data:dict):
    try:
        file_dir = os.path.dirname(file_path)

        os.makedirs(file_dir, exist_ok = True)
        with open (file_path, 'w') as file_writer:
            yaml.dump(data, file_writer)
            
    except Exception as e:
        raise SensorException(e, sys)


def convert_columns_float(df:pd.DataFrame , exclude_col:list):
    try:
        for column in df.columns:
            if column not in exclude_col:
                df[column] = df[column].astype('float')
        return df
    except Exception as e:
        raise SensorException(e, sys)
