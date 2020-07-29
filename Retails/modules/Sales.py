from Retails import db
from datetime import date


class Sales(db.Model):
    __tablename__ = "sales"
    id = db.Column(db.Integer, primary_key=True, index=True)
    item = db.Column(db.Integer, db.ForeignKey('Items.id'))
    price = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    sold_by = db.Column(db.String)
    sold_to = db.Column(db.String)
    sold_at = db.Column(db.Date)
    updated_by = db.Column(db.String)
    updated_at = db.Column(db.DateTime)


    def __repr__(self):
        return f"{self.unit_price, self.quantity_sold, self.sold_by, self.recorded_at, self.item, self.price,self.quantity,self.updated_by, self.updated_at,self.sold_on}"
