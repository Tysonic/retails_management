import re
from Retails.modules.Accounts import Accounts
from flask_wtf import FlaskForm
from werkzeug.routing import ValidationError
from wtforms import SubmitField, PasswordField, StringField
from wtforms.validators import DataRequired, Email, EqualTo


class UserRegitrationForm(FlaskForm):
    username = StringField("User Name", validators=[DataRequired(message="User Name required")])
    email = StringField("Email", validators=[DataRequired(message="Email Required"), Email()])
    password = PasswordField("Password",
                             validators=[DataRequired(message="Enter password"), EqualTo("confirm_password")])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(message="Please confirm password")])

    submit = SubmitField("Register")


    def check_email(self, field):
        if Accounts.query.filter_by(self.email == field.data).first():
            raise ValidationError("your email has already been registered")


    def check_username(self, field):
        if Accounts.query.filter_by(self.username == field.data).first():
            raise ValidationError("Username already exitst")

    def check_password(self, field):
        if len(field.password < 8):
            raise ValidationError("Password must be at least 8 characters long")
        if not re.search(r"[\d]+", field.password):
            raise ValidationError("This password must contain at least 1 digit")
        if re.search(r"[A-Z]+", field.password.data):
            raise ValidationError("This password must contain at least 1 uppercase characte")


class UserLoginForm(FlaskForm):
    email = StringField("Email")
    password = PasswordField("Password")
    submit = SubmitField("Login")
