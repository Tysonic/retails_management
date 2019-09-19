from Cices_enterprise import db


class Sales(db.Model):
    Id = db.Column(db.Integer, primary_key =True, index=True)
    price = db.Column(db.String)
    date_sold = db.Column(db.DateTime)
    quantity_sold = db.Column(db.Integer)
    unit_sold = db.Column(db.String)
    sold_by = db.Column(db.String)
    sold_on = db.Column(db.DateTime)
    recorded_at = db.Column(db.DateTime)
    item_sold = db.Column(db.String)

    def __init__(self, price, date_sold, quantity_sold, unit_sold, sold_by, sold_on, recorded_at, item_sold):
        self.price = price
        self.date_sold = date_sold
        self.quantity_sold = quantity_sold
        self.unit_sold = unit_sold
        self.sold_by = sold_by
        self.sold_on = sold_on
        self.recorded_at = recorded_at
        self.item_sold = item_sold

    def __repr__(self):
        f"{self.price,self.date_sold, self.quantity_sold, self.unit_sold, self.sold_by, self.sold_on, self.recorded_at, self.item_sold}"

