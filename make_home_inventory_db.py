import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError
import os
import warnings
import pymysql

USER = "root"
PASSWORD = "flPyog?nL4Ww"
HOST = "127.0.0.1"
PORT = "3306"
DATABASE = "home_inventory_db"





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

def make_df(csv):
    this_csv=os.path.join("resources", csv)
    df=pd.read_csv(this_csv)
    return df

def make_table(TABLENAME, df):
    engine.execute(f"DROP TABLE IF EXISTS {TABLENAME}")
    df.to_sql(name=TABLENAME, con=engine)
    return

for csv in csv_list:
    for TABLENAME in tables_list:
        
        df=make_df(csv)
        make_table(TABLENAME, df)

'''This creates four tables and the home_inventory database. In SQLWorkbench order_products_train is added to order_products_prior.'''


    
