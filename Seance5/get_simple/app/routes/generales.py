from ..app import app, db
from flask import render_template, request
from sqlalchemy import or_
from ..models.factbook import Country, Resources, Map, Area, Boundaries

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
        resources = db.session.execute("""select a.id from country a 
            inner join country_resources b on b.id = a.id 
            inner join resources c on c.name = b.resource and (c.name like '%"""+chaine+"""%' or  c.id like '%"""+chaine+"""%')
            """).fetchall()
        
        maps = db.session.execute("""select a.id from country a 
            inner join country_map b on b.id = a.id 
            inner join map  c on c.name = b.map_ref and (c.name like '%"""+chaine+"""%' or  c.id like '%"""+chaine+"""%')
            """).fetchall()

        resultats = Country.query.\
            filter(
                or_(
                    Country.name.ilike("%"+chaine+"%"),
                    Country.type.ilike("%"+chaine+"%"),
                    Country.Introduction.ilike("%"+chaine+"%"),
                    Country.id.in_([r.id for r in resources] + [m.id for m in maps])
                )
            ).\
            distinct(Country.name).\
            order_by(Country.name).\
            paginate(page=page, per_page=app.config["PAYS_PER_PAGE"])
    else:
        resultats = None
        
    return render_template("pages/resultats_recherche_pays.html", 
            sous_titre= "Recherche | " + chaine, 
            donnees=resultats,
            requete=chaine)