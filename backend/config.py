class Config:
    username = 'user_1'
    password = '27@5638Hg'
    host = 'localhost'
    database_name = 'saka-keja'
    SQLALCHEMY_DATABASE_URI = f'postgresql://{username}:{password}@{host}:5432/{database_name}'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
