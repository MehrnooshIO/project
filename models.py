from operator import index
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey


db_Url="sqlite:///UserDB.db"
engine = create_engine(db_Url, connect_args={'check_same_thread': False})
Sesionlocal = sessionmaker(bind=engine)
Base=declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    password = Column(String(50))
    email = Column(String(50), unique=True)
    

Base.metadata.create_all(bind=engine)
