import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError

import pymysql

USER = "root"
PASSWORD = "flPyog?nL4Ww"
HOST = "127.0.0.1"
PORT = "3306"
DATABASE = "home_inventory_db"
TABLENAME = "order_products_prior"
# create the dataframe
final_df=pd.read_csv("order_products__prior.csv")
engine = create_engine(f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}")
# try:
#     engine.execute(f"CREATE DATABASE {DATABASE}")
# except ProgrammingError:
#     warnings.warn(
#         f"Could not create database {DATABASE}. Database {DATABASE} may already exist."
#     )
#     pass
engine.execute(f"USE {DATABASE}")
engine.execute(f"DROP TABLE IF EXISTS {TABLENAME}")
final_df.to_sql(name=TABLENAME, con=engine)