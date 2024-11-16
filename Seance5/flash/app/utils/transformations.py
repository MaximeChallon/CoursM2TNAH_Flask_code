import re

def nettoyage_string_to_int(chaine):
    # Dans le cas où plusieurs informations sont données dans la chaine comme 
    # <strong>Saint Helena: </strong>60 km<br> <strong>Ascension Island: </strong>NA<br> <strong>Tristan da Cunha (island only): </strong>34 km
    # il faut retourner la somme de ces nombres
    res = None

    def clean(ch):
        res = re.sub(r'\(.*\)', '', ch) # pour supprimer les dates entre parenthèses
        res = re.sub(r'[^0-9\.]*', '', res) # pour supprimer tous les carctères sauf les points
        res = re.sub(r'\..*', '', res) # pour supprimer toutes les décimales
        if res:
            res = int(res)
        else:
            res = None
        return res
    
    if chaine :
        # cas normal 
        if "<" not in chaine:
            res = clean(chaine)
        # cas de la somme
        else :
            tmp = 0
            for el in chaine.split("<br"):
                tmp = tmp + int(clean(el))
            res = tmp
    return res

def clean_arg(arg):
    if arg == "":
        return None
    else:
        return arg
    
def to_bool(s):
    r = False 
    if(s.lower() == "true"):
        r = True
    elif(s.lower() == "false"):
        r = False
    return r