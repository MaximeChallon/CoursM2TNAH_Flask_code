from ..app import app, db

class Country(db.Model):
    __tablename__ = "country"

    id = db.Column(db.String(10), primary_key=True)
    Introduction = db.Column(db.Text)
    name = db.Column(db.String(500), unique=True, nullable=False)
    type = db.Column(db.String(100))

    def __repr__(self):
        return '<Country %r>' % (self.name)
