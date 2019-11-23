from Cices_enterprise import App,db
from flask import Blueprint,render_template,request
from werkzeug.utils import secure_filename
from Cices_enterprise.Modules.State import State
import datetime

import os



class Images(db.Model):
    __tablename__="Images"
    _Id = db.Column(db.Integer, primary_key =True)
   # item_id = db.Column(db.Integer, db.ForeignKey("Items._Id"))
    image = db.Column(db.String)
    description = db.Column(db.String)
    status = db.Column(db.Integer, db.ForeignKey("State._Id"))
    uploaded_on = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def __repr__(self):
        return f"{self.item_id,self.image}"
