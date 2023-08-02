from urllib.parse import quote_plus

class Config:
    password = '1Godwin2wonderful'
    encoded_password = quote_plus(password)
    SQLALCHEMY_DATABASE_URI = f'postgresql://stevenmolvin@gmail.com:{encoded_password}@localhost:5432/saka-keja'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
