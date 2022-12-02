from ..app import app, db
from flask import render_template
from ..models.factbook import Country

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
    print(Country.__table__)
    return render_template("pages/tous_pays.html", donnees=donnees, sous_titre="Tous les pays")

@app.route("/pays/<string:nom>")
def pays_specifique(nom):
    grandes_villes = []
    if nom =='France':
        grandes_villes = ['Paris', 'Lyon', 'Marseille']
    return render_template("pages/pays.html", pays=nom, grandes_villes=grandes_villes, sous_titre=nom)