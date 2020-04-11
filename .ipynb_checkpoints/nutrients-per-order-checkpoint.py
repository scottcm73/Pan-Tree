from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, BigInteger, VARCHAR, SmallInteger
from sqlalchemy import *
import datetime

####-----------------------
#### make sure USER and PASSWORD agree with
#### with your machines local host
####-----------------------
DIALECT = 'mysql'
DRIVER = 'pymysql'
PORT = '3306'
HOST = '162.241.193.35'
USER = 'datascm2_cesar'
PASSWORD = '3b^WP+WbYP2J8pQPvSJbWWsXr7v2F2jDTq^+2KqF&S&uR*f?JUCaJ*5+NmWbKrJu'
DATABASE = 'datascm2_home_inventory_db'

SQALCHEMY_DATABASE_URL = f"{DIALECT}+{DRIVER}://{USER}:{PASSWORD}@{HOST}/{DATABASE}"

engine = create_engine(
    SQALCHEMY_DATABASE_URL, 
    pool_recycle=3600,
    pool_pre_ping=True
)


Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base()
class DictMixIn:
    def to_dict(self):
        return {
            column.name: getattr(self, column.name)
            if not isinstance(getattr(self, column.name), datetime.datetime)
            else getattr(self, column.name).isoformat()
            for column in self.__table__.columns
        }

class Product_nutrients(Base, DictMixIn):
    __tablename__ = "product_nutrients"
    product_id = Column(BigInteger, primary_key=True)
    product_name = Column(VARCHAR (120))
    price = Column(Integer)
    aisle_id = Column(Integer)
    department_id = Column(Integer)
    text_API = Column(Integer)
    ENERC_KCAL = Column(Integer)
    FAT = Column(Integer)
    CHOCDF = Column(Integer)
    FIBTG = Column(Integer)
    PROCNT = Column(Integer)
    
class Orders(Base, DictMixIn):
    __tablename__ = "orders"
    order_id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger)
    order_date = Column(BigInteger)
    days_since_prior_order = Column(Integer)
    
class T_Order_products(Base, DictMixIn):
    __tablename__ = "t_order_products"
    order_id = Column(BigInteger, primary_key=True)
    product_id = Column(BigInteger)
    quantity = Column(Integer)
    q_left = Column(Integer)
    trash = Column(Integer)

query = session.query(
    Orders.order_date,
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
    Orders, T_Order_products.order_id == Orders.order_id
).limit(1000).all()

query_dicts = [q._asdict() for q in query]

dates_list = [p['order_date'] for p in query_dicts]

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
    choc_count = 0
    fib_count = 0
    pro_count = 0
    for point in query_dicts:        
        if point['order_date'] == date:
            ##ENEC
            enerc_count += point['ENERC_KCAL']
            ##FAT
            fat_count += point['FAT']
            ##CHOC
            choc_count += point['CHOCDF']
            ##FIB
            fib_count += point['FIBTG']
            #PRO
            pro_count += point['PROCNT']
        data_dict[date] = {
                'total_calories' : enerc_count,
                'total_fat' : fat_count,
                'total_carbs' : choc_count,
                'total_fiber' : fib_count,
                'total_protein' : pro_count
            }
    data.append(data_dict)
