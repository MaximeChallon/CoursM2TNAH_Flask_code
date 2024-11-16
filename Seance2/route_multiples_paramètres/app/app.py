from flask import Flask
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/home/<string:id>")
def home(id:str):
    return "Hello world! On a demandé l'identifiant " + id

@app.route("/calcul/<string:type_calcul>/<float:f1>/<float:f2>")
def calcul(type_calcul:str, f1:float, f2:float):
    if(type_calcul == "multiplication"):
        return build_result(type_calcul, f1, f2, round(f1*f2, 5))
    elif(type_calcul == "division"):
        return build_result(type_calcul, f1, f2, round(f1/f2, 5))
    elif(type_calcul == "addition"):
        return build_result(type_calcul, f1, f2, round(f1+f2, 5))
    elif(type_calcul == "soustraction"):
        return build_result(type_calcul, f1, f2, round(f1-f2, 5))
    else:
        return "Opération " + type_calcul + " inconnue"
    
def build_result(type_calcul:str, f1:float, f2:float, f:float):
    return "Le résultat de " + type_calcul + " de " + str(f1) + " et " + str(f2) + " est " + str(f)