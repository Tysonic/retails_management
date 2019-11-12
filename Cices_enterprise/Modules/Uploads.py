from Cices_enterprise import App,db
from flask import Blueprint,render_template,request
from werkzeug.utils import secure_filename
from Cices_enterprise import upload
import os



class Images(db.Model):
    Id = db.Column(db.Integer, primary_key =True)
    item_id = db.Column(db.Integer)
    image = db.Column(db.String)

    def __init__(self, item_id, image):
        self.image = image
        self.item_id = item_id

    def __repr__(self):
        return f"{self.item_id,self.image}"