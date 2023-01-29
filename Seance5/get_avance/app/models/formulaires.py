from flask_wtf import FlaskForm
from wtforms import StringField, SelectField

class Recherche(FlaskForm):
    nom_pays = StringField("nom_pays", validators=[]) 
    ressources = SelectField('ressources', choices=[('', ''),('PET', 'pétrole'), ('GOL', 'or')])
    continents = SelectField('continents', choices=[('', ''),('Europe', 'Europe'), ('Asia', 'Asie'), ('Africa', 'Afrique')])