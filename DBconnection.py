#Starter Inventory App
import numpy as np
import pandas as pd
import datetime as dt
# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.orm import Session 
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, func
from sqlalchemy import inspect, desc
from sqlalchemy import Column, Integer, String, BigInteger, VARCHAR, SmallInteger
from sqlalchemy.ext.declarative import declarative_base
import pymysql
import os
from pprint import pprint
db_user="root"
db_pass="wDyG5qeG?6G+])wX"
db_name="home_inventory_db"
# db_user = os.environ.get("DB_USER")
# db_pass = os.environ.get("DB_PASS")
# db_name = os.environ.get("DB_NAME")
#cloud_sql_connection_name = os.environ.get("CLOUD_SQL_CONNECTION_NAME")
db_instance="home-inventory-270423:us-central1:home-inventory-project"
# The SQLAlchemy engine will help manage interactions, including automatically
# managing a pool of connections to your database
db = sqlalchemy.create_engine(
    # Equivalent URL:
    # mysql+pymysql://root:wDyG5qeG?6G+])wX@/<db_name>?unix_socket=/cloudsql/<cloud_sql_instance_name>
    sqlalchemy.engine.url.URL(
        drivername="mysql+pymysql",
        username=db_user,
        password=db_pass,
        database=db_name,
        cloud_sql_connection_name=db_instance
        query={"unix_socket": "/cloudsql/{}".format(cloud_sql_connection_name)},
    ),
    # ... Specify additional properties here.
    # ...
)





  


Base = declarative_base()

class DictMixIn:
    def to_dict(self):
        return {
            column.name: getattr(self, column.name)
            if isinstance(getattr(self, column.name), datetime.datetime)
            else getattr(self, column.name).isoformat()
            for column in self.__table__.columns
        }

class Products(Base, DictMixIn):
    __tablename__ = "products"
    index = Column(BigInteger, primary_key=True)
    product_id = Column(BigInteger)
    product_name = Column(VARCHAR (120))
    aisle_id = Column(Integer)
    department_id = Column(Integer)


class Orders(Base, DictMixIn):
    __tablename__ = "orders"
    index= Column(Integer, primary_key=True)
    order_id = Column(BigInteger)
    user_id = Column(BigInteger)
    eval_set = Column(VARCHAR(10))
    order_number = Column(BigInteger)
    order_dow = Column(BigInteger)
    order_hour_of_day = Column(Integer)
    days_since_prior_order = Column(Integer)

class Order_products_prior(Base, DictMixIn):
    __tablename__ = "order_products_prior"
    index= Column(BigInteger, primary_key=True)
    order_id = Column(BigInteger)
    product_id = Column(BigInteger)
    add_to_cart_order = Column(Integer)
    reordered = Column(SmallInteger)

class Departments(Base, DictMixIn):
    __tablename__ = "departments"
    index = Column(BigInteger, primary_key=True)
    department_id = Column(BigInteger)
    department = Column(VARCHAR(30))


class Aisles(Base, DictMixIn):
    __tablename__ = "aisles"
    index = Column(BigInteger, primary_key=True)
    aisle_id = Column(BigInteger)
    aisle = Column(VARCHAR(30))


session=Session(engine)

user_data=session.query(aisles).all()
# user_data=session.query(Orders.order_id, Orders.order_number, Orders.order_hour_of_day, 
#                         Orders.days_since_prior_order, Products.product_id, 
#                         Products.product_name, Departments.department)\
#                             .filter(Orders.user_id==1)\
#                             .filter(Orders.order_id==Order_products_prior.order_id)\
#                             .filter(Order_products_prior.product_id==Products.product_id)\
#                             .filter(Products.department_id==Departments.department_id)

for row in user_data:
     print(row)


