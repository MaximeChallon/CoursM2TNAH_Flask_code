from ..app import app, db
from flask import render_template, request, flash
from ..models.factbook import Country, Resources, Map
from ..models.formulaires import  SuppressionPays, SuppressionRessource
from ..utils.transformations import  clean_arg

@app.route("/suppressions/pays", methods=['GET', 'POST'])
def suppression_pays():
    form = SuppressionPays()
    form.nom_pays.choices = [('','')] + [(pays.id, pays.name) for pays in Country.query.all()]

    def delete_pays(pays):
        # vérifier que le code existe bien en base
        pays = Country.query.get(code_pays)
        if pays:
            db.session.delete(pays)
            db.session.commit()

    try:
        if form.validate_on_submit():
            nom_pays =  clean_arg(request.form.get("nom_pays", None))
            code_pays =  clean_arg(request.form.get("code_pays", None))

            if code_pays:
                delete_pays(code_pays)
                flash("La suppression du pays s'est correctement déroulée", 'info')
            
            elif nom_pays:
                delete_pays(nom_pays)
                flash("La suppression du pays s'est correctement déroulée", 'info')

            else:
                flash("Il n'y a aucun pays spécifié", "error")
    
    except Exception as e :
        flash("Une erreur s'est produite lors de la suppression : " + str(e), "error")
    
    return render_template("pages/suppression_pays.html", 
            sous_titre= "Suppression pays" , 
            form=form)

@app.route("/suppressions/ressource", methods=['GET', 'POST'])
def suppression_ressource():
    form = SuppressionRessource()
    form.nom_res.choices = [('','')] + [(res.id, res.name) for res in Resources.query.all()]

    def delete_ressource(ressource):
        # vérifier que le code existe bien en base
        ressource = Resources.query.get(ressource)
        if ressource:
            db.session.delete(ressource)
            db.session.commit()

    try:
        if form.validate_on_submit():
            nom_res =  clean_arg(request.form.get("nom_res", None))
            code_res =  clean_arg(request.form.get("code_res", None))

            if code_res:
                delete_ressource(code_res)
                flash("La suppression de la ressource s'est correctement déroulée", 'info')
            
            elif nom_res:
                delete_ressource(nom_res)
                flash("La suppression de la ressource s'est correctement déroulée", 'info')

            else:
                flash("Il n'y a aucune ressource spécifiée", "error")
    
    except Exception as e :
        flash("Une erreur s'est produite lors de la suppression : " + str(e), "error")
    
    return render_template("pages/suppression_ressource.html", 
            sous_titre= "Suppression ressource" , 
            form=form)
