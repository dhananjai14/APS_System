import pandas as pd
from sensor.config import mongo_client
from sensor.logger import logging
from sensor.exception import SensorException


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