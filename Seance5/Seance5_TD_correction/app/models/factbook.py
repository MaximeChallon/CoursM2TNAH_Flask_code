from ..app import app, db
from ..utils.transformations import nettoyage_string_to_int

country_map = db.Table(
    "country_map",
    db.Column('id', db.String(100), db.ForeignKey('country.id'), primary_key=True),
    db.Column('map_ref', db.String(100), db.ForeignKey('map.name'), primary_key=True)
)

country_resources = db.Table(
    "country_resources",
    db.Column('id', db.String(100), db.ForeignKey('country.id'), primary_key=True),
    db.Column('resource', db.String(100), db.ForeignKey('resources.id'), primary_key=True)
)

country_country = db.Table(
    "country_country",
    db.Column('source', db.String(10), db.ForeignKey('country.id')),
    db.Column('target', db.String(10), db.ForeignKey('country.id'))
)

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

    maps = db.relationship(
        'Map', 
        secondary=country_map, 
        backref="maps"
    )
    resources = db.relationship(
        'Resources', 
        secondary=country_resources, 
        backref="resources"
    )

    #dependencies = db.relationship('Country',  secondary=country_country, backref="dependencies")

    dependences = db.relationship(
        'Country', secondary=country_country,
        primaryjoin=(country_country.c.source == id),
        secondaryjoin=(country_country.c.target == id),
        backref=db.backref('dependencies', lazy='dynamic'), lazy='dynamic')

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

    def total_int(self):
        return nettoyage_string_to_int(self.total)

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

    def coastline_int(self):
        return nettoyage_string_to_int(self.coastline)

    def irrigated_land_int(self):
        return nettoyage_string_to_int(self.irrigated_land)

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

class Map(db.Model):
    __tablename__ = "map"

    id = db.Column(db.String(100))
    name = db.Column(db.Text, primary_key=True)

    def __repr__(self):
        return '<Map %r>' % (self.name)

class Resources(db.Model):
    __tablename__ = "resources"

    id = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.Text)

    def __repr__(self):
        return '<Resources %r>' % (self.name)

    def get_resourceid(self):
        return Resources.query.filter(Resources.name == self.name).first().id

    def get_pays(self):
        pays_par_ressource = []

        for pays in Country.query.all():
            for ressource in pays.resources:
                if ressource == self:
                    if pays.name not in pays_par_ressource:
                        pays_par_ressource.append(pays.name)
        
        return pays_par_ressource