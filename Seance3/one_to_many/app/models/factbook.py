from ..app import app, db

class Country(db.Model):
    __tablename__ = "country"

    id = db.Column(db.String(10), primary_key=True)
    Introduction = db.Column(db.Text)
    name = db.Column(db.String(500), unique=True, nullable=False)
    type = db.Column(db.String(100))

    # propriétés de relation
    areas = db.relationship('Area',  backref='areas',  lazy=True)
    boundaries = db.relationship('Boundaries',  backref='boundaries',  lazy=True)
    elevations = db.relationship('Elevation',  backref='elevations',  lazy=True)
    geographies = db.relationship('Geography',  backref='geographies',  lazy=True)    
    landuses = db.relationship('Landuse',  backref='landuses',  lazy=True)

    def __repr__(self):
        return '<Country %r>' % (self.name) 

class Area(db.Model):
    __tablename__ = "area"

    area_comparative = db.Column(db.Text)
    total = db.Column(db.String(100), primary_key=True)
    land = db.Column(db.String(100))
    water = db.Column(db.String(100))
    note = db.Column(db.String(1000))

    # clés étrangères
    id = db.Column(
        db.String(100),  
        db.ForeignKey('country.id')
    )

    def __repr__(self):
        return '<Area %r>' % (self.total) 

class Boundaries(db.Model):
    __tablename__ = "boundaries"

    total = db.Column(db.String(100), primary_key=True)
    border_countries = db.Column(db.String(1000))
    note = db.Column(db.String(1000))

    # clés étrangères
    id = db.Column(
        db.String(100),  
        db.ForeignKey('country.id')
    )

    def __repr__(self):
        return '<Boundaries %r>' % (self.total) 

class Elevation(db.Model):
    __tablename__ = "elevation"

    highest_point = db.Column(db.String(100), primary_key=True)
    lowest_point = db.Column(db.String(100))
    mean_elevation = db.Column(db.String(100))
    note =db.Column(db.Text)

    # clés étrangères
    id = db.Column(
        db.String(100),  
        db.ForeignKey('country.id')
    )

    def __repr__(self):
        return '<Elevation %r>' % (self.highest_point)

class Geography(db.Model):
    __tablename__ = "geography"

    location = db.Column(db.String(1000), primary_key=True)
    coordinates = db.Column(db.String(100))
    coastline = db.Column(db.String(100))
    climate = db.Column(db.Text)
    terrain = db.Column(db.Text)
    irrigated_land = db.Column(db.Text)
    fresh_water_lakes = db.Column(db.Text)
    salted_water_lakes = db.Column(db.Text)
    major_rivers = db.Column(db.Text)
    major_watersheds = db.Column(db.Text)
    major_aquifers = db.Column(db.Text)
    population_distribution = db.Column(db.Text)
    natural_hazards = db.Column(db.Text)
    geography_note = db.Column(db.Text) 

    # clés étrangères
    id = db.Column(
        db.String(100),  
        db.ForeignKey('country.id')
    )

    def __repr__(self):
        return '<Geography %r>' % (self.location)

class Landuse(db.Model):
    __tablename__ = "landuse"

    landuse_id = db.Column(db.Integer, primary_key=True)
    agricultural_land = db.Column(db.Text)
    arable_land = db.Column(db.Text)
    permanent_crops = db.Column(db.Text)
    permanent_pasture = db.Column(db.Text)
    forest = db.Column(db.Text)
    other = db.Column(db.Text)

    # clés étrangères
    id = db.Column(
        db.String(100),  
        db.ForeignKey('country.id')
    )

    def __repr__(self):
        return '<Landuse %r>' % (self.landuse_id)