from ..app import app, db
from flask import render_template
from ..models.factbook import Country
from sqlalchemy import or_

@app.route("/pays")
def pays():
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

@app.route("/tous_pays")
def tous_pays():
    resultats = Country.query.all()
    return render_template("pages/generique.html", donnees=resultats)

@app.route("/le_premier_pays")
def le_premier_pays():
    resultats = list(Country.query.first())
    return render_template("pages/generique.html", donnees=resultats)

@app.route("/pays_differents_de_souverain")
def pays_differents_de_souverain():
    resultats = Country.query.filter(Country.type != 'sovereign').all()
    return render_template("pages/generique.html", donnees=resultats)

@app.route("/condition_or_autre_condition")
def condition_or_autre_condition():
    resultats = Country.query.filter(or_(Country.type == 'sovereign', Country.id == 'ay')).all()
    return render_template("pages/generique.html", donnees=resultats)

@app.route("/pays_souverains_ranges_ordre_decroissant")
def pays_souverains_ranges_ordre_decroissant():
    resultats = Country\
        .query.filter(
            or_(
                Country.type == 'sovereign', 
                Country.type == 'other')
            )\
        .order_by(Country.id.desc())\
        .all()
    return render_template("pages/generique.html", donnees=resultats)

@app.route("/ressources/<string:nom>")
def ressources(nom):
    ressources = []

    query =  Country.query
    ressources = query.filter(Country.name == nom).first()

    return render_template("pages/pays_ressources.html", pays=nom, ressources=ressources, sous_titre=nom)

@app.route("/ajout_pays/<string:id>/<string:name>/<string:type>/<string:rapide_description>")
def ajout_pays(name, id, type, rapide_description):
    nouveau_pays = Country(id=id , name=name , type=type, Introduction=rapide_description)
    db.session.add(nouveau_pays)
    db.session.commit()
    return "OK"

@app.route("/get_pays/<string:name>")
def get_pays(name):
    resultats = [Country.query.get(name)]
    return render_template("pages/generique.html", donnees=resultats)

@app.route("/suppression_pays/<string:id>")
def suppression_pays(id):

    pays = Country.query.get(id)

    db.session.delete(pays)
    db.session.commit()
    
    return "OK"

@app.route("/pays_pagination")
@app.route("/pays_pagination/<int:page>")
def pays_pagination(page=1):
    donnees = []
    query =  Country.query
    tous_resultats = query.paginate(page=page, per_page=app.config["PAYS_PER_PAGE"])
    return render_template("pages/pays_pagination.html", pagination=tous_resultats, sous_titre="Tous les pays")