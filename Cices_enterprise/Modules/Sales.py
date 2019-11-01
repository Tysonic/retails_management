from Cices_enterprise import db
from datetime import datetime

class Sales(db.Model):
    __tablename__ = "Sales"
    Id = db.Column(db.Integer, primary_key =True, index=True)
    unit_price = db.Column(db.Integer, nullable=False)
    quantity_sold = db.Column(db.Integer, nullable=False)
    sold_by = db.Column(db.String)
    sold_on = db.Column(db.DateTime)
    recorded_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_by = db.Column(db.String)
    updated_at= db .Column(db.DateTime)
    item_sold = db.Column(db.String, db.ForeignKey('Items.Id'))


    def __repr__(self):
        f"{self.price,self.date_sold, self.quantity_sold, self.unit_sold, self.sold_by, self.recorded_at, self.item_sold}"
