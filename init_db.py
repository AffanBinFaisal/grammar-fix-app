import os
import sys

from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from dotenv import load_dotenv

# Add current directory to path so we can import app modules
sys.path.append(os.getcwd())

from app.database import Base, engine
from app.models import User  # Import models so they are registered with Base

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

def init():
    if not DATABASE_URL:
        print("DATABASE_URL not found in .env file")
        return

    print(f"Checking database connection to: {DATABASE_URL}")
    
    try:
        if not database_exists(engine.url):
            print(f"Database {engine.url.database} does not exist. Creating...")
            create_database(engine.url)
            print("Database created successfully.")
        else:
            print(f"Database {engine.url.database} already exists.")

        print("Creating tables...")
        Base.metadata.create_all(bind=engine)
        print("Tables created successfully.")
        
    except Exception as e:
        print(f"Error connecting to database: {e}")

if __name__ == "__main__":
    init()
