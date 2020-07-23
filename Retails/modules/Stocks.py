import datetime

from Retails import db


class Stocks(db.Model):
    __tablename__ = "Stocks"
    id= db.Column(db.Integer, primary_key=True)
    item_purchased = db.Column(db.Integer, db.ForeignKey('Items.id'))
    unit_price = db.Column(db.Integer, nullable=False)
    quantity_purchased = db.Column(db.Integer, nullable=False)
    purchase_date = db.Column(db.Date, default=datetime.datetime.utcnow())
    recorded_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    purchased_by = db.Column(db.String, nullable=False)
    updated_at = db.Column(db.DateTime)
    updated_by = db.Column(db.String)

    supplier = db.Column(db.String)


    def __repr__(self):
        return f"{self._Id, self.unit_price, self.item_purchased,self.quantity_purchased, self.recorded_at,self.purchased_by,self.purchase_date,self.unit_price, self.updated_at, self.updated_by, self.supplier}"

