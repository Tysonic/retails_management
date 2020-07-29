from Retails import db


class InitialItems(db.Model):
    __tablename__ = 'InitialItems'
    id = db.Column(db.Integer, primary_key=True, index=True)
    item = db.Column(db.Integer, db.ForeignKey('Items.id'))
    sales_quantity = db.Column(db.Integer)
    create_by = db.Column(db.String)
    created_at = db.Column(db.DateTime)

    def __init__(self, item, sales_quantity, created_by, created_at):
        self.item = item
        self.sales_quantity = sales_quantity
        self.create_by = created_by
        self.create_at = created_at

    def __repr__(self):
        f"{self.sales_quantity, self.item, self.create_by, self.created_at}"


class InitialCash(db.Model):
    __tablename__ = 'InitialCash'
    id = db.Column(db.Integer, primary_key=True, index=True)
    cash = db.Column(db.Integer)
    create_by = db.Column(db.String)
    created_at = db.Column(db.DateTime)

    def __init__(self, cash, created_by, created_at):
        self.cash = cash
        self.create_by = created_by
        self.created_at = created_at

    def __repr__(self):
        f" {self.cash, self.create_by, self.created_at} "