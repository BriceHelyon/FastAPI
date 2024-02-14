from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Crée une instance du moteur SQLite
engine = create_engine("sqlite:///fastapidb.db")

# Crée une instance de DeclarativeMeta
Base = declarative_base()

# Crée la classe SessionLocal à partir de la factory sessionmaker
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)
