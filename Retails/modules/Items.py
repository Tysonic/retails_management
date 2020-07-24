from Retails import db


class Items(db.Model):
    __tablename__ = "Items"
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String)
    unit_stock=db.Column(db.String)
    unit_sales = db.Column(db.String)
    sales_per_stock = db.Column(db.Integer)
    size = db.Column(db.String)
    category = db.Column(db.String)
    selling_price = db.Column(db.Integer)
    buying_price = db.Column(db.Integer)
    created_by = db.Column(db.String)
    created_at = db.Column(db.DateTime)
    updated_by = db.Column(db.String)
    updated_at = db.Column(db.DateTime)
    initials = db.relationship("InitialItems", backref='initials')
    sales = db.relationship("Sales", backref='sales')
    stock = db.relationship("Stocks", backref='stocks')


    # def __init__(self,name,unit_stock,unit_sales,sales_per_stock,size,category, created_at, created_by, updated_at="", updated_by=""):
    #     self.name = name
    #     self.unit_sales = unit_sales
    #     self.unit_stock=unit_stock
    #     self.size = size
    #     self.category = category
    #     self.sales_per_stock = sales_per_stock
    #     self.updated_at = updated_at
    #     self.updated_by = updated_by
    #     self.created_at = created_at
    #     self.created_by = created_by


    def __repr__(self):
        return f"{self.sales_per_stock,self.unit_sales,self.category,self.name,self.size,self.id,self.unit_stock,self.created_by, self.created_at,self.updated_by, self.updated_at}"