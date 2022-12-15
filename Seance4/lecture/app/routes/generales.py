from ..app import app, db
from flask import render_template
from ..models.factbook import Country

@app.route("/all")
def all():
    donnees = []

    query =  Country.query
    tous_resultats = query.all()

    for resultat in tous_resultats:
        donnees.append({
            "nom": resultat.name,
            "description": resultat.Introduction,
            "type": resultat.type
        })
    
    return render_template("pages/all.html", donnees=donnees, sous_titre="All")