from ..app import app, db
from flask import render_template
from ..models.factbook import Country
from sqlalchemy import and_, or_, distinct

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

@app.route("/first")
def first():
    donnees = []

    query =  Country.query
    resultat = query.first()

    donnees.append({
            "nom": resultat.name,
            "description": resultat.Introduction,
            "type": resultat.type
        })
    
    return render_template("pages/all.html", donnees=donnees, sous_titre="First")

@app.route("/get")
def get():
    donnees = []

    query =  Country.query
    resultat = query.get('fr')

    donnees.append({
            "nom": resultat.name,
            "description": resultat.Introduction,
            "type": resultat.type
        })
    
    return render_template("pages/all.html", donnees=donnees, sous_titre="Get")

@app.route("/filter")
def filter():
    donnees = []

    query =  Country.query
    resultats = query.filter(Country.type == 'sovereign').all()

    for resultat in resultats:
        donnees.append({
            "nom": resultat.name,
            "description": resultat.Introduction,
            "type": resultat.type
        })
    
    return render_template("pages/all.html", donnees=donnees, sous_titre="Filter")

@app.route("/filter_and_implicite")
def filter_and_implicite():
    donnees = []

    query =  Country.query
    resultats = query.filter(Country.type == 'sovereign', Country.id == 'fr' ).all()

    for resultat in resultats:
        donnees.append({
            "nom": resultat.name,
            "description": resultat.Introduction,
            "type": resultat.type
        })
    
    return render_template("pages/all.html", donnees=donnees, sous_titre="And implicite")

@app.route("/filter_and_explicite")
def filter_and_explicite():
    donnees = []

    query =  Country.query
    resultats = query.filter(and_(Country.type == 'sovereign', Country.id == 'fr' )).all()

    for resultat in resultats:
        donnees.append({
            "nom": resultat.name,
            "description": resultat.Introduction,
            "type": resultat.type
        })
    
    return render_template("pages/all.html", donnees=donnees, sous_titre="And explicite")

@app.route("/filter_or_implicite")
def filter_or_implicite():
    donnees = []

    query =  Country.query
    resultats = query.filter((Country.type == 'dependency')|(Country.id == 'fr')).all()

    for resultat in resultats:
        donnees.append({
            "nom": resultat.name,
            "description": resultat.Introduction,
            "type": resultat.type
        })
    
    return render_template("pages/all.html", donnees=donnees, sous_titre="Or implicite")

@app.route("/filter_or_explicite")
def filter_or_explicite():
    donnees = []

    query =  Country.query
    resultats = query.filter(or_(Country.type == 'dependency', Country.id == 'fr' )).all()

    for resultat in resultats:
        donnees.append({
            "nom": resultat.name,
            "description": resultat.Introduction,
            "type": resultat.type
        })
    
    return render_template("pages/all.html", donnees=donnees, sous_titre="Or explicite")

@app.route("/count")
def count():
    donnees = []

    query =  Country.query
    resultat = query.filter(Country.type == 'sovereign').count()
    
    return render_template("pages/count.html", count=str(resultat), type="souverains", sous_titre="Count")

@app.route("/order_by")
def order_by():
    donnees = []

    query =  Country.query
    resultats = query.order_by(Country.name).all()

    for resultat in resultats:
        donnees.append({
            "nom": resultat.name,
            "description": resultat.Introduction,
            "type": resultat.type
        })
    
    return render_template("pages/all.html", donnees=donnees, sous_titre="Order by")


@app.route("/order_by_desc")
def order_by_desc():
    donnees = []

    query =  Country.query
    resultats = query.order_by(Country.name.desc()).all()

    for resultat in resultats:
        donnees.append({
            "nom": resultat.name,
            "description": resultat.Introduction,
            "type": resultat.type
        })
    
    return render_template("pages/all.html", donnees=donnees, sous_titre="Order by DESC")

@app.route("/group_by")
def group_by():
    donnees = []

    query =  Country.query
    resultats = query.group_by(Country.type).all()

    for resultat in resultats:
        donnees.append({
            "nom": "",
            "description": "",
            "type": resultat.type
        })
    
    return render_template("pages/all.html", donnees=donnees, sous_titre="Group by")

@app.route("/distinct")
def distinct():
    donnees = []

    query =  Country.query
    resultats = query.with_entities(Country.type).distinct()

    for resultat in resultats:
        donnees.append({
            "nom": "",
            "description": "",
            "type": resultat.type
        })
    
    return render_template("pages/all.html", donnees=donnees, sous_titre="Distinct")
