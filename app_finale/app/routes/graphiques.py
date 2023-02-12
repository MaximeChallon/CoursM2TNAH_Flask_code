from ..app import app, db
from flask import render_template, request, flash
from flask_login import login_required
from ..models.factbook import Country, country_resources
from sqlalchemy import func, text

@app.route("/graphiques/ressources_pays", methods=['GET', 'POST'])
@login_required
def graphiques_ressources_pays():
    donnees_brutes = db.session.query(Country, func.count(country_resources.c.resource).label('total'))\
        .join(country_resources, )\
        .group_by(Country.id)\
        .order_by(text('total DESC'))\
        .limit(20)

    # formattage des données pour les envoyer au graphique: il faut deux listes:
    # une pour les labels
    # une pour les nombres de chaque pays, rangée dans l'ordre de celle des labels

    labels = []
    nombres=[]

    for pays in donnees_brutes.all():
        labels.append(pays[0].name)
        nombres.append(pays.total)

    return render_template("pages/graphiques/ressources_pays.html", labels=labels, nombres=nombres)