from urllib.parse import quote_plus
import os

class Config:
    password = 'Skylar@001'
    encoded_password = quote_plus(password)
    SQLALCHEMY_DATABASE_URI = f'postgresql://skylar:{encoded_password}@localhost:5432/saka-keja'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CLOUDINARY_CLOUD_NAME = os.environ.get('CLOUDINARY_CLOUD_NAME')
    CLOUDINARY_API_KEY = os.environ.get('CLOUDINARY_API_KEY')
    CLOUDINARY_API_SECRET = os.environ.get('CLOUDINARY_API_SECRET')