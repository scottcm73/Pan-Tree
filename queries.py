from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, BigInteger, VARCHAR, SmallInteger
import datetime
from database import SessionLocal, engine, Base

from models import (
    Products,
    Departments,
    Aisles,
    T_Orders,
    T_Order_products,
    Product_nutrients
)

session = SessionLocal()

department_query = session.query(Departments).all()

nutrient_query = session.query(
    T_Orders.order_date,
    T_Order_products.order_id,
    Product_nutrients.product_name, 
    Product_nutrients.ENERC_KCAL,
    Product_nutrients.FAT,
    Product_nutrients.CHOCDF,
    Product_nutrients.FIBTG,
    Product_nutrients.PROCNT,    
    ).join(
        Product_nutrients, T_Order_products.product_id == Product_nutrients.product_id
    ).join(
        T_Orders, T_Order_products.order_id == T_Orders.order_id
    ).limit(100).all()