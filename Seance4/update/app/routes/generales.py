from ..app import app, db
from flask import render_template
from ..models.factbook import  Resources

@app.route("/update_ressource/<string:current_name>/<string:new_name>")
def add_ressource(current_name, new_name):
    
    Resources.query.filter(Resources.name == current_name).update({"name": new_name})
    db.session.commit()
    
    return "Succeded"
