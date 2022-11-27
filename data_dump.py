import pymongo
import pandas as pd
import json

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

file_path = r'/config/workspace/aps_failure_training_set1.csv'
database_name = 'aps'
collection_name = 'sensor'

if __name__ == '__main__':
    df = pd.read_csv(file_path)
    print(f'row and columns: {df.shape[0]} rows and {df.shape[1]} columns')
    
    # Convert dataframe into JSON
    df.reset_index(drop = True, inplace = True)

    json_record = list(json.loads(df.T.to_json()).values())

    client[database_name][collection_name].insert_many(json_record)
