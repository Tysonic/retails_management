from Cices_enterprise import db


class Purchases(db.Model):
    __tablename__ = "Purchases"
    Id = db.Column(db.Integer, primary_key =True, index=True)
    price = db.Column(db.String)
    # date_purchased = db.Column(db.DateTime)
    # quantity_purchased = db.Column(db.Integer)
    # purchased_by = db.Column(db.String)
    # purchased_on = db.Column(db.DateTime)
    # recorded_at = db.Column(db.DateTime)
    item_purchased = db.Column(db.String, db.ForeignKey('Items.Id'))

    def __init__(self, price, date_purchased, quantity_purchased, purchased_by, purchased_on, recorded_at, item_purchased):
        self.price = price
        # self.date_purchased= date_purchased
        # self.quantity_purchased = quantity_purchased
        # self.purchased_by = purchased_by
        # self.purchased_on = purchased_on
        # self.recorded_at = recorded_at
        self.item_purchased = item_purchased

    def __repr__(self):
        f"{self.price, self.item_purchased}"
