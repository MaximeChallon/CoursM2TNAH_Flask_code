from ..app import app, db
from flask import render_template
from ..models.factbook import  Resources

@app.route("/delete_ressource_by_query/<string:name>")
def delete_ressource_by_query(name):
    
    Resources.query.filter(Resources.name == name).delete()
    db.session.commit()
    
    return "Succeded"

@app.route("/delete_ressource/<string:name>")
def delete_ressource(name):

    ressource = Resources.\
        query.\
        filter(Resources.name == name).\
        first()

    db.session.delete(ressource)
    db.session.commit()
    
    return "Succeded"