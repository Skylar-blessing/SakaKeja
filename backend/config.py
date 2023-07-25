from sqlalchemy import create_engine

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/saka-keja'
    SQLALCHEMY_TRACK_MODIFICATIONS = False