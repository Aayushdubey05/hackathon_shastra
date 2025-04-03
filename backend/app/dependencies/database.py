from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URI = "mysql+pymysql://root:----@localhost:3306/fastApi"
engine =  create_engine(DATABASE_URI)

SessionLocal = sessionmaker(bind = engine, autocommit = False, autoflush = False)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()
   