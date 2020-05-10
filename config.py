from flask_bootstrap import Bootstrap
from flask import (
    Flask,
    _app_ctx_stack,
)
from flask_cors import CORS
from flask_login import LoginManager
from sqlalchemy.orm import scoped_session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy


DIALECT = "mysql"
DRIVER = "pymysql"
USER = "datascm2_web"

HOST = "35.232.35.9"
PORT = "3306"
DATABASE = "datascm2_home_inventory_db"

SQALCHEMY_DATABASE_URL = (f"{DIALECT}+{DRIVER}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")


##database configuration
engine = create_engine(SQALCHEMY_DATABASE_URL, pool_recycle=3600, pool_pre_ping=True)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
## needed for User methods with flask_login
db = SQLAlchemy()


##app configuration
app = Flask(__name__, static_url_path="/static")

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = SQALCHEMY_DATABASE_URL
app.config["JSON_SORT_KEYS"] = False
app.secret_key = KEY
db.init_app(app)
Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
##addtitions to use simple SQLAlchemy
CORS(app)

app.session = scoped_session(SessionLocal, scopefunc=_app_ctx_stack.__ident_func__)

