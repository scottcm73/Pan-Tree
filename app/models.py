from sqlalchemy import Column, Integer, String, BigInteger, VARCHAR, SmallInteger
from sqlalchemy.types import Date
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_login import UserMixin
from config import Base, db
import datetime

class DictMixIn:
    def to_dict(self):
        return {
            column.name: getattr(self, column.name)
            if not isinstance(getattr(self, column.name), datetime.datetime)
            else getattr(self, column.name).isoformat()
            for column in self.__table__.columns
        }
class User(Base, UserMixin, DictMixIn, db.Model,):
    extend_existing=True
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
    order_date = Column(BigInteger)
    days_since_prior_order = Column(Integer)
    
class Order_products(Base, DictMixIn):
    __tablename__ = "order_products"
    order_id = Column(BigInteger, primary_key=True)
    product_id = Column(BigInteger)
    quantity = Column(Integer)
    q_left = Column(Integer)
    trash = Column(Integer)
    
class T_Orders(Base, DictMixIn):
    __tablename__ = "t_orders"
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


class LoginForm(FlaskForm):
    username = StringField(
        "username", validators=[InputRequired(), Length(min=4, max=15)]
    )
    password = PasswordField(
        "password", validators=[InputRequired(), Length(min=8, max=80)]
    )
    remember = BooleanField("remember me")


class RegisterForm(FlaskForm):
    email = StringField(
        "email", validators=[InputRequired(), Email(message="Invalid Email")]
    )
    username = StringField(
        "username", validators=[InputRequired(), Length(min=4, max=15)]
    )
    password = PasswordField(
        "password", validators=[InputRequired(), Length(min=8, max=80)]
    )
