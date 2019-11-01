from Cices_enterprise import db
from datetime import datetime

class Staffs(db.Model):
    __tablename__ = 'Staffs'
    Id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String)
    first_name = db.Column(db.String)
    other_name = db.Column(db.String)
    home_address = db.Column(db.String)
    next_of_kin = db.Column(db.String)
    date_of_birth = db.Column(db.DateTime, default=datetime.utcnow())
    role = db.Column(db.String)
    telephone_contact = db.Column(db.String)
    email = db.Column(db.String)

    def __repr__(self):
        return f"{self.user_name, self.first_name, self.other_name, self.home_address, self.next_of_kin, self.date_of_birth, self.role, self.telephone_contact, self.email}"

