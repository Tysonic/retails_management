from Retails import db
from datetime import datetime


class Sales(db.Model):
    __tablename__ = "sales"
    _Id = db.Column(db.Integer, primary_key=True, index=True)
    items = db.Column(db.String)
    seller = db.Column(db.String)
    sold_to = db.Column(db.String)
    date_sold = db.Column(db.DateTime)
    updater = db.Column(db.String)
    updated_at = db.Column(db.DateTime)
    total_amount = db.Column(db.Integer)
    cash_paid = db.Column(db.Integer)


    def __repr__(self):
        return f"{self.unit_price, self.quantity_sold, self.sold_by, self.recorded_at, self.item_sold, self.updated_by, self.updated_at,self.sold_on}"
