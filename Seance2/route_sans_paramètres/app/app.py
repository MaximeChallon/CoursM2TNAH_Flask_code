from flask import Flask
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/")
@app.route("/home")
def home():
    return "Hello world!"