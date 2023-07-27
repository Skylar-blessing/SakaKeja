from urllib.parse import quote_plus

class Config:
    password = 'Skylar@001'
    encoded_password = quote_plus(password)
    SQLALCHEMY_DATABASE_URI = f'postgresql://skylar:{encoded_password}@localhost:5432/saka-keja'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
