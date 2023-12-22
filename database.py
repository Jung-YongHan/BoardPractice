from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

username = "postgres"
password = "1234"
host = "localhost"
port = "5432"
db_name = "qrade"

SQLALCHEMY_DATABASE_URL = f"postgresql://{username}:{password}@{host}:{port}/{db_name}"

# postgreSQL 연결
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()