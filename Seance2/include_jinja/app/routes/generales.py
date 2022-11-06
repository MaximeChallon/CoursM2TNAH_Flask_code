from ..app import app
from flask import render_template

@app.route("/pays")
def pays():
    donnees = [{
        "nom":"France",
        "capitale":"Paris",
        "continent":"Europe"
    },{
        "nom":"Etats-Unis",
        "capitale":"Washington",
        "continent":"Amérique"
    },{
        "nom":"Egypte",
        "capitale":"Le Caire",
        "continent":"Afrique"
    },{
        "nom":"Chine",
        "capitale":"Pékin",
        "continent":"Asie"
    }]
    return render_template("pages/pays.html", donnees=donnees, sous_titre="Tous les pays")