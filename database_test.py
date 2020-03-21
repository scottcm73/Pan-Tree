from app_config import DIALECT, DRIVER, username, password, host, database
#from testconfig import DIALECT, DRIVER, USERNAME, PASSWORD, DATABASE, HOSTNAME, PORT
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, Column, String, Integer

Base = automap_base()
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True)
    email = Column(String(30), unique=True)
    password = Column(String(80))


connection_string = (
    f"{DIALECT}+{DRIVER}://{username}:{password}@{host}/{database}"
)

engine = create_engine(connection_string)
# reflect the tables


Base.prepare(engine, reflect=True)
conn = engine.connect()
Base.metadata.create_all(engine)
session = Session(bind=engine)




user = input('pleaser enter usrname:  ')
email = input('pleaser enter email:  ')
password = input('pleaser enter password:  ')

# new_user = User(username=user, email=email, password=password)
# db.session.add(new_user)
# db.session.commit()

