import dotenv
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dotenv.load_dotenv(os.path.join(BASE_DIR, '.env'))

def to_bool(s):
    r = False 
    if(s.lower() == "true"):
        r = True
    elif(s.lower() == "false"):
        r = False
    return r

class Config():
    DEBUG = to_bool(os.environ.get("DEBUG"))