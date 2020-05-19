import csv
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError
import warnings
import sqlalchemy
import numpy as np
import os

# Importing dependencies for scraping
import requests
from bs4 import BeautifulSoup

my_password = "Bakken11"
DIALECT = 'mysql'
DRIVER = 'pymysql'
USER = "root"
PASSWORD = my_password
HOST = "127.0.0.1"
PORT = "3306"
DATABASE = "datascm2_home_inventory_db"

###################################################################
#                 Database Connection to MySQL                    #
###################################################################
engine = create_engine(f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}")
try:
    engine.execute(f"CREATE DATABASE {DATABASE}")
except ProgrammingError:
    warnings.warn(
        f"Could not create database {DATABASE}. Database {DATABASE} may already exist."
    )
    pass
engine.execute(f"USE {DATABASE}")

ORDER_PRODUCTS_2_TABLENAME = "order_products_2"
engine.execute(f"DROP TABLE IF EXISTS {ORDER_PRODUCTS_2_TABLENAME}")

df = pd.read_csv("order_products_wm_edit_df.csv").to_sql(
    name=ORDER_PRODUCTS_2_TABLENAME,
    con=engine,
    index=False,
    dtype={
        "number": sqlalchemy.types.Integer(),
        "order_id": sqlalchemy.types.Integer(),
        "product_id": sqlalchemy.types.Integer(),
        "quantity": sqlalchemy.types.Integer(),
        "q_left": sqlalchemy.types.Integer(),
        "trash": sqlalchemy.types.Integer(),
        "product_id.1": sqlalchemy.types.Integer(),
        "product_name": sqlalchemy.types.String(length=500),
        "asile_id" : sqlalchemy.types.Integer(),
        "department_id" : sqlalchemy.types.Integer(),
        "price": sqlalchemy.types.Integer(),},)
engine.execute(f"ALTER TABLE {ORDER_PRODUCTS_2_TABLENAME} ADD PRIMARY KEY (`number`)"
)