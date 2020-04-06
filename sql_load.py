import pandas as pd
import os

prior_path = os.path.join('Resources', 'order_products__prior.csv')
train_path = os.path.join('Resources', 'order_products__train.csv')
order_path = os.path.join('Resources', 'orders2.csv')
department_path = os.path.join('Resources', 'departments.csv')
aisles_path = os.path.join('Resources', 'aisles.csv')
products_path = os.path.join('Resources', 'products_price.csv')

prior_df = pd.read_csv(prior_path)
train_df = pd.read_csv(train_path)
order_df = pd.read_csv(order_path) 
department_df = pd.read_csv(department_path)
aisles_df = pd.read_csv(aisles_path)
products_df = pd.read_csv(products_path) 

order_products_df = pd.concat([prior_df, train_df])

from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, BigInteger, VARCHAR, SmallInteger
from sqlalchemy import *


####-----------------------
#### make sure USER and PASSWORD agree with
#### with your machines local host
####-----------------------
DIALECT = 'mysql'
DRIVER = 'pymysql'
PORT = '3306'
USER = 'root'
PASSWORD = 'a1b2c3d4e5f6'
HOST = '127.0.0.1'

SQALCHEMY_DATABASE_URL = f"{DIALECT}+{DRIVER}://{USER}:{PASSWORD}@{HOST}/local_inventory"

engine = create_engine(
    SQALCHEMY_DATABASE_URL, 
    pool_recycle=3600,
    pool_pre_ping=True
)

Base = declarative_base()

class DictMixIn:
    def to_dict(self):
        return {
            column.name: getattr(self, column.name)
            if not isinstance(getattr(self, column.name), datetime.datetime)
            else getattr(self, column.name).isoformat()
            for column in self.__table__.columns
        }
class User(Base):
    __tablename__ = "users" 
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(15), unique=True)
    email = Column(String(50), unique=True)
    passw = Column(String(80))

class Departments(Base, DictMixIn):
    __tablename__ = "departments"
    department_id = Column(BigInteger, primary_key=True)
    department = Column(VARCHAR(30))

class Aisles(Base, DictMixIn):
    __tablename__ = "aisles"
    aisle_id = Column(BigInteger, primary_key=True)
    aisle = Column(VARCHAR(30))

class Products(Base, DictMixIn):
    __tablename__ = "products"
    product_id = Column(BigInteger, primary_key=True)
    product_name = Column(VARCHAR (120))
    price = Column(Integer)
    aisle_id = Column(Integer)
    department_id = Column(Integer)

class Orders(Base, DictMixIn):
    __tablename__ = "orders"
    order_id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger)
    order_dow = Column(BigInteger)
    days_since_prior_order = Column(Integer)

class Order_products(Base, DictMixIn):
    __tablename__ = "order_products"
    order_id = Column(BigInteger, primary_key=True )
    product_id = Column(BigInteger, ForeignKey('products.product_id'))
    num_of_product = Column(Integer)
    add_to_cart_order = Column(Integer)
    reordered = Column(SmallInteger)

Base.metadata.create_all(engine)

order_products_df.to_sql(name='order_products',
                         con=engine,
                         if_exists='replace', 
                         index=False,
                         chunksize=200
                        )
order_df.to_sql(name='orders',
                con=engine,
                if_exists='replace',
                index=False,
                chunksize=200)
department_df.to_sql(name='departments',
                con=engine,
                if_exists='replace',
                index=False,
                chunksize=200)
aisles_df.to_sql(name='aisles',
                con=engine,
                if_exists='replace',
                index=False,
                chunksize=200)
products_df.to_sql(name='products',
                con=engine,
                if_exists='replace',
                index=False,
                chunksize=200)
