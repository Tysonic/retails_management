from Cices_enterprise import db
from datetime import datetime


class Sales(db.Model):
    __tablename__ = "Sales"
    _Id = db.Column(db.Integer, primary_key=True, index=True)
    unit_price = db.Column(db.Integer, nullable=False)
    quantity_sold = db.Column(db.Integer, nullable=False)
    sold_by = db.Column(db.String)
    sold_on = db.Column(db.DateTime)
    recorded_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_by = db.Column(db.String)
    updated_at = db.Column(db.DateTime)
    item_sold = db.Column(db.Integer, db.ForeignKey('Items._Id'))

    def __repr__(self):
        return f"{self.unit_price, self.quantity_sold, self.sold_by, self.recorded_at, self.item_sold, self.updated_by, self.updated_at,self.sold_on}"
