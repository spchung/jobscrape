from config import config
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = config.get('database','ecerything_jobscrapper')

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Base = declarative_base()

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = Session()