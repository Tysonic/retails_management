from Cices_enterprise import App,db



class Images(db.Model):
    Id = db.Column(db.Integer, primary_key =True)
    item_id = db.Column(db.integer)
    image = db.Column(db.string, len(128))

    def __init__(self, item_id, image):
        self.image = image
        self.item_id = item_id

    def __repr__(self):
        return f"{self.item_id,self.image}"