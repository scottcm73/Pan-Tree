import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError

import pymysql

USER = "root"
PASSWORD = "flPyog?nL4Ww"
HOST = "127.0.0.1"
PORT = "3306"
DATABASE = "the_home_inventory"





#create the dataframe

engine = create_engine(f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}")
try:
    engine.execute(f"CREATE DATABASE {DATABASE}")
except ProgrammingError:
    warnings.warn(
        f"Could not create database {DATABASE}. Database {DATABASE} may already exist."
    )
    pass
engine.execute(f"USE {DATABASE}")
tables_list=["order_products_prior", "order_products_train", "orders", "products"]
csv_list=["order_products__prior.csv","order_products__train.csv", "orders.csv", "products.csv"]

def make_df:
    df=pd.read_csv(csv)
    return df

def make_table(TABLENAME):
    engine.execute(f"DROP TABLE IF EXISTS {TABLENAME}")
    df.to_sql(name=TABLENAME, con=engine)
    return

for csv in csv_list:
    for TABLENAME in tables_list:
        make_df(csv)
        make_table(TABLENAME)




    
