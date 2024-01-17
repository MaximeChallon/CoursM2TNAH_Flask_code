from ..app import app, db
from flask import render_template, request
from sqlalchemy import or_, text
from ..models.factbook import Country, Resources, Map, Area, Boundaries
from ..models.formulaires import Recherche
from ..utils.transformations import clean_arg

@app.route("/")
@app.route("/pays")
@app.route("/pays/<int:page>")
def pays(page=1):
    return render_template("pages/pays.html", 
        sous_titre="Pays", 
        donnees= Country.query.order_by(Country.name).paginate(page=page, per_page=app.config["PAYS_PER_PAGE"]))

@app.route("/pays/<string:nom_pays>")
def un_pays(nom_pays):
    return render_template("pages/un_pays.html", 
        sous_titre=nom_pays, 
        donnees= Country.query.filter(Country.name == nom_pays).first())

@app.route("/continents")
@app.route("/continents/<int:page>")
def continents(page=1):
    # on va créer un dictionnaire (JSON) avec en clé les continents et en valeur une liste de pays
    # il faut initialiser ce dictionnaire au début 
    pays_par_continent = {}

    for pays in Country.query.all():
        for continent in pays.maps:
            # si la clé (continent) existe déjà dans le dictionnaire, alors il est simplement nécessaire 
            # d'ajouter le pays s'il n'est pas déjà présent
            if continent.name in pays_par_continent:
                if pays.name not in pays_par_continent[continent.name]:
                    pays_par_continent[continent.name].append(pays.name)
            # sinon il faut créer la clé et initialiser la valeur
            else:
                pays_par_continent[continent.name] = [pays.name]

    return render_template("pages/continents.html",
        sous_titre="Continents",
        donnees=Map.query.paginate(page=page, per_page=app.config["PAYS_PER_PAGE"]),
        donnees_generales=pays_par_continent)

@app.route("/continents/<string:nom_continent>")
def un_continent(nom_continent):
    continent = Map.query.filter(Map.name == nom_continent).first()

    return render_template("pages/un_continent.html", 
        sous_titre=nom_continent, 
        donnees= Country.query.filter(Country.maps.contains(continent)).order_by(Country.name).all())

@app.route("/ressources")
@app.route("/ressources/<int:page>")
def ressources(page=1):
    # on va créer un dictionnaire (JSON) avec en clé les continents et en valeur une liste de pays
    # il faut initialiser ce dictionnaire au début 
    pays_par_ressource = {}

    for pays in Country.query.all():
        for ressource in pays.resources:
            # si la clé (ressource) existe déjà dans le dictionnaire, alors il est simplement nécessaire 
            # d'ajouter le pays s'il n'est pas déjà présent
            if ressource.name in pays_par_ressource:
                if pays.name not in pays_par_ressource[ressource.name]:
                    pays_par_ressource[ressource.name].append(pays.name)
            # sinon il faut créer la clé et initialiser la valeur
            else:
                pays_par_ressource[ressource.name] = [pays.name]
    
    return render_template("pages/ressources.html",
        sous_titre="Ressources",
        donnees=Resources.query.paginate(page=page, per_page=app.config["RESOURCES_PER_PAGE"]),
        donnees_generales=pays_par_ressource)

@app.route("/ressources/<string:nom_ressource>")
def une_ressource(nom_ressource):
    ressource = Resources.query.filter(Resources.name == nom_ressource).first()

    return render_template("pages/une_ressource.html", 
        sous_titre=nom_ressource, 
        donnees= Country.query.filter(Country.resources.contains(ressource)).order_by(Country.name).all())

@app.route("/recherche_rapide")
@app.route("/recherche_rapide/<int:page>")
def recherche_rapide(page=1):
    chaine =  request.args.get("chaine", None)
    if chaine:
        resources = db.session.execute(text("""select a.id from country a 
            inner join country_resources b on b.id = a.id 
            inner join resources c on c.name = b.resource
            and (c.name like '%"""+chaine+"""%' or  c.id like '%"""+chaine+"""%')
            """)).fetchall()
        maps = db.session.execute(text("""select a.id from country a 
            inner join country_map b on b.id = a.id 
            inner join map  c on c.name = b.map_ref 
            and (c.name like '%"""+chaine+"""%' or  c.id like '%"""+chaine+"""%')
            """)).fetchall()
        resultats = Country.query.filter(
                or_(
                    Country.name.ilike("%"+chaine+"%"),
                    Country.type.ilike("%"+chaine+"%"),
                    Country.Introduction.ilike("%"+chaine+"%"),
                    Country.id.in_([r.id for r in resources] + [m.id for m in maps])
                )
            ).distinct(Country.name).order_by(Country.name).\
            paginate(page=page, per_page=app.config["PAYS_PER_PAGE"])
    else:
        resultats = None     
    return render_template("pages/resultats_recherche_pays.html", 
            sous_titre= "Recherche | " + chaine, donnees=resultats,requete=chaine)

@app.route("/recherche", methods=['GET', 'POST'])
@app.route("/recherche/<int:page>", methods=['GET', 'POST'])
def recherche(page=1):
    form = Recherche() 

    # récupération des éventuels arguments de l'URL qui seraient le signe de l'envoi d'un formulaire
    nom_pays =  clean_arg(request.form.get("nom_pays", None))
    ressource =  clean_arg(request.form.get("ressources", None))
    continent =  clean_arg(request.form.get("continents", None))

    # initialisation des données de retour dans le cas où il n'y ait pas de requête
    donnees = []
    if form.validate_on_submit():
        # si l'un des champs de recherche a une valeur, alors cela veut dire que le formulaire a été rempli et qu'il faut lancer une recherche 
        # dans les données
        if nom_pays  or continent or ressource:
            # initialisation de la recherche; en fonction de la présence ou nom d'un filtre côté utilisateur, nous effectuerons des filtres SQLAlchemy,
            # ce qui signifie que nous pouvons jouer ici plusieurs filtres d'affilée
            query_results = Country.query

            if nom_pays:
                query_results = query_results.filter(Country.name.ilike("%"+nom_pays.lower()+"%"))
            
            if ressource:
                resource = db.session.execute(text("""select a.id from country a 
                    inner join country_resources b on b.id = a.id and b.resource  == '"""+ressource+"""'
                    """)).fetchall()
                query_results = query_results.filter(Country.id.in_([r.id for r in resource] ))
            
            if continent:
                map = db.session.execute(text("""select a.id from country a 
                    inner join country_map b on b.id = a.id and map_ref == '"""+continent+"""'
                    """)).fetchall()
                query_results = query_results.filter(Country.id.in_([m.id for m in map] ))
            
            donnees = query_results.order_by(Country.name).paginate(page=page, per_page=app.config["PAYS_PER_PAGE"])

            # renvoi des filtres de recherche pour préremplissage du formulaire
            form.nom_pays.data = nom_pays
            form.continents.data = continent
            form.ressources.data = ressource

    return render_template("pages/resultats_recherche.html", 
            sous_titre= "Recherche" , 
            donnees=donnees,
            form=form)