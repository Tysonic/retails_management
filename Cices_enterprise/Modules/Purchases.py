import datetime

from Cices_enterprise import db


class Purchases(db.Model):
    __tablename__ = "Purchases"
    purchase_id= db.Column(db.Integer, primary_key=True)
    unit_price = db.Column(db.Integer, nullable=False)
    purchase_date = db.Column(db.Date, default=datetime.datetime.utcnow())
    recorded_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    purchased_by = db.Column(db.String, nullable=False)
    updated_at = db.Column(db.DateTime)
    updated_by = db.Column(db.String)
    quantity_purchased = db.Column(db.Integer, nullable=False)
    item_purchased = db.Column(db.Integer, db.ForeignKey("Items.Id"))

    def __repr__(self):
        f"{self.price, self.item_purchased,self.quantity_purchased}, " \
        f"{self.recorded_at,self.purchased_by,self.purchase_date,self.unit_price, self.updated_at, self.updated_by}"
