from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from Retails import db


class Accounts(db.Model, UserMixin):
    __tablename__ = "Accounts"
    # __bind_key__="Accounts"
    id = db.Column(db.Integer, primary_key=True, index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, email, password, username):
        self.email = email
        self.password_hash = generate_password_hash(password)
        self.username = username

    def __repr__(self):
        return f"{self.email, self.password_hash, self.username}"
