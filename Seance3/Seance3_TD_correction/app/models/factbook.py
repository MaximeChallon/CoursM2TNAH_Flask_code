from ..app import db

class Country(db.Model):
    id = db.Column(db.String(10), primary_key=True)
    Introduction = db.Column(db.Text)
    name = db.Column(db.String(500))
    type = db.Column(db.String(100))