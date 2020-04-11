from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app_config import USER, PASSWORD,  HOST, PORT, DATABASE, DIALECT, DRIVER, secret
 


SQALCHEMY_DATABASE_URL = f"{DIALECT}+{DRIVER}://{USER}:{PASSWORD}@{HOST}/{DATABASE}"

engine = create_engine(
    SQALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()