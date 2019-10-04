from app import db
from sqlalchemy.dialects.postgresql import JSON

class NewTitles(db.Model):
    __tablename__ = 'newtitles'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    precision_code = db.Column(db.Integer)
    region = db.Column(db.String())
    location = db.Column(db.String())
    pleiades_id = db.Column(db.String())
    latitude = db.Column(db.Numeric)
    longitude = db.Column(db.Numeric)
    bsn = db.Column(db.String(7), nullable=False)

    def __init__(self, id, date, precision_code, region, location, pleiades_id, latitute, longitude, bsn):
        self.self = self
        self.id = id
        self.date = date
        self.precision_code = precision_code
        self.region = region
        self.location = location
        self.pleiades_id = pleiades_id
        self.latitute = latitute
        self.longitude = longitude
        self.bsn = bsn
    
    def __repr__(self):
        return '<id {}>'.format(self.id)
