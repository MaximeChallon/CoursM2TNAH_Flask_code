from ..app import app, db
from flask import render_template
from sqlalchemy import text
from ..models.factbook import Country

@app.route("/pays")
def pays():
    '''donnees = [{
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
    '''
    resultats = db.session.execute(text("SELECT * FROM country LIMIT 10")).fetchall()
    #print(resultats)

    results = Country.query.all()
    #print(results)
    '''for r in results:
        print(r )
        print(type(r))
        print(r.id)
        print(r.name)
        print(type(r.name))'''
    
    donnees = []
    for country in Country.query.all():
        donnees.append({
            "nom": country.name,
            "capitale":"inconnu",
            "continent":"inconnu"
        })
    
    return render_template("pages/tous_pays.html", donnees=donnees, sous_titre="Tous les pays")

@app.route("/pays/<string:nom>")
def pays_specifique(nom):
    grandes_villes = []
    if nom =='France':
        grandes_villes = ['Paris', 'Lyon', 'Marseille']
    return render_template("pages/pays.html", pays=nom, grandes_villes=grandes_villes, sous_titre=nom)