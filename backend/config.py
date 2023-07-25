from sqlalchemy import create_engine

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://Postgres:postgres@localhost:5432/saka-keja'
    # Disable SQLAlchemy's modification tracking system for better performance.
    SQLALCHEMY_TRACK_MODIFICATIONS = False