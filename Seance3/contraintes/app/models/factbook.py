from ..app import app, db

class Area(db.Model):
    __tablename__ = "area"

    id = db.Column(db.String(100))
    area_comparative = db.Column(db.Text)
    total = db.Column(db.String(100))
    land = db.Column(db.String(100))
    water = db.Column(db.String(100))
    note = db.Column(db.String(1000))

class Boundaries(db.Model):
    __tablename__ = "boundaries"

    id = db.Column(db.String(100))
    total = db.Column(db.String(100))
    border_countries = db.Column(db.String(1000))
    note = db.Column(db.String(1000))

class Country(db.Model):
    __tablename__ = "country"

    id = db.Column(db.String(10), primary_key=True)
    Introduction = db.Column(db.Text)
    name = db.Column(db.String(500), unique=True, nullable=False)
    type = db.Column(db.String(100))

    def __repr__(self):
        return '<Country %r>' % (self.name)

class Elevation(db.Model):
    __tablename__ = "elevation"

    id = db.Column(db.String(100))
    highest_point = db.Column(db.String(100))
    lowest_point = db.Column(db.String(100))
    mean_elevation = db.Column(db.String(100))
    note =db.Column(db.Text)

class Geography(db.Model):
    __tablename__ = "geography"

    id = db.Column(db.String(100))
    location = db.Column(db.String(1000))
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

class Landuse(db.Model):
    __tablename__ = "landuse"

    id = db.Column(db.String(100))
    agricultural_land = db.Column(db.Text)
    arable_land = db.Column(db.Text)
    permanent_crops = db.Column(db.Text)
    permanent_pasture = db.Column(db.Text)
    forest = db.Column(db.Text)
    other = db.Column(db.Text)

class Map(db.Model):
    __tablename__ = "map"

    id = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.Text)

    def __repr__(self):
        return '<Map %r>' % (self.name)

class Resources(db.Model):
    __tablename__ = "resources"

    id = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.Text)

    def __repr__(self):
        return '<Resources %r>' % (self.name)