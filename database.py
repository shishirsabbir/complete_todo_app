# importing packages
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base

# database url
SQLALCHEMY_DATABASE_URL = 'sqlite:///todosapp.db'

# creating database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# creating a session instance
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# creating a base for the database
Base = declarative_base()

# creating models for the database
class Todos(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)
