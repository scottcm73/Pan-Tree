from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, BigInteger, VARCHAR, SmallInteger
import datetime
from config import SessionLocal, engine, Base

from models import (
    Products,
    Departments,
    Aisles,
    T_Orders,
    T_Order_products,
    Product_nutrients
)

session = SessionLocal()


#department and aisles
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


def count_nutrients(query_dicts):

    unique_dates = []
    for i in query_dicts:
        if i['order_date'] not in unique_dates:
            unique_dates.append(i['order_date'])

    sort_dates = sorted(unique_dates)
    data=[]

    for date in sort_dates:
        
        data_dict = {}
        enerc_count = 0
        fat_count = 0
        carb_count = 0
        fib_count = 0
        pro_count = 0
        for point in query_dicts:        
            if point['order_date'] == date:
                enerc_count += point['ENERC_KCAL']
                fat_count += point['FAT']
                carb_count += point['CHOCDF']
                fib_count += point['FIBTG']
                pro_count += point['PROCNT']
        data_dict = {'date' : date,
                'total_calories' : enerc_count,
                'total_fat' : fat_count,
                'total_carbs' : carb_count,
                'total_fiber' : fib_count,
                'total_protein' : pro_count
            }
        data.append(data_dict)
    return data
