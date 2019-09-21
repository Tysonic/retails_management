from Cices_enterprise import db


class Staffs(db.Model):
    __tablename__ = 'Staffs'
    user_name = db.Column(db.String, primary_key=True, index=True, unique=True)
    first_name = db.Column(db.String)
    other_name = db.Column(db.String)
    home_address = db.Column(db.String)
    next_of_kin = db.Column(db.String)
    date_of_birth = db.Column(db.DateTime)
    role = db.Column(db.String)
    telephone_contact = db.Column(db.String)
    email = db.Column(db.String)

    def __init__(self, user_name, first_name, other_name, home_address, next_of_kin, date_of_birth, role, telephone_contact, email):
        self.user_name = user_name
        self.first_name = first_name
        self.other_name = other_name
        self.home_address = home_address
        self.next_of_kin = next_of_kin
        self.date_of_birth = date_of_birth
        self.role = role
        self.telephone_contact = telephone_contact
        self.email = email

    def __repr__(self):
        return f"{self.user_name, self.first_name, self.other_name, self.home_address, self.next_of_kin, self.date_of_birth, self.role, self.telephone_contact, self.email}"

