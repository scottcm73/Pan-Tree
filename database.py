from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from boto.s3.connection import S3Connection
s3 = S3Connection(os.environ['USER'], 
                    os.environ['PASSWORD'], 
                    os.environ['HOST'], 
                    os.environ['PORT'], 
                    os.environ['DATABASE'],
                    os.environ['DIALECT'],
                    os.environ['DRIVER'],
                    os.environ['secret']
                    )

USER=s3.USER
PASSWORD = s3.PASSWORD
HOST = s3.HOST
PORT = s3.PORT
DATABASE = s3.DATABASE
DIALECT = s3.DIALECT
DRIVER = s3.DRIVER
secret = s3.secret


 
SQALCHEMY_DATABASE_URL = f"{DIALECT}+{DRIVER}://{USER}:{PASSWORD}@{HOST}/{DATABASE}"

engine = create_engine(
    SQALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
