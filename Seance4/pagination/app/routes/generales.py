from ..app import app, db
from flask import render_template
from ..models.factbook import Country, Elevation
from sqlalchemy import and_, or_, distinct, func

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


@app.route("/pagination_sql/<int:numero_page>/<int:nb_resultats>")
def pagination_sql(numero_page, nb_resultats):
    donnees = []

    query =  Country.query
    tous_resultats = query.limit(nb_resultats * numero_page).offset(numero_page).all()

    for resultat in tous_resultats:
        donnees.append({
            "nom": resultat.name,
            "description": resultat.Introduction,
            "type": resultat.type
        })
    
    return render_template("pages/all.html", donnees=donnees, sous_titre="Pagination SQL")

@app.route("/pays/<int:page>")
def pays(page):
    donnees = []

    query =  Country.query
    tous_resultats = query.paginate(page=page, per_page=app.config["PAYS_PER_PAGE"])
    
    return render_template("pages/pays.html", pagination=tous_resultats, sous_titre="Pagination")