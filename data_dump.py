import pymongo
import pandas as pd
import json
client =  pymongo.MongoClient("mongodb://localhost:27017/")

DATAFILE_PATH = r"C:\Users\Ranjeet\ML Projects\apps-fault-detetcion\workplace\aps_failure_training_set1.csv"
DATABASE_NAME = "APS"
COLLECTION_NAME = "sensor"

if __name__ == "__main__":
    df =  pd.read_csv(DATAFILE_PATH)
    print(f"Rows & Col :{df.shape}")
    
    # convert dataframe into JSON
    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())

    print(json_record[0])

    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)



