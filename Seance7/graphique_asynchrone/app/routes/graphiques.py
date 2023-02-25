from ..app import app, db
from flask import render_template, request, flash
from flask_login import login_required
from ..models.factbook import Country, country_resources
from sqlalchemy import func, text

@app.route("/graphiques/ressources_pays", methods=['GET', 'POST'])
def graphiques_ressources_pays():
    return render_template("pages/graphiques/ressources_pays.html")

@app.route("/graphiques/ressources_pays_donnees", methods=['GET', 'POST'])
def graphiques_ressources_pays_donnees():
    donnees_brutes = db.session.query(Country, func.count(country_resources.c.resource).label('total'))\
        .join(country_resources, )\
        .group_by(Country.id)\
        .order_by(text('total DESC'))\
        .limit(20)

    donnees = []

    for pays in donnees_brutes.all():
        donnees.append({
            "label": pays[0].name,
            "nombre": pays.total
        })

    return donnees