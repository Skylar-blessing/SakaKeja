from urllib.parse import quote_plus

class Config:
    password = '27@5638Hg'
    encoded_password = quote_plus(password)
    SQLALCHEMY_DATABASE_URI = f'postgresql://user_1:{encoded_password}@localhost:5432/saka-keja'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
