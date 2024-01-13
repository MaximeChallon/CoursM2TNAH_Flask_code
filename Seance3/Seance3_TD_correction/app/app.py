from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(
    __name__, 
    template_folder='templates',
    static_folder='statics')
app.config.from_object(Config)

db = SQLAlchemy(app)

from .routes import generales