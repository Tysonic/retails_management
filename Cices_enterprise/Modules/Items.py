from Cices_enterprise import db
from wtforms.validators import DataRequired
from Cices_enterprise.Modules.Purchases import Purchases
from Cices_enterprise.Modules.Sales import Sales
from datetime import datetime
from Cices_enterprise.Modules.Uploads import Images


class Items(db.Model):
    __tablename__ = "Items"
    _Id = db.Column(db.Integer, primary_key=True, index=True)
    item = db.Column(db.String)
    name = db.Column(db.Integer, db.ForeignKey('ItemNames.name_id'))
    size = db.Column(db.Integer, nullable=True)
    brand = db.Column(db.Integer, db.ForeignKey('ItemBrands.brand_id'))
    unit = db.Column(db.Integer, db.ForeignKey('ItemUnits.unit_id'))
    packaging = db.Column(db.Integer, db.ForeignKey('ItemPackaging.packaging_id'))
    stock = db.Column(db.Integer, default=0)
    created_by = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_by = db.Column(db.String, default="")
    updated_at = db.Column(db.DateTime, default=None)
    sales = db.relationship('Sales', backref='sales')
    purchases = db.relationship('Purchases', backref='purchase')

    # image = db.relationship("Images", backref='image')

    def __init__(self, stock,name,item, created_by,   size, brand, unit,
                 packaging, updated_at=None,  updated_by=""):
        self.name = name
        self.unit = unit
        self.item = item
        self.updated_at = updated_at
        self.updated_by = updated_by
        self.size = size
        self.brand = brand
        self.stock = stock
        self.packaging = packaging
        self.created_by = created_by

    def __repr__(self):
        return f"{self.name,self.item, self.unit, self.size, self.brand, self.packaging,self.created_by, self.created_at, self.updated_at, self.updated_by, self.stock} "
