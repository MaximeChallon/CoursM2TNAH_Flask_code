from ..app import app, db

class Area(db.Model):
    id = db.Column(db.String(100))
    area_comparative = db.Column(db.Text)
    total = db.Column(db.String(100))
    land = db.Column(db.String(100))
    water = db.Column(db.String(100))
    note = db.Column(db.String(1000))

class Boundaries(db.Model):
    id = db.Column(db.String(100))
    total = db.Column(db.String(100))
    border_countries = db.Column(db.String(1000))
    note = db.Column(db.String(1000))

class Country(db.Model):
    id = db.Column(db.String(10))
    Introduction = db.Column(db.Text)
    name = db.Column(db.String(500))
    type = db.Column(db.String(100))

class Elevation(db.Model):
    id = db.Column(db.String(100))
    highest_point = db.Column(db.String(100))
    lowest_point = db.Column(db.String(100))
    mean_elevation = db.Column(db.String(100))
    note =db.Column(db.Text)

class Geography(db.Model):
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
    id = db.Column(db.String(100))
    agricultural_land = db.Column(db.Text)
    arable_land = db.Column(db.Text)
    permanent_crops = db.Column(db.Text)
    permanent_pasture = db.Column(db.Text)
    forest = db.Column(db.Text)
    other = db.Column(db.Text)

class Map(db.Model):
    id = db.Column(db.String(100))
    name = db.Column(db.Text)

class Resources(db.Model):
    id = db.Column(db.String(100))
    name = db.Column(db.Text)