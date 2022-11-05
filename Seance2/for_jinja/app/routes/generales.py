from ..app import app
from flask import render_template

@app.route("/pays/<string:nom>")
def pays(nom):
    grandes_villes = []
    if nom =='France':
        grandes_villes = ['Paris', 'Lyon', 'Marseille']
    return render_template("pages/pays.html", pays=nom, grandes_villes=grandes_villes)