from flask import Flask
from backend.config import Config
app = Flask(__name__)

app.config.from_object(Config)