from Cices_enterprise import db
from Cices_enterprise.Modules.Items import Items


class ItemUnits(db.Model):
    """Item units model"""
    __tablename__ = "ItemUnits"
    _Id = db.Column(db.Integer, primary_key=True)
    unit = db.Column(db.String, nullable=False)
    item = db.relationship("Items", backref="item_unit")

    def __init__(self, unit=""):
        self.unit = unit

    def __repr__(self):
        return f"{self.unit, self._Id}"


class ItemPackaging(db.Model):
    """Item Packaging model"""
    __tablename__ = "ItemPackaging"
    _Id = db.Column(db.Integer, primary_key=True)
    packaging = db.Column(db.String, nullable=False)
    item = db.relationship("Items", backref="item_packaging")

    def __init__(self, packaging):
        self.packaging = packaging

    def __repr__(self):
        return f"{self.packaging, self._Id}"


class ItemNames(db.Model):
    """Model for item names"""
    __tablename__ = "ItemNames"
    _Id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String)
    item = db.relationship("Items", backref="item_name")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.name,self._Id}"


class ItemBrands(db.Model):
    """Item brand model"""
    __tablename__ = "ItemBrands"
    _Id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String, nullable=False)
    item = db.relationship("Items", backref="item_brand")

    def __init__(self, brand):
        self.brand = brand

    def __repr__(self):
        return f"{self.brand,self._Id}"
