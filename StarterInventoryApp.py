#Starter Inventory App
# Save as Starter_inventory_yourname.ipynb
import numpy as np
import pandas as pd
import datetime as dt
# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.orm import Session 
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, func
from sqlalchemy import inspect, desc
from sqlalchemy import Column, Integer, String, BigInteger, VARCHAR, SmallInteger, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy
import pymysql
import os
from pprint import pprint
from app_config import USER, PASSWORD, HOST, PORT, DATABASE
#I will send a username and password for each of you.
from sqlalchemy.ext.declarative import as_declarative
from collections import defaultdict
import json




engine = create_engine(f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}") 
Base = declarative_base()




class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True)
    email = Column(String(30), unique=True)
    passw = Column(String(80))

class Departments(Base):
    __tablename__ = "departments"
    department_id = Column(BigInteger, primary_key=True)
    department = Column(VARCHAR(30))


class Aisles(Base):
    __tablename__ = "aisles"
    aisle_index = Column(BigInteger, primary_key=True)
    aisle_id = Column(BigInteger)
    aisle = Column(VARCHAR(30))   

class Products(Base):
    __tablename__ = "products"
    product_id = Column(BigInteger, primary_key=True)
    product_name = Column(VARCHAR (120))
    aisle_id = Column(Integer)
    department_id = Column(Integer, ForeignKey('departments.department_id'))

    price = Column(Float)


class Orders(Base):
    __tablename__ = "orders"
    order_id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger)
    order_dow = Column(BigInteger)
    days_since_prior_order = Column(Integer)
    order_date = Column(VARCHAR(12))

class Order_products_prior(Base):
    __tablename__ = "order_products_prior"
    
    order_id = Column(BigInteger, ForeignKey('orders.order_id'))
    product_id = Column(BigInteger, ForeignKey('products.product_id'))
    num_of_product = Column(SmallInteger)
    opp_id = Column(BigInteger, primary_key=True)
    



with engine.begin() as connection:
    session=Session(connection)


# Never got this query to work...
    user_data=session.query(Orders, Order_products_prior, Products, Departments)\
        .filter(Orders.order_id==Order_products_prior.order_id)\
        .filter(Order_products_prior.product_id==Products.product_id)\
        .filter(Products.department_id==Departments.department_id)\
        .filter(Orders.user_id==5)
    
    print(user_data)


 
    x=0
    data="{\"product_order\":["
    for row in user_data:
        data=data+str(row._asdict())+","
        x=x+1
    data=data.replace("'", "\"")
    data = data[:-1] # Erases final comma
    data = data + "]}"
    print(x)
    print(data)
connection.close()


with open('data.txt', 'w+') as file:
    file.write(data)
   


 
 


    



    