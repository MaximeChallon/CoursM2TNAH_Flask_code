from ..app import app, db
from flask import render_template, request, flash
from ..models.factbook import Country, Resources, Map
from ..models.formulaires import InsertionPays, InsertionRessource
from ..utils.transformations import  clean_arg

@app.route("/insertions/pays", methods=['GET', 'POST'])
def insertion_pays():
    form = InsertionPays() 

    try:
        if form.validate_on_submit():
            nom_pays =  clean_arg(request.form.get("nom_pays", None))
            code_pays =  clean_arg(request.form.get("code_pays", None))
            type =  clean_arg(request.form.get("type", None))
            introduction =  clean_arg(request.form.get("introduction", None))
            ressources =  clean_arg(request.form.getlist("ressources", None))
            continent =  clean_arg(request.form.get("continent", None))

            nouveau_pays = Country(id=code_pays, 
                Introduction=introduction,
                name=nom_pays,
                type = type)

            for ressource in ressources:
                ressource = Resources.\
                    query.\
                    filter(Resources.id == ressource).\
                    first()
                nouveau_pays.resources.append(ressource)
            
            nouveau_pays.maps.append(Map.query.filter(Map.name==continent).first())

            db.session.add(nouveau_pays)
            db.session.commit()

            flash("L'insertion du pays "+ nom_pays + " s'est correctement déroulée", 'info')
    
    except Exception as e :
        flash("Une erreur s'est produite lors de l'insertion de " + nom_pays + " : " + str(e), "error")

        db.session.rollback()
    
    return render_template("pages/insertion_pays.html", 
            sous_titre= "Insertion pays" , 
            form=form)

@app.route("/insertions/ressource", methods=['GET', 'POST'])
def insertion_ressource():
    form = InsertionRessource() 

    try:
        if form.validate_on_submit():
            nom_res =  clean_arg(request.form.get("nom_res", None))
            id_res =  clean_arg(request.form.get("code_res", None))

            nouvelle_ressource = Resources(id=id_res, 
                name=nom_res)

            db.session.add(nouvelle_ressource)
            db.session.commit()

            flash("L'insertion de la ressource "+ nom_res + " s'est correctement déroulée", 'info')
    
    except Exception as e :
        flash("Une erreur s'est produite lors de l'insertion de " + nom_res + " : " + str(e), "error")

        db.session.rollback()
    
    return render_template("pages/insertion_ressource.html", 
            sous_titre= "Insertion ressource" , 
            form=form)