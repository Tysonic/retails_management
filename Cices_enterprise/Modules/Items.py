from Cices_enterprise import db
from wtforms.validators import DataRequired
from Cices_enterprise.Modules.Purchases import Purchases
from Cices_enterprise.Modules.Sales import Sales

class Items(db.Model):
    __tablename__ = "Items"
    Id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String, unique=True)
    size = db.Column(db.Integer)
    unit = db.Column(db.String)
    packaging = db.Column(db.String)
    created_by = db.Column(db.String)
    created_at = db.Column(db.DateTime)
    sales = db.relationship('Sales', backref='sales')
    purchases = db.relationship('Purchases', backref='purchase')


    def __init__(self,name, unit="", size=0, packaging="", created_by="", created_at=None):
        self.name = name
        self.unit = unit
        self.size = size
        self.packaging = packaging
        self.created_by = created_by
        self.created_at = created_at

    def __repr__(self):
        return f"{self.name, self.unit, self.size, self.packaging,self.created_by,self.created_at} "
