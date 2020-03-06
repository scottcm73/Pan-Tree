import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError
<<<<<<< HEAD
=======
import os
>>>>>>> 78977ff45b40d147ab026624c2545578e0e1c21e
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
<<<<<<< HEAD
tables_list=["aisles", "departments", "products", 
            "order_products_prior", "order_products_train", "orders"]
csv_list=["aisles.csv", "departments.csv", "products.csv", 
            "order_products__prior.csv","order_products__train.csv", "orders.csv"] 


def make_df(csv):
    this_csv=os.path.join("Resources", csv)
    df=pd.read_csv(this_csv, encoding='ISO 8859-1')
=======
tables_list=["order_products_prior", "order_products_train", "orders", "products"]
csv_list=["order_products__prior.csv","order_products__train.csv", "orders.csv", "products.csv"]

def make_df(csv):
    this_csv=os.path.join("resources", csv)
    df=pd.read_csv(this_csv)
>>>>>>> 78977ff45b40d147ab026624c2545578e0e1c21e
    return df

def make_table(TABLENAME, df):
    engine.execute(f"DROP TABLE IF EXISTS {TABLENAME}")
<<<<<<< HEAD
    df.to_sql(name=TABLENAME, con=engine, if_exists='replace')
    return

for x in range (0, len(csv_list)):
    df=make_df(csv_list[x])
    TABLENAME=tables_list[x]
    make_table(TABLENAME, df)


=======
    df.to_sql(name=TABLENAME, con=engine)
    return

for csv in csv_list:
    for TABLENAME in tables_list:
        
        df=make_df(csv)
        make_table(TABLENAME, df)

'''This creates four tables and the home_inventory database. In SQLWorkbench order_products_train is added to order_products_prior.'''
>>>>>>> 78977ff45b40d147ab026624c2545578e0e1c21e


    
