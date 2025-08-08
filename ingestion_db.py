import pandas as pd 
import os 
from sqlalchemy import create_engine
import time
import logging

logging.basicConfig(
    filename="logs/ingestion_db.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)
engine =create_engine ('sqlite:///inventory.db')
def ingest_db(df, table_name, engine):
    ''' this function will ingest the dataframe into the database tables'''
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
def load_raw_data(): 
    ''' this function will load csv as dataframe and ingest into db'''
    start=time.time()
    for file in os.listdir(r'C:\Users\kakan\Downloads\data\data'):
        if '.csv' in file :
            df=pd.read_csv(r'C:\Users\kakan\Downloads\data\data\\'+ file)
            logging.info(f'ingesting{file} in db')
            ingest_db(df, file[:-4], engine)
    end=time.time()
    total_time=(end-start)/60
    logging.info("ingestion complete")
    logging.info(f"total_time_taken:{total_time} minutes")
if __name__=='__main__':
    load_raw_data()