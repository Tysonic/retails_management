from Cices_enterprise import App,db
from flask import Blueprint,render_template,request
from werkzeug.utils import secure_filename
import datetime

import os



class Images(db.Model):
    __tablename__="Images"
    _Id = db.Column(db.Integer, primary_key =True)
   # item_id = db.Column(db.Integer, db.ForeignKey("Items._Id"))
    image = db.Column(db.String)
    description = db.Column(db.String)
    status = db.Column(db.Integer, db.ForeignKey("Status._Id"))
    uploaded_on = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def __init__(self, item_id, image,description,status=1):
        self.image = image
        self.item_id = item_id

    def __repr__(self):
        return f"{self.item_id,self.image}"


class State(db.Model):
    __tablename__="Status"
    _Id = db.Column(db.Integer, primary_key=True)
    states = db.Column(db.String, unique=True)
    created_by = db.Column(db.String)
    created_at= db.Column(db.DateTime, default = datetime.datetime.utcnow())
    updated_by = db.Column(db.String)
    updated_at = db.Column(db.DateTime)
    image= db.relationship("Images",backref="images")



    def __repr__(self):
        return f"{self.status,self.created_by, self.created_at, self.updated_at, self.updated_by}"
