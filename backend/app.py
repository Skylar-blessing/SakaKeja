from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config  # Import the Config class from config.py

# Initialize the Flask app and database
app = Flask(__name__)
app.config.from_object(Config)  # Load the configuration from the Config class
db = SQLAlchemy(app)

# Rest of your app configurations, routes, etc.

def create_app():
    return app
