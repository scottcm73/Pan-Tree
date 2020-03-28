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





engine = create_engine(f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}") 
Base = declarative_base()




class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True)
    email = Column(String(30), unique=True)
    passw = Column(String(80))

    

class Products(Base):
    __tablename__ = "products"
    product_id = Column(BigInteger, primary_key=True)
    product_name = Column(VARCHAR (120))
    aisle_id = Column(Integer)
    department_id = Column(Integer)
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
    
    order_id = Column(BigInteger)
    product_id = Column(BigInteger)
    num_of_product = Column(SmallInteger)
    opp_id = Column(BigInteger, primary_key=True)

class Departments(Base):
    __tablename__ = "departments"
    dept_index = Column(BigInteger, primary_key=True)
    department_id = Column(BigInteger)
    department = Column(VARCHAR(30))


class Aisles(Base):
    __tablename__ = "aisles"
    aisle_index = Column(BigInteger, primary_key=True)
    aisle_id = Column(BigInteger)
    aisle = Column(VARCHAR(30))

with engine.begin() as connection:
    session=Session(connection)


# Never got this query to work...
    user_data=session.query(Orders.order_id, 
                        Orders.days_since_prior_order, Orders.order_date, Products.product_id, Products.price,
                        Products.product_name, Departments.department)\
                            .filter(Orders.user_id==5)\
                            .filter(Orders.order_id==Order_products_prior.order_id)\
                            .filter(Order_products_prior.product_id==Products.product_id)\
                            .filter(Products.department_id==Departments.department_id).all()
 
   
    t=""
    for row in user_data:
        t=t+str(row._asdict())

    

pprint(t)
 
 


    



    