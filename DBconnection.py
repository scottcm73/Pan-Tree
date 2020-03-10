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
      pool_size=5,
    # Temporarily exceeds the set pool_size if no connections are available.
    max_overflow=2,
    # The total number of concurrent connections for your application will be
    # a total of pool_size and max_overflow.
    # [END cloud_sql_mysql_sqlalchemy_limit]
    # [START cloud_sql_mysql_sqlalchemy_backoff]
    # SQLAlchemy automatically uses delays between failed connection attempts,
    # but provides no arguments for configuration.
    # [END cloud_sql_mysql_sqlalchemy_backoff]
    # [START cloud_sql_mysql_sqlalchemy_timeout]
    # 'pool_timeout' is the maximum number of seconds to wait when retrieving a
    # new connection from the pool. After the specified amount of time, an
    # exception will be thrown.
    pool_timeout=30,  # 30 seconds
    # [END cloud_sql_mysql_sqlalchemy_timeout]
    # [START cloud_sql_mysql_sqlalchemy_lifetime]
    # 'pool_recycle' is the maximum number of seconds a connection can persist.
    # Connections that live longer than the specified amount of time will be
    # reestablished
    pool_recycle=1800,  # 30 minutes
    # [END cloud_sql_mysql_sqlalchemy_lifetime]
    # [END_EXCLUDE]

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


# session=Session(engine)

# user_data=session.query(aisles).all()
# user_data=session.query(Orders.order_id, Orders.order_number, Orders.order_hour_of_day, 
#                         Orders.days_since_prior_order, Products.product_id, 
#                         Products.product_name, Departments.department)\
#                             .filter(Orders.user_id==1)\
#                             .filter(Orders.order_id==Order_products_prior.order_id)\
#                             .filter(Order_products_prior.product_id==Products.product_id)\
#                             .filter(Products.department_id==Departments.department_id)

# for row in user_data:
#      print(row)


@app.route("/", methods=["GET"])
def index():
    votes = []
    with db.connect() as conn:
        # Execute the query and fetch all results
        session=Session(conn)
        
        test_query=session.query(aisles).all()

    return render_template(
        "index.html", testquery=testquery
    )


# @app.route("/", methods=["POST"])
# # def save_vote():
# #     # Get the team and time the vote was cast.
# #     team = request.form["team"]
# #     time_cast = datetime.datetime.utcnow()
# #     # Verify that the team is one of the allowed options
# #     if team != "TABS" and team != "SPACES":
# #         logger.warning(team)
# #         return Response(response="Invalid team specified.", status=400)

# #     # [START cloud_sql_mysql_sqlalchemy_connection]
# #     # Preparing a statement before hand can help protect against injections.
# #     stmt = sqlalchemy.text(
# #         "INSERT INTO votes (time_cast, candidate)" " VALUES (:time_cast, :candidate)"
# #     )
# #     try:
# #         # Using a with statement ensures that the connection is always released
# #         # back into the pool at the end of statement (even if an error occurs)
# #         with db.connect() as conn:
# #             conn.execute(stmt, time_cast=time_cast, candidate=team)
# #     except Exception as e:
# #         # If something goes wrong, handle the error in this section. This might
# #         # involve retrying or adjusting parameters depending on the situation.
# #         # [START_EXCLUDE]
# #         logger.exception(e)
# #         return Response(
# #             status=500,
            
# #         )
# #         # [END_EXCLUDE]
# #     # [END cloud_sql_mysql_sqlalchemy_connection]

#     return Response(
#         status=200,
        
#     )


if __name__ == "__main__":
    app.run(host="35.224.15.57", port=8080, debug=True)