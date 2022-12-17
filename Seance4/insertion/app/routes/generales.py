from ..app import app, db
from flask import render_template
from ..models.factbook import Country, country_resources, Resources

@app.route("/add_country/<string:pays>/<string:id>/<string:type>")
def add_country(pays, id, type):
    nouveau_pays = Country(id=id , name=pays , type=type)
    db.session.add(nouveau_pays)
    db.session.commit()

    return "Succeded"

@app.route("/add_ressource/<string:pays>/<string:ressource>")
def add_ressource(pays, ressource):
    
    pays = Country.\
        query.\
        filter(Country.name == pays).\
        first()
    ressource = Resources.\
        query.\
        filter(Resources.name == ressource).\
        first()

    pays.resources.append(ressource)
    db.session.add(pays)
    db.session.commit()
    
    return "Succeded"
