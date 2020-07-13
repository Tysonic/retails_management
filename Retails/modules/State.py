from Retails import db
import datetime

import os


class State(db.Model):
    __tablename__="State"
    _Id = db.Column(db.Integer, primary_key=True)
    states = db.Column(db.String, unique=True)
    created_by = db.Column(db.String)
    created_at= db.Column(db.DateTime, default = datetime.datetime.utcnow())
    updated_by = db.Column(db.String)
    updated_at = db.Column(db.DateTime)
    image_state= db.relationship("Images",backref="image_states")



    def __repr__(self):
        return f"{self.status,self.created_by, self.created_at, self.updated_at, self.updated_by}"
