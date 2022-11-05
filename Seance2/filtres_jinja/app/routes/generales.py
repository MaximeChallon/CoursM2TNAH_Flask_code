from ..app import app
from flask import render_template

@app.route("/pays/<string:nom>")
def pays(nom):
    return render_template("pages/pays.html", pays=nom)