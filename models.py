from sqlalchemy import Column, Integer, String, BigInteger, VARCHAR, SmallInteger
from sqlalchemy.types import Date
from database import Base
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_login import UserMixin
import datetime


class DictMixIn:
    def to_dict(self):
        return {
            column.name: getattr(self, column.name)
            if not isinstance(getattr(self, column.name), datetime.datetime)
            else getattr(self, column.name).isoformat()
            for column in self.__table__.columns
        }



class Products(Base, DictMixIn):
    __tablename__ = "products"
    #index = Column(BigInteger, primary_key=True)
    product_id = Column(BigInteger, primary_key=True)
    product_name = Column(VARCHAR (120))
    aisle_id = Column(Integer)
    department_id = Column(Integer)
    price = Column(Integer)


class Orders(Base, DictMixIn):
    __tablename__ = "orders"
    #index = Column(Integer)
    order_id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger)
    #eval_set = Column(VARCHAR(10))
    #order_number = Column(BigInteger)
    order_dow = Column(BigInteger)
    #order_hour_of_day = Column(Integer)
    days_since_prior_order = Column(Integer)

class Order_products_prior(Base, DictMixIn):
    __tablename__ = "order_products_prior"
    #index= Column(BigInteger)
    opp_id = Column(BigInteger, primary_key=True )
    order_id = Column(BigInteger)
    product_id = Column(BigInteger)
    num_of_product = Column(Integer)
    # add_to_cart_order = Column(Integer)
    # reordered = Column(SmallInteger)

class Departments(Base, DictMixIn):
    __tablename__ = "departments"
    department_id = Column(BigInteger, primary_key=True)
    department = Column(VARCHAR(30))


class Aisles(Base, DictMixIn):
    __tablename__ = "aisles"
    aisle_id = Column(BigInteger, primary_key=True)
    aisle = Column(VARCHAR(30))



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
