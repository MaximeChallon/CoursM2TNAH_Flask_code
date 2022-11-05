from ..app import app
from flask import render_template

@app.route("/")
def accueil():
    return render_template("pages/accueil.html")